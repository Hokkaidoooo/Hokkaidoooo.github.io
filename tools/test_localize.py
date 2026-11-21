import unittest

from localize import Translation


class TranslationTest(unittest.TestCase):
    def test_translates_entities_and_rejects_markup_in_copy(self):
        page = Translation('<p>项目 &amp; 工具</p>', 'en', {'项目 & 工具': 'Projects & <tools>'})
        self.assertEqual(page.render(), '<p>Projects &amp; &lt;tools&gt;</p>')

    def test_requires_current_translations(self):
        with self.assertRaises(KeyError):
            Translation('<p>新项目</p>', 'ja', {}).render()
        with self.assertRaisesRegex(ValueError, 'Obsolete'):
            Translation('<p>HTML</p>', 'es', {'旧项目': 'Anterior'}).render()

    def test_links_follow_the_selected_language(self):
        page = Translation('', 'ja', {})
        self.assertEqual(page.localized_url('en/index.html'), '../en/index.html')
        self.assertEqual(page.localized_url('#tools'), '#tools')
        self.assertEqual(page.localized_url('https://github.com/Hokkaidoooo/tracedesk'),
                         'https://github.com/Hokkaidoooo/tracedesk/blob/main/README.ja.md')
        self.assertEqual(page.localized_url('https://hokkaidoooo.github.io/blog/'),
                         'https://hokkaidoooo.github.io/blog/ja/')


if __name__ == '__main__':
    unittest.main()
