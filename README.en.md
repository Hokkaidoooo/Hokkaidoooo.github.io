# Hokkaido’s portfolio

[简体中文](README.md) · **English** · [Español](README.es.md) · [日本語](README.ja.md)

**[Open the portfolio in English](https://hokkaidoooo.github.io/en/)** · [Notes](https://hokkaidoooo.github.io/blog/en/) · [GitHub profile](https://github.com/Hokkaidoooo)

Follow an HTTP request through a C++ server, compare cache replacement policies in a browser, or explore how risk propagates along a supply chain. Each project links to its repository. Other sections cover a material requirements planner, tools for offline reading, multibeam survey planning and a year of weather in Nanjing. Captions distinguish working interfaces, diagrams and synthetic data. The blog has a translated index; the articles are in Chinese.

## View locally

Open `en/index.html` directly, or run this command from the repository root and visit <http://127.0.0.1:4186/en/>:

```sh
python -m http.server 4186 --bind 127.0.0.1
```

The site is static HTML and CSS. It works without JavaScript, third-party fonts, analytics, cookies or a frontend build. All images are served with the page. GitHub Pages and external project sites have their own service policies.

## Structure and images

- [`index.html`](index.html) contains the shared layout, Chinese copy and project links. [`tools/home-copy.json`](tools/home-copy.json) contains the English, Spanish and Japanese text. With Python 3.10+, run `python tools/localize.py` after an edit; `python tools/localize.py --check` checks that all three pages are up to date.
- [`assets/site.css`](assets/site.css) is shared by all languages. The pages include a keyboard skip link, visible focus indicators and reduced-motion support. GitHub Pages serves the committed files from the root of `main`.
- The [images](assets/) come from the linked public projects: the systems lab is a screenshot, the risk example uses synthetic data and the weather charts summarize the 2023 records. The server, MRP and news portal graphics are diagrams. Sources and cropping details are in the [Chinese image credits](README.md#图片来源).
