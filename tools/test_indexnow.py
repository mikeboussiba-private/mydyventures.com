import json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indexnow

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.app/</loc></url>
  <url><loc>https://example.app/why</loc></url>
</urlset>"""

class IndexNowTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        open(os.path.join(self.root, 'sitemap.xml'), 'w').write(SITEMAP)
        self.key = 'a' * 32
        open(os.path.join(self.root, f'{self.key}.txt'), 'w').write(self.key)

    def test_payload_lists_every_sitemap_url(self):
        p = indexnow.build_payload(self.root)
        self.assertEqual(p['host'], 'example.app')
        self.assertEqual(p['key'], self.key)
        self.assertEqual(p['keyLocation'], f'https://example.app/{self.key}.txt')
        self.assertEqual(p['urlList'], ['https://example.app/', 'https://example.app/why'])

    def test_missing_key_file_fails_loudly(self):
        os.remove(os.path.join(self.root, f'{self.key}.txt'))
        with self.assertRaises(SystemExit):
            indexnow.build_payload(self.root)

    def test_key_file_must_contain_its_own_name(self):
        open(os.path.join(self.root, f'{self.key}.txt'), 'w').write('wrong')
        with self.assertRaises(SystemExit):
            indexnow.build_payload(self.root)

if __name__ == '__main__':
    unittest.main()
