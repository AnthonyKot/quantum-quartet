#!/usr/bin/env python3
"""Per-chapter checks from notes/REWORK-PLAN.md section 10 that a machine can do.

    python3 scripts/check_page.py chapters/01-blackbody-planck.html

Checks: banned phrases; KaTeX errors; display equations wider than the text column
(which would show a horizontal scrollbar) at desktop and phone width; page-level
horizontal overflow; figure labels at least 10 px tall at phone width; and that a
printed PDF contains the text of every closed optional section and worked answer
(needs pdftotext). Needs a headless Chromium (Playwright's cache is searched).
"""
import glob, http.server, os, re, subprocess, sys, threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANNED = ["the four authors", "our four", "four books", "the course", "entry points",
          "obviously", "simply", "of course", "relativistic mass"]
PROBE = """<script>window.addEventListener('load',()=>setTimeout(()=>{
const out=[];document.querySelectorAll('.katex-display').forEach((d,i)=>{
 if(d.scrollWidth>d.clientWidth+1)out.push('WIDE eq '+i+': '+d.scrollWidth+'>'+d.clientWidth+' '+d.textContent.slice(0,40));});
out.push('katex-errors='+document.querySelectorAll('.katex-error').length);
out.push('page-overflow='+(document.documentElement.scrollWidth>innerWidth));
let minLabel=99;document.querySelectorAll('.fig-svg text').forEach(t=>{const h=t.getBoundingClientRect().height;if(h>0)minLabel=Math.min(minLabel,h);});
out.push('min-label-px='+(minLabel===99?'none':minLabel.toFixed(1)));
const pre=document.createElement('pre');pre.id='probe';pre.textContent=out.join('\\n');
document.body.appendChild(pre);},1500));</script></body>"""


def chromium():
    hits = sorted(glob.glob(os.path.expanduser("~/.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell")))
    if not hits:
        sys.exit("no headless Chromium found")
    return hits[-1]


def main(rel):
    page = ROOT / rel
    src = page.read_text(encoding="utf-8")
    ok = True
    prose = re.sub(r'<div class="read-originals">.*?</div>', " ", src, flags=re.S)  # book titles may quote
    low = re.sub(r"<[^>]+>", " ", prose).lower()
    for w in BANNED:
        if w in low:
            print(f"BANNED phrase: {w!r}"); ok = False
    if "entry-table" in src:
        print("leftover entry-points table"); ok = False
    probe = page.with_name("_probe.html")
    probe.write_text(src.replace("</body>", PROBE), encoding="utf-8")
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=str(ROOT), **k)
    http.server.SimpleHTTPRequestHandler.log_message = lambda *a: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        url = f"http://127.0.0.1:{srv.server_address[1]}/{probe.relative_to(ROOT)}"
        for width in (1200, 390):
            dom = subprocess.run([chromium(), "--no-sandbox", "--disable-gpu", "--virtual-time-budget=9000",
                                  f"--window-size={width},900", "--dump-dom", url],
                                 capture_output=True, text=True).stdout
            m = re.search(r'<pre id="probe">(.*?)</pre>', dom, re.S)
            res = m.group(1).strip() if m else "probe did not run"
            print(f"width {width}: " + res.replace("\n", " | "))
            if "WIDE" in res or "katex-errors=0" not in res or "page-overflow=false" not in res:
                ok = False
            m2 = re.search(r"min-label-px=([\d.]+)", res)
            if m2 and float(m2.group(1)) < 10:
                print(f"  figure labels too small at width {width}"); ok = False
        # print: every <details> body must reach the PDF
        pdf = page.with_name("_probe.pdf")
        subprocess.run([chromium(), "--no-sandbox", "--disable-gpu", "--virtual-time-budget=9000",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf}", url.replace("_probe.html", page.name)],
                       capture_output=True)
        text = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
        pdf.unlink(missing_ok=True)
        letters = lambda t: re.sub(r"[^a-z]", "", t.lower())
        pdf_letters = letters(text)
        missing = 0
        for body in re.findall(r"<details>.*?</summary>(.*?)</details>", src, re.S):
            prose = re.sub(r"<[^>]+>", " ", body)
            prose = re.sub(r"&[a-z]+;", " ", prose)
            # longest stretch of the fold-out that contains no maths
            chunks = re.split(r"\$\$.*?\$\$|\$[^$]*\$", prose, flags=re.S)
            chunk = letters(max(chunks, key=lambda c: len(letters(c))))
            # three 20-letter samples; text extraction can reorder lines around maths, so one hit is enough
            n = len(chunk)
            needles = [chunk[i:i + 20] for i in (0, max(0, n // 2 - 10), max(0, n - 20))] if n > 20 else [chunk]
            if chunk and not any(nd in pdf_letters for nd in needles):
                missing += 1
        n_det = len(re.findall(r"<details>", src))
        print(f"print: {n_det - missing}/{n_det} fold-outs present in PDF")
        if missing:
            ok = False
    finally:
        srv.shutdown(); probe.unlink()
    print("OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
