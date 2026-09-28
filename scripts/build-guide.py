#!/usr/bin/env python3
"""Build a wagyu guide page from a draft (markdown) and assets/guide-template.html.

Usage:
  build-guide.py DRAFT.md OUT.html --lang en|id --cta-url URL
                 [--brand "#1f4fd1" --brand-ink "#ffffff"] [--banner TEXT] [--docs]

--docs writes plain HTML for Google Docs import instead of the page: no template, buttons, or script,
and screenshots become "[Insert image: ...]" markers.

Needs pandoc on PATH (or the PANDOC environment variable). Draft conventions are in commands/draft.md.
Exits 1 if any template placeholder, CTA_URL, or [NEEDS SOURCE] marker is left in the page.
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "guide-template.html"
LABELS = {
    "en": {"expect": "You should see:", "pitfall": "Watch out:", "verify": "Not yet verified:",
           "copy": "Copy", "toc": "Contents", "shot": "Screenshot needed:", "insert": "Insert image:"},
    "id": {"expect": "Hasil yang benar:", "pitfall": "Hati-hati:", "verify": "Belum diverifikasi:",
           "copy": "Salin", "toc": "Daftar isi", "shot": "Screenshot dibutuhkan:", "insert": "Sisipkan gambar:"},
}
IMAGE = re.compile(r"\.(png|jpe?g|webp|gif|svg)$|^https?://", re.I)


def pandoc(md):
    exe = os.environ.get("PANDOC") or shutil.which("pandoc")
    if not exe:
        sys.exit("pandoc not found: install it or set PANDOC to its path")
    return subprocess.run([exe, "-f", "gfm", "-t", "html5", "--wrap=none"], input=md,
                          capture_output=True, text=True, encoding="utf-8", check=True).stdout


def inline(md):
    return re.sub(r"^<p>|</p>$", "", pandoc(md).strip())


def split_hero(md):
    """Eyebrow line, '# Title', subtitle paragraph, chips paragraph ('a · b · c'), then the intro."""
    intro, sep, body = md.partition("\n## ")
    blocks = [b.strip() for b in re.split(r"\n\s*\n", intro.strip()) if b.strip()]
    t = next(i for i, b in enumerate(blocks) if b.startswith("# "))
    eyebrow = blocks[t - 1] if t else ""
    title, subtitle, chips = blocks[t][2:].strip(), blocks[t + 1], blocks[t + 2]
    return eyebrow, title, subtitle, [c.strip() for c in chips.split("·")], "\n\n".join(blocks[t + 3:]), sep + body


def details(h):
    """After <!-- wg:details -->, each paragraph that starts in bold opens a collapsible item."""
    while "<!-- wg:details -->" in h:
        start = h.index("<!-- wg:details -->")
        rest = h[start + len("<!-- wg:details -->"):]
        stops = [i for i in (rest.find("<h2"), rest.find("<!-- wg:")) if i >= 0]
        end = min(stops) if stops else len(rest)
        chunks = re.split(r"(?=<p><strong>)", rest[:end])
        out = [chunks[0]]
        for c in chunks[1:]:
            m = re.match(r"<p><strong>(.*?)</strong>\s*(.*)", c, flags=re.S)
            body = m[2][4:] if m[2].startswith("</p>") else "<p>" + m[2]
            out.append(f"<details><summary>{m[1]}</summary>{body.strip()}</details>\n")
        h = h[:start] + "".join(out) + rest[end:]
    return h


def transform(h, L):
    h = h.replace(f"<p><strong>{L['expect']}</strong>", f'<p class="wg-expect"><strong>{L["expect"]}</strong>')
    h = re.sub(rf"<blockquote>\s*<p><strong>{re.escape(L['pitfall'])}</strong>(.*?)</p>\s*</blockquote>",
               lambda m: f'<p class="wg-pitfall"><strong>{L["pitfall"]}</strong>{m[1]}</p>', h, flags=re.S)
    h = re.sub(r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>", r'<p class="wg-aside">\1</p>', h, flags=re.S)
    h = h.replace("[VERIFY]", f"<strong>{L['verify']}</strong>")

    def shot(m):
        s = html.unescape(m[1])
        if IMAGE.search(s):
            return f'<figure class="wg-shot"><img src="{html.escape(s)}" alt="{html.escape(Path(s).stem.replace("-", " "))}" loading="lazy"></figure>'
        return f'<div class="wg-shot-todo">{L["shot"]} {m[1]}</div>'
    h = re.sub(r"<p>\[SCREENSHOT: (.*?)\]</p>", shot, h)

    h = re.sub(r'<pre(?: [^>]*)?><code(?: [^>]*)?>',
               f'<div class="wg-code"><button class="wg-copy" type="button">{L["copy"]}</button><pre><code>', h)
    h = h.replace("</code></pre>", "</code></pre></div>")

    h = re.sub(r'<li>(?:<label>)?<input type="checkbox" (?:\w+="" )*/>\s*(.*?)(?:</label>)?</li>',
               r'<li><label><input type="checkbox"> \1</label></li>', h, flags=re.S)
    h = re.sub(r'<ul(?: class="task-list")?>(\s*<li><label><input type="checkbox">)', r'<ul class="wg-check">\1', h)
    h = re.sub(r'(<p><strong>[^<]*</strong></p>\s*<ul class="wg-check">.*?</ul>)',
               r'<div class="wg-box">\1</div>', h, flags=re.S)

    h = (h.replace("<!-- wg:box -->", '<div class="wg-box">').replace("<!-- /wg:box -->", "</div>")
          .replace("<!-- wg:cols -->", '<div class="wg-cols"><div class="wg-box">')
          .replace("<!-- wg:col -->", '</div><div class="wg-box">')
          .replace("<!-- /wg:cols -->", "</div></div>"))
    return details(h)


def closing(h):
    """<!-- wg:cta --> starts the premium block; a lone link becomes the button, the paragraph before it the not-for line.
    A final horizontal rule separates the footer."""
    foot = ""
    if "<hr />" in h:
        h, _, foot = h.rpartition("<hr />")
        foot = foot.replace("<p>", '<p class="wg-foot">')
    if "<!-- wg:cta -->" in h:
        before, _, cta = h.partition("<!-- wg:cta -->")
        cta = re.sub(r'(<p>)((?:(?!<p>).)*?</p>\s*)<p><a href="([^"]+)">(.*?)</a></p>',
                     r'<p class="wg-notfor">\2<a class="wg-btn" href="\3">\4</a>', cta, flags=re.S)
        h = f'{before}<section class="wg-cta">{cta}</section>'
    return h + foot


def docs_html(md, L, banner, title):
    """Plain HTML that Google Docs imports cleanly: headings, lists, tables, code, links."""
    md = re.sub(r"^<!-- /?wg:[a-z]+ -->\n?", "", md, flags=re.M)
    md = md.replace("[VERIFY]", f"**{L['verify']}**")
    md = re.sub(r"\n(Cause|Fix|Penyebab|Solusi):", r"  \n**\1:**", md)  # own line in Docs
    md = re.sub(r"\[SCREENSHOT: (.*?)\]",
                lambda m: f"*[{L['insert'] if IMAGE.search(m[1]) else L['shot']} {m[1]}]*", md)
    if banner:
        md = f"**{banner}**\n\n{md}"
    body = re.sub(r'<li><label><input type="checkbox" (?:\w+="" )*/>(.*?)</label></li>',
                  lambda m: f"<li>☐ {m[1]}</li>", pandoc(md), flags=re.S)
    body = body.replace('<ul class="task-list">', "<ul>")  # Docs drops form inputs; keep a visible box
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title></head>'
            f"<body>{body}</body></html>")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft")
    ap.add_argument("out")
    ap.add_argument("--lang", choices=LABELS, required=True)
    ap.add_argument("--cta-url", required=True)
    ap.add_argument("--brand")
    ap.add_argument("--brand-ink")
    ap.add_argument("--banner")
    ap.add_argument("--docs", action="store_true")
    a = ap.parse_args()
    L = LABELS[a.lang]

    md = Path(a.draft).read_text(encoding="utf-8").replace("\r\n", "\n")
    if md.startswith("Status:"):
        md = md.split("\n", 1)[1]
    md = md.replace("CTA_URL", a.cta_url)
    if a.docs:
        title = next((l[2:].strip() for l in md.splitlines() if l.startswith("# ")), "Guide")
        page = docs_html(md, L, a.banner, html.escape(title))
        Path(a.out).write_text(page, encoding="utf-8")
        left = {k: page.count(k) for k in ("CTA_URL", "[NEEDS SOURCE]") if page.count(k)}
        print(f"{a.out}: {len(page)} bytes, {page.count(L['insert'])} images to insert, {page.count(L['shot'])} screenshots still needed")
        if left:
            sys.exit(f"Not ready, left in document: {left}")
        return
    eyebrow, title, subtitle, chips, intro, body = split_hero(md)

    body_html = closing(transform(pandoc(body), L))
    cta_at = body_html.find('<section class="wg-cta">')
    toc_src = body_html if cta_at < 0 else body_html[:cta_at]
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', toc_src))

    top = ""
    if a.banner:
        top += f'<p class="wg-pitfall"><strong>{html.escape(a.banner)}</strong></p>\n'
    if eyebrow:
        top += f'<p class="wg-eyebrow">{inline(eyebrow)}</p>\n'
    top += f"<h1>{inline(title)}</h1>\n<p class=\"wg-sub\">{inline(subtitle)}</p>\n"
    top += '<ul class="wg-chips">' + "".join(f"<li>{inline(c)}</li>" for c in chips) + "</ul>\n"
    top += transform(pandoc(intro), L) if intro else ""
    top += f'<nav class="wg-box wg-toc" aria-label="{L["toc"]}"><strong>{L["toc"]}</strong><ol>{toc}</ol></nav>\n'

    tpl = TEMPLATE.read_text(encoding="utf-8").replace("\r\n", "\n")
    tpl = re.sub(r"<!--\s*WAGYU guide page template.*?-->\n", "", tpl, flags=re.S)
    open_tag = '<div class="wg-guide">'
    start, end = tpl.index(open_tag) + len(open_tag), tpl.index("</div>\n<script>")
    page = tpl[:start] + "\n" + top + body_html + tpl[end:]
    plain_title = html.escape(re.sub(r"<[^>]+>", "", html.unescape(inline(title))))
    page = page.replace('<html lang="id">', f'<html lang="{a.lang}">').replace("<title>{{TITLE}}</title>", f"<title>{plain_title}</title>")
    if a.brand:
        page = page.replace("--wg-brand:#1f4fd1", f"--wg-brand:{a.brand}", 1)
    if a.brand_ink:
        page = page.replace("--wg-brand-ink:#ffffff", f"--wg-brand-ink:{a.brand_ink}", 1)

    Path(a.out).write_text(page, encoding="utf-8")
    problems = {k: page.count(k) for k in ("{{", "CTA_URL", "[NEEDS SOURCE]", "[SCREENSHOT")}
    print(f"{a.out}: {len(re.findall(r'<h3', page))} steps, {page.count('class="wg-copy"')} copy blocks, "
          f"{page.count('<details>')} troubleshooting items, {page.count('class="wg-shot-todo"')} screenshots still needed")
    left = {k: v for k, v in problems.items() if v}
    if left:
        sys.exit(f"Not ready, left in page: {left}")


if __name__ == "__main__":
    main()
