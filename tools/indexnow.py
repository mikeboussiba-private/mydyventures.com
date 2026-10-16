#!/usr/bin/env python3
"""Tell IndexNow engines (Bing, Yandex, Seznam, Naver) the site changed.

Bing also feeds DuckDuckGo and ChatGPT search, so this is the fastest way to
get a deploy recrawled. Google ignores IndexNow; it reads sitemap.xml.

Usage: tools/indexnow.py <served-dir>        # after every deploy
The key file (<32 hex>.txt, containing its own name) lives in the served dir;
it is public by design — it only proves we control the host.
"""
import glob, json, os, re, sys, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

ENDPOINT = 'https://api.indexnow.org/indexnow'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


def _key(root):
    for path in glob.glob(os.path.join(root, '*.txt')):
        name = os.path.basename(path)[:-4]
        if re.fullmatch(r'[0-9a-f]{32}', name):
            if open(path).read().strip() != name:
                sys.exit(f'indexnow: {path} must contain exactly {name}')
            return name
    sys.exit(f'indexnow: no <32-hex>.txt key file in {root}')


def build_payload(root):
    urls = [loc.text.strip() for loc in ET.parse(os.path.join(root, 'sitemap.xml')).getroot().iterfind('s:url/s:loc', NS)]
    host = urllib.parse.urlsplit(urls[0]).hostname
    key = _key(root)
    return {'host': host, 'key': key, 'keyLocation': f'https://{host}/{key}.txt', 'urlList': urls}


def main():
    payload = build_payload(sys.argv[1] if len(sys.argv) > 1 else '.')
    req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                                 headers={'content-type': 'application/json; charset=utf-8'})
    with urllib.request.urlopen(req, timeout=20) as res:
        print(f"indexnow: {res.status} for {len(payload['urlList'])} URLs on {payload['host']}")


if __name__ == '__main__':
    main()
