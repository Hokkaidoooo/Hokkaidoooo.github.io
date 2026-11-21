"""Build the static portfolio translations; run with --check to detect drift."""

import argparse
from html import escape, unescape
from html.parser import HTMLParser
from itertools import accumulate
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://hokkaidoooo.github.io/'
OG_LOCALE = {'en': 'en_US', 'es': 'es_ES', 'ja': 'ja_JP'}
HAN = re.compile(r'[\u3400-\u9fff]')


class Translation(HTMLParser):
    def __init__(self, source, language, messages):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.language = language
        self.messages = messages
        self.used = set()
        self.edits = []
        self.offsets = [0, *accumulate(map(len, source.splitlines(keepends=True)))]

    def replace(self, original, replacement):
        start = self.source_offset()
        if not self.source.startswith(original, start):
            raise ValueError(f'Unexpected markup at offset {start}')
        self.edits.append((start, start + len(original), replacement))

    def source_offset(self):
        line, column = self.getpos()
        return self.offsets[line - 1] + column

    def translate(self, value):
        key = value.strip()
        if key not in self.messages and not HAN.search(key):
            return value
        self.used.add(key)
        return value.replace(key, self.messages[key])

    def localized_url(self, url):
        parts = urlsplit(url)
        if not parts.scheme and parts.path and not url.startswith('/'):
            return posixpath.relpath(url, self.language)
        if url == SITE + 'blog/':
            return f'{url}{self.language}/'
        if url == 'https://github.com/Hokkaidoooo':
            return f'{url}/Hokkaidoooo/blob/main/README.{self.language}.md'
        if parts.netloc == 'github.com' and re.fullmatch(r'/Hokkaidoooo/[\w.-]+', parts.path):
            return f'{url}/blob/main/README.{self.language}.md'
        return url

    def handle_starttag(self, tag, attrs):
        source = self.get_starttag_text()
        original = dict(attrs)
        result = original.copy()
        for attr in ('aria-label', 'alt', 'title', 'content'):
            if attr in result:
                result[attr] = self.translate(result[attr])
        if tag == 'html':
            result['lang'] = self.language
        elif tag == 'meta' and result.get('property') == 'og:locale':
            result['content'] = OG_LOCALE[self.language]
        elif tag == 'meta' and result.get('property') == 'og:url':
            result['content'] = f'{SITE}{self.language}/'
        elif tag == 'link' and result.get('rel') == 'canonical':
            result['href'] = f'{SITE}{self.language}/'
        elif 'href' in result:
            result['href'] = self.localized_url(result['href'])
        if 'src' in result:
            result['src'] = self.localized_url(result['src'])
        if tag == 'a' and 'hreflang' in result:
            result.pop('aria-current', None)
            if result['hreflang'] == self.language:
                result['aria-current'] = 'page'
        if original != result:
            attributes = ''.join(f' {k}' if v is None else f' {k}="{escape(v, quote=True)}"' for k, v in result.items())
            self.replace(source, f'<{tag}{attributes}>')

    def handle_data(self, data):
        if data.strip() in {'简体中文', '日本語'}:
            return  # Language names keep their endonyms in the selector.
        translated = self.translate(data)
        if translated != data:
            start = self.source_offset()
            end = self.source.find('<', start)
            raw = self.source[start:end if end != -1 else len(self.source)]
            if unescape(raw) != data:
                raise ValueError(f'Unexpected source text at offset {start}')
            self.replace(raw, escape(translated, quote=False))

    def render(self):
        self.feed(self.source)
        self.close()
        unused = self.messages.keys() - self.used
        if unused:
            raise ValueError(f'Obsolete translations: {sorted(unused)}')
        result = self.source
        for start, end, replacement in reversed(self.edits):
            result = result[:start] + replacement + result[end:]
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    options = parser.parse_args()
    source = (ROOT / 'index.html').read_text(encoding='utf-8')
    catalog = json.loads((ROOT / 'tools' / 'home-copy.json').read_text(encoding='utf-8'))
    languages = catalog['languages']
    if set(languages) != OG_LOCALE.keys() or len(languages) != len(OG_LOCALE):
        raise ValueError('Language columns must match the supported locales')
    columns = {key: dict(zip(languages, row, strict=True)) for key, row in catalog['messages'].items()}
    if any(not isinstance(v, str) or not v.strip() for row in columns.values() for v in row.values()):
        raise ValueError('Every message must have a nonblank translation in every language')
    for lang in languages:
        target = ROOT / lang / 'index.html'
        result = Translation(source, lang, {k: v[lang] for k, v in columns.items()}).render()
        if options.check:
            if target.read_text(encoding='utf-8') != result:
                raise SystemExit(f'Stale page: {target.relative_to(ROOT)}')
        else:
            target.parent.mkdir(exist_ok=True)
            target.write_text(result, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
