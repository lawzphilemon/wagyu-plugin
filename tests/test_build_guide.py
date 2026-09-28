"""Smoke test for scripts/build-guide.py. Run: python tests/test_build_guide.py (needs pandoc)."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "build-guide.py"
DRAFT = """Status: confirmed

Free Guide · Test

# Do a **thing** in 10 minutes

A subtitle for testing.

10 min · Beginner · Tool cost: $0

<!-- wg:box -->
**You'll have:** a thing.
<!-- /wg:box -->

<!-- wg:cols -->
**For:** people.
<!-- wg:col -->
**Not for:** robots.
<!-- /wg:cols -->

## Phase 1: Start

### Step 1.1 — Open the app

1. Click **Open**.

**You should see:** the app.

> **Watch out:** [VERIFY] it may differ.

[SCREENSHOT: screenshots/step-1.1.png]

[SCREENSHOT: the settings page]

```text
copy <me> & keep
```

**Checkpoint**

- [ ] App open

> A soft aside. [Learn more](CTA_URL)

## Troubleshooting

<!-- wg:details -->

**T1. It breaks**
Cause: reasons. Fix: do this.

**T2. Still breaks**

Second paragraph body.

<!-- wg:cta -->
## What's next

Wall and bridge.

Not for premium if small.

[Talk to us](CTA_URL)

---

Checked on a date.
"""


def main():
    if not shutil.which("pandoc"):
        print("SKIP: pandoc not installed")
        return
    with tempfile.TemporaryDirectory() as d:
        draft, out = Path(d, "04-draft.md"), Path(d, "guide.html")
        draft.write_text(DRAFT, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), str(draft), str(out), "--lang", "en",
                            "--cta-url", "https://example.com/cta", "--banner", "TEST"], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr + r.stdout
        page = out.read_text(encoding="utf-8")
    for needle in ['<html lang="en">', "<title>Do a thing in 10 minutes</title>", '<p class="wg-eyebrow">',
                   '<ul class="wg-chips"><li>10 min</li>', 'class="wg-cols"', 'class="wg-expect"', 'class="wg-pitfall"',
                   "Not yet verified:", '<img src="screenshots/step-1.1.png"', "Screenshot needed: the settings page",
                   "copy &lt;me&gt; &amp; keep", 'class="wg-copy"', 'class="wg-check"', 'class="wg-aside"',
                   "<summary>T1. It breaks</summary>", "<summary>T2. Still breaks</summary>", "Second paragraph body",
                   '<section class="wg-cta">', '<p class="wg-notfor">', 'class="wg-btn" href="https://example.com/cta"',
                   '<p class="wg-foot">', 'href="#phase-1-start"']:
        assert needle in page, f"missing: {needle}"
    assert "{{" not in page and "CTA_URL" not in page and "What's next</a>" not in page

    with tempfile.TemporaryDirectory() as d:
        draft, out = Path(d, "04-draft.md"), Path(d, "guide.docs.html")
        draft.write_text(DRAFT, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), str(draft), str(out), "--lang", "en",
                            "--cta-url", "https://example.com/cta", "--docs"], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr + r.stdout
        doc = out.read_text(encoding="utf-8")
    for needle in ["<title>Do a **thing** in 10 minutes</title>", "Insert image: screenshots/step-1.1.png",
                   "Screenshot needed: the settings page", "☐ App open", "Not yet verified:",
                   'href="https://example.com/cta"', "copy &lt;me&gt; &amp; keep"]:
        assert needle in doc, f"docs missing: {needle}"
    assert "<!-- wg:" not in doc and "<script" not in doc and "wg-copy" not in doc

    with tempfile.TemporaryDirectory() as d:
        draft, out = Path(d, "04-draft.md"), Path(d, "guide.snippet.html")
        draft.write_text(DRAFT, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), str(draft), str(out), "--lang", "en",
                            "--cta-url", "https://example.com/cta", "--snippet",
                            "--img-base", "https://site.test/wp-content/uploads/2026/09/"], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr + r.stdout
        snip = out.read_text(encoding="utf-8")
    assert snip.startswith("<!-- Do a thing in 10 minutes: paste into a Custom HTML block.")
    for needle in ["<style>", '<div class="wg-guide">', "<script>", 'class="wg-btn" href="https://example.com/cta"',
                   '<img src="https://site.test/wp-content/uploads/2026/09/step-1.1.png"']:
        assert needle in snip, f"snippet missing: {needle}"
    for banned in ["<html", "<head", "<body", "</body>", "<title>", "{{"]:
        assert banned not in snip, f"snippet has: {banned}"
    print("OK")


if __name__ == "__main__":
    main()
