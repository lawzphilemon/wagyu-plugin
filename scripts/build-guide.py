#!/usr/bin/env python3
"""Build a wagyu guide page from a draft (markdown) and assets/guide-template.html.

Usage:
  build-guide.py DRAFT.md OUT.html --lang en|id --cta-url URL
                 [--brand "#1f4fd1" --brand-ink "#ffffff"] [--banner TEXT] [--img-base URL] [--review FILE]
                 [--docs | --post | --snippet | --wordpress]

--docs writes plain HTML for Google Docs import instead of the page: no template, buttons, or script,
and screenshots become "[Insert image: ...]" markers (real images with --img-base). --review FILE puts a Markdown
reviewer brief above it.
--post writes the same plain HTML for a WordPress post: open it in a browser, copy all, and paste into the block
editor (headings, lists, tables, and images become blocks). The post title is the H1, so the eyebrow, title, and
chips are left out and the subtitle opens the post. Use --img-base so screenshots become images.
--snippet writes paste-ready HTML code (<style> + guide + <script>, no <html>/<head>) for a
WordPress Custom HTML block or a page builder. The host page must be set to noindex itself.
--wordpress writes one block with every style inlined and no <style>, <script>, copy buttons, or H1, for
sites that strip those tags on save (the leftover CSS then shows as text). Needs premailer (pip install premailer).
Screenshots: "[SCREENSHOT: path-or-URL | alt text]"; the alt text is optional.
--img-base rewrites local screenshot paths to URL + file name, e.g. your media library folder.
--theme appends a brand theme (assets/themes/*.css) to the page CSS; a "font-url:" line in it adds the
font stylesheet to full pages.

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
           "copy": "Copy", "toc": "Contents", "next": "Next step", "shot": "Screenshot needed:", "insert": "Insert image:"},
    "id": {"expect": "Hasil yang benar:", "pitfall": "Hati-hati:", "verify": "Belum diverifikasi:",
           "copy": "Salin", "toc": "Daftar isi", "next": "Langkah berikutnya", "shot": "Screenshot dibutuhkan:", "insert": "Sisipkan gambar:"},
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
        # pandoc autolinks a bare URL; take the link text back. "path | alt text" sets the alt text.
        s = html.unescape(re.sub(r"<a [^>]*>(.*?)</a>", r"\1", m[1]))
        src, _, alt = (p.strip() for p in s.partition(" | "))
        if IMAGE.search(src):
            alt = alt or Path(src).stem.replace("-", " ")
            return f'<figure class="wg-shot"><img src="{html.escape(src)}" alt="{html.escape(alt)}" loading="lazy"></figure>'
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


def wordpress(page, title):
    """One block for hosts that strip <style> and <script> on save: every rule inlined as style="".
    Drops the H1 (the post title already is one), the copy buttons, and the script."""
    try:
        from premailer import Premailer
    except ImportError:
        sys.exit("--wordpress needs premailer: python -m pip install premailer")
    css = "\n".join(re.findall(r"<style>(.*?)</style>", page, flags=re.S))
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"rgb\(\s*(\d+)\s+(\d+)\s+(\d+)\s*/\s*([\d.]+)\s*\)", r"rgba(\1,\2,\3,\4)", css)  # premailer drops this syntax
    tokens = {}  # later .wg-guide blocks (the theme) override earlier ones
    for block in re.findall(r"\.wg-guide\s*\{([^}]*)\}", css):
        tokens.update((k, v.strip()) for k, v in re.findall(r"(--wg-[\w-]+)\s*:\s*([^;}]+)", block))
    css = re.sub(r"--wg-[\w-]+\s*:\s*[^;}]+;?", "", css)
    var = re.compile(r"var\((--wg-[\w-]+)(?:,([^()]*(?:\([^()]*\)[^()]*)*))?\)")
    for _ in range(5):
        css = var.sub(lambda m: tokens.get(m[1], (m[2] or "").strip()), css)
    # Media queries can't be inlined: let the two columns wrap on their own.
    css = css.replace(".wg-cols{display:grid;grid-template-columns:1fr 1fr", ".wg-cols{display:flex;flex-wrap:wrap")
    css += "\n.wg-cols .wg-box{flex:1 1 260px}\n.wg-guide p.wg-foot{margin:3em 0 0}\n"
    guide = page[page.index('<div class="wg-guide">'):page.index("</body>")]
    guide = re.sub(r"<script>.*?</script>", "", guide, flags=re.S)
    guide = re.sub(r'<button class="wg-copy"[^>]*>.*?</button>', "", guide, flags=re.S)
    guide = re.sub(r"<h1>.*?</h1>\s*", "", guide, count=1, flags=re.S)
    guide = re.sub(r'<div class="wg-shot-todo">.*?</div>\s*', "", guide, flags=re.S)  # a live page shows no gaps
    doc = Premailer(f"<html><head><style>{css}</style></head><body>{guide}</body></html>", keep_style_tags=False,
                    disable_validation=True, cssutils_logging_level=50, allow_network=False).transform()
    body = re.search(r"<body>(.*)</body>", doc, flags=re.S)[1].strip()
    return (f"<!-- {title}: paste into one Custom HTML block. No separate CSS or script needed; the post title is the H1. "
            f"Set this page to noindex. -->\n{body}\n")


def docs_html(md, L, banner, title, review=None, img_base=None):
    """Plain HTML that Google Docs and the WordPress block editor import cleanly: headings, lists, tables, code, links."""
    md = re.sub(r"^<!-- /?wg:[a-z]+ -->$", "", md, flags=re.M)  # keep the line empty, so a list above it ends
    if review:  # reviewer brief above the guide, cut off by a rule
        md = f"{review.strip()}\n\n---\n\n{md}"
    md = md.replace("[VERIFY]", f"**{L['verify']}**")
    md = re.sub(r"\n(Cause|Fix|Penyebab|Solusi):", r"  \n**\1:**", md)  # own line in Docs

    def shot(m):
        src, _, alt = (p.strip() for p in m[1].partition(" | "))
        if IMAGE.search(src) and (img_base or src.startswith("http")):  # an image someone can fetch
            url = src if src.startswith("http") else img_base.rstrip("/") + "/" + Path(src).name
            return f"![{alt or Path(src).stem}]({url})"
        return f"*[{L['insert'] if IMAGE.search(src) else L['shot']} {m[1]}]*"
    md = re.sub(r"\[SCREENSHOT: (.*?)\]", shot, md)
    if banner:
        md = f"**{banner}**\n\n{md}"
    body = re.sub(r'<li><label><input type="checkbox" (?:\w+="" )*/>(.*?)</label></li>',
                  lambda m: f"<li>☐ {m[1]}</li>", pandoc(md), flags=re.S)
    body = body.replace('<ul class="task-list">', "<ul>")  # Docs drops form inputs; keep a visible box
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title></head>'
            f"<body>{body}</body></html>")


CTA_MARK = "WGCTAMARK"  # stands in for <!-- wg:cta --> through docs_html, which drops the wg markers


def theme_tokens(theme=None):
    """--wg-* tokens from the template, overridden by the theme file."""
    css = TEMPLATE.read_text(encoding="utf-8") + (Path(theme).read_text(encoding="utf-8") if theme else "")
    tokens = {}
    for block in re.findall(r"\.wg-guide\s*\{([^}]*)\}", css):
        tokens.update((k[5:], v.strip()) for k, v in re.findall(r"(--wg-[\w-]+)\s*:\s*([^;}]+)", block))
    return tokens


def post_callouts(body, L, theme=None):
    """--post: each expected result, pitfall, ladder aside, and the closing CTA becomes its own Custom HTML block
    with inline styles. The block editor keeps them as they are (wp-draft.py, or a paste into the Code editor);
    a visual paste would strip the styles."""
    t = theme_tokens(theme)
    ink, brand, brand_ink = t.get("ink", "#16181d"), t.get("brand", "#1f4fd1"), t.get("brand-ink", "#ffffff")
    line, soft, radius = t.get("line", "#e2e5ec"), t.get("soft", "#f4f6fa"), t.get("radius", "12px")
    cta_bg, cta_ink = t.get("cta-bg", brand), t.get("cta-ink", brand_ink)
    btn_bg, btn_ink = t.get("btn-bg", brand_ink), t.get("btn-ink", brand)
    font = "font-family:inherit"

    def block(h):
        return f"<!-- wp:html -->\n{h}\n<!-- /wp:html -->"

    def note(label, text, box, badge, glyph):
        text = text.strip()
        text = text[:1].upper() + text[1:]  # the label now stands on its own line, so the text starts a sentence
        return block(
            f'<div role="note" style="display:flex;gap:14px;align-items:flex-start;{box};border-radius:{radius};'
            f'padding:16px 18px;margin:1.4em 0;{font};color:{ink}">'
            f'<span aria-hidden="true" style="flex:none;width:28px;height:28px;border-radius:50%;{badge};'
            f'font-weight:800;font-size:15px;line-height:28px;text-align:center">{glyph}</span>'
            f'<div style="min-width:0"><p style="margin:0 0 2px;font-size:12px;font-weight:800;letter-spacing:.08em;'
            f'text-transform:uppercase">{label.rstrip(":")}</p>'
            f'<p style="margin:0;font-size:16px;line-height:1.6">{text.strip()}</p></div></div>')

    pill = (f"display:inline-block;background:{brand};color:{brand_ink};font-weight:700;text-decoration:none;"
            f"border-radius:999px;padding:4px 14px")
    body = re.sub(rf"<p><strong>{re.escape(L['expect'])}</strong>(.*?)</p>",
                  lambda m: note(L["expect"], m[1], f"background:{soft};border:1px solid {line};border-left:4px solid {ink}",
                                 f"background:{brand};color:{brand_ink}", "&#10003;"), body, flags=re.S)
    body = re.sub(rf"<blockquote>\s*<p><strong>{re.escape(L['pitfall'])}</strong>(.*?)</p>\s*</blockquote>",
                  lambda m: note(L["pitfall"], m[1], f"background:{t.get('warn-bg', '#fff7e6')};border:1px solid {brand}",
                                 f"background:{ink};color:{brand}", "!"), body, flags=re.S)
    body = re.sub(r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>", lambda m: block(
        f'<div style="border:2px solid {ink};border-radius:{radius};padding:16px 18px;margin:1.6em 0;{font};color:{ink}">'
        f'<p style="margin:0;font-size:16px;line-height:1.7">'
        + m[1].replace("<a ", f'<a style="{pill}" ') + "</p></div>"), body, flags=re.S)

    if f"<p>{CTA_MARK}</p>" in body:
        before, _, cta = body.partition(f"<p>{CTA_MARK}</p>")
        foot = ""
        if "<hr />" in cta:
            cta, _, foot = cta.rpartition("<hr />")
            foot = "<hr />" + foot
        btn = ""
        m = re.search(r'<p><a href="([^"]+)">(.*?)</a></p>\s*$', cta.strip(), flags=re.S)
        if m:  # a lone link at the end is the button, the paragraph before it the not-for line
            btn = (f'<a href="{m[1]}" style="display:inline-block;background:{btn_bg};color:{btn_ink};font-weight:700;'
                   f'font-size:16px;text-decoration:none;border-radius:999px;padding:13px 24px;margin-top:8px">{m[2]}</a>')
            cta = cta.strip()[:m.start()]
            paras = re.findall(r"<p>.*?</p>", cta, flags=re.S)
            if len(paras) > 1:
                cta = cta.replace(paras[-1], paras[-1].replace(
                    "<p>", f'<p style="margin:0 0 12px;font-size:14px;line-height:1.55;opacity:.8">', 1), 1)
        cta = re.sub(r"<h2([^>]*)>", rf'<h2\1 style="margin:0 0 10px;font-size:24px;line-height:1.3;color:{cta_ink};border:0;padding:0">', cta)
        cta = re.sub(r"<p>", '<p style="margin:0 0 10px;font-size:16px;line-height:1.6">', cta)
        cta = cta.replace("<a href", f'<a style="color:{cta_ink}" href')
        tag = (f'<p style="display:inline-block;margin:0 0 12px;background:{brand};color:{brand_ink};border-radius:999px;'
               f'padding:3px 12px;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase">{L["next"]}</p>')
        body = before + block(f'<div style="background:{cta_bg};color:{cta_ink};border-radius:{radius};padding:28px 24px;'
                              f'margin:2.4em 0;{font}">{tag}{cta.strip()}{btn}</div>') + "\n" + foot
    return body


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft")
    ap.add_argument("out")
    ap.add_argument("--lang", choices=LABELS, required=True)
    ap.add_argument("--cta-url", required=True)
    ap.add_argument("--brand")
    ap.add_argument("--brand-ink")
    ap.add_argument("--banner")
    ap.add_argument("--img-base")
    ap.add_argument("--theme", help="CSS file with .wg-guide token overrides, e.g. assets/themes/gwenchana.css")
    ap.add_argument("--review", help="--docs only: Markdown reviewer brief placed above the guide")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--docs", action="store_true")
    mode.add_argument("--snippet", action="store_true")
    mode.add_argument("--wordpress", action="store_true")
    mode.add_argument("--post", action="store_true")
    a = ap.parse_args()
    L = LABELS[a.lang]

    md = Path(a.draft).read_text(encoding="utf-8").replace("\r\n", "\n")
    if md.startswith("Status:"):
        md = md.split("\n", 1)[1]
    md = md.replace("CTA_URL", a.cta_url)
    if a.docs or a.post:
        title = next((l[2:].strip() for l in md.splitlines() if l.startswith("# ")), "Guide")
        review = Path(a.review).read_text(encoding="utf-8") if a.review and a.docs else None
        if a.post:  # the post title is the H1: drop eyebrow, title, and chips; the subtitle opens the post
            _, _, subtitle, _, intro, body = split_hero(md)
            md = "\n\n".join(p for p in (subtitle, intro) if p) + "\n" + body
            md = md.replace("<!-- wg:cta -->", f"{CTA_MARK}\n")
        page = docs_html(md, L, a.banner, html.escape(title), review, a.img_base)
        if a.post:
            head, _, rest = page.partition("<body>")
            page = head + "<body>" + post_callouts(rest, L, a.theme)
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
    if a.theme:
        css = Path(a.theme).read_text(encoding="utf-8")
        page = page.replace("</style>", css.rstrip() + "\n</style>", 1)
        font = re.search(r"font-url:\s*(\S+)", css)
        if font and not (a.snippet or a.wordpress):  # pasted code uses the host site's fonts
            page = page.replace("<style>", f'<link rel="stylesheet" href="{html.escape(font[1])}">\n<style>', 1)
    if a.img_base:
        base = a.img_base.rstrip("/") + "/"
        page = re.sub(r'<img src="(?!https?://)([^"]+)"', lambda m: f'<img src="{base}{Path(m[1]).name}"', page)
    if a.snippet:
        style = re.search(r"<style>.*?</style>", page, flags=re.S)[0]
        guide = page[page.index('<div class="wg-guide">'):page.index("</body>")].rstrip()
        page = f"<!-- {plain_title}: paste into a Custom HTML block. Set this page to noindex. -->\n{style}\n{guide}\n"
    todo = page.count('class="wg-shot-todo"')
    if a.wordpress:
        page = wordpress(page, plain_title)

    Path(a.out).write_text(page, encoding="utf-8")
    problems = {k: page.count(k) for k in ("{{", "CTA_URL", "[NEEDS SOURCE]", "[SCREENSHOT")}
    if a.wordpress:
        problems.update({k: page.count(k) for k in ("var(--", "<style", "<script")})
    print(f"{a.out}: {len(re.findall(r'<h3', page))} steps, {page.count('class="wg-copy"')} copy blocks, "
          f"{page.count('<details')} troubleshooting items, {todo} screenshots still needed{' (left out of the page)' if a.wordpress and todo else ''}")
    left = {k: v for k, v in problems.items() if v}
    if left:
        sys.exit(f"Not ready, left in page: {left}")


if __name__ == "__main__":
    main()
