#!/usr/bin/env python3
"""Send a --post build to WordPress as a draft. Never publishes: the status is always "draft".

Usage:
  wp-draft.py POST.html --site https://example.com/guides --title "Guide title"
              [--more-before "Step 1.2"] [--category slug ...] [--lang en] [--translation-of 123]

POST.html is the output of build-guide.py --post. --more-before puts a More tag before the first heading that
contains the text, so a gate that honors it shows everything above as the public teaser. --category takes
existing category slugs (a missing slug stops the run; nothing is created).
--lang sets the Polylang language (slug such as en or id) on a site that runs Polylang; without it Polylang files the
draft under the site's default language. --translation-of links the new draft to an existing post in another language.
Auth: WP_GUIDES_AUTH = base64 of "username:application password" (WordPress Users > Profile > Application Passwords).
Prints the draft's edit and preview links. The post lands as Classic blocks around a More block, with the callouts as Custom HTML blocks. It renders as is;
"Convert to blocks" on each Classic block is optional.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


def post_body(page):
    """The --post file is a whole HTML page; WordPress only wants what is inside <body>."""
    m = re.search(r"<body[^>]*>(.*)</body>", page, flags=re.S)
    return (m[1] if m else page).strip()


def add_more(body, before):
    """Insert a More block before the first <h2>-<h4> whose text contains `before`.
    A bare <!--more--> would be dropped by the editor's "Convert to blocks"; as its own block it survives."""
    for m in re.finditer(r"<h[2-4][^>]*>(.*?)</h[2-4]>", body, flags=re.S):
        if before.lower() in re.sub(r"<[^>]+>", "", m[1]).lower():
            return f"{body[:m.start()]}<!-- wp:more -->\n<!--more-->\n<!-- /wp:more -->\n{body[m.start():]}"
    sys.exit(f'--more-before: no heading contains "{before}"')


def api(site, path, auth, data=None):
    req = urllib.request.Request(f"{site.rstrip('/')}/wp-json/wp/v2/{path}",
                                 data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"WordPress said {e.code}: {e.read().decode(errors='replace')[:300]}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("post_html")
    p.add_argument("--site", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--more-before")
    p.add_argument("--category", action="append", default=[])
    p.add_argument("--lang", help="Polylang language slug, e.g. en or id")
    p.add_argument("--translation-of", type=int, help="ID of the same guide in another language (needs --lang)")
    a = p.parse_args()
    if a.translation_of and not a.lang:
        sys.exit("--translation-of needs --lang")
    auth = os.environ.get("WP_GUIDES_AUTH")
    if not auth:
        sys.exit("WP_GUIDES_AUTH is not set")

    body = post_body(Path(a.post_html).read_text(encoding="utf-8"))
    if a.more_before:
        body = add_more(body, a.more_before)
    cats = []
    for slug in a.category:
        found = api(a.site, f"categories?slug={urllib.parse.quote(slug)}", auth)
        if not found:
            sys.exit(f"category not found: {slug}")
        cats.append(found[0]["id"])

    data = {"title": a.title, "content": body, "status": "draft", "categories": cats}
    if a.lang:
        data["lang"] = a.lang
    post = api(a.site, "posts", auth, data)
    assert post["status"] == "draft", post["status"]
    if a.lang and post.get("lang") != a.lang:
        print(f"warning: language not set (site answered lang={post.get('lang')!r}); is Polylang active?", file=sys.stderr)
    if a.translation_of:
        other = api(a.site, f"posts/{a.translation_of}?context=edit&_fields=lang,translations", auth)
        links = {**(other.get("translations") or {}), other["lang"]: a.translation_of, a.lang: post["id"]}
        api(a.site, f"posts/{post['id']}", auth, {"translations": links})
        print(f"linked as {a.lang} translation of {a.translation_of}")
    print(f"draft {post['id']}")
    print(f"edit: {a.site.rstrip('/')}/wp-admin/post.php?post={post['id']}&action=edit")
    print(f"preview: {a.site.rstrip('/')}/?p={post['id']}&preview=true")


if __name__ == "__main__":
    main()
