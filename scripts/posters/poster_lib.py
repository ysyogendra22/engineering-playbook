"""Tiny poster renderer: builds an HTML page from boxes and screenshots it with headless Chrome.

Usage (from this folder):  python3 poster_ds.py ../../01-data-structure/data_structure_cheatsheet.png
Needs: Google Chrome (set CHROME=/path/to/chrome if it is not at the macOS default), Pillow, internet for Google Fonts.
"""
import html, os, re, subprocess, tempfile
from PIL import Image

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
COLORS = {"r": "#b3261e", "g": "#17703a", "b": "#27479b", "p": "#6a2c91", "o": "#b4560a", "t": "#0b6e75"}

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#1f2937;--paper:#fbfaf7;--line:#2b2f36;--soft:#eef0f3}
body{width:1700px;background:var(--paper);color:var(--ink);font-family:'Inter','SF Pro Text','Helvetica Neue',Arial,sans-serif;font-size:16.5px;line-height:1.42;padding:22px 24px 26px;-webkit-font-smoothing:antialiased}
.head{display:grid;grid-template-columns:1fr 2fr 1fr;align-items:center;margin-bottom:14px}
.head .l,.head .r{font-size:17px;font-weight:500;line-height:1.4;color:#475569}
.head .r{text-align:right}
.head .c{text-align:center}
.title{font-weight:800;font-size:52px;letter-spacing:-1px;line-height:1.05}
.title b{color:#b3261e;background:none;font-weight:800}
.title.long{font-size:46px}
.sub{font-size:19px;font-weight:500;margin-top:8px;color:#475569}
.sub u{color:#27479b;text-decoration:none;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(4,1fr);border:2px solid var(--line);border-radius:4px}
.box{border:1px solid #9aa1ab;padding:13px 16px 15px;position:relative;min-width:0}
.box h2{font-weight:700;font-size:15.5px;letter-spacing:.06em;margin-bottom:8px;text-transform:uppercase}
.box h3{font-size:16px;font-weight:600;margin:8px 0 3px}
.span2{grid-column:span 2}.span3{grid-column:span 3}.span4{grid-column:span 4}
b{font-weight:600;background:linear-gradient(transparent 60%,#ffe9a3 60%)}
ul{list-style:none}
li{padding-left:16px;position:relative;margin:2px 0}
li:before{content:"";position:absolute;left:2px;top:.62em;width:5px;height:5px;border-radius:50%;background:#94a3b8}
li.sub2{padding-left:30px;font-size:15.5px}
li.ok:before{content:"✓";background:none;width:auto;height:auto;top:0;left:0;color:#17703a;font-weight:700}
li.ok{padding-left:20px}
.kv{display:grid;grid-template-columns:auto 1fr;gap:3px 14px;align-items:baseline}
.kv .k{font-weight:600}
.kv .code,.k.code{font-family:'JetBrains Mono','Menlo',monospace;font-size:13.5px;font-weight:500}
table{border-collapse:collapse;width:100%;font-size:15px}
td,th{border:1px solid #cdd2d9;padding:3px 8px;text-align:left;vertical-align:top}
th{background:var(--soft);font-weight:600}
code,.code{font-family:'JetBrains Mono','Menlo',monospace;font-size:13.5px;background:#eceff3;padding:1px 4px;border-radius:4px}
pre{font-family:'JetBrains Mono','Menlo',monospace;font-size:12.8px;line-height:1.5;border:1px solid #b7d9c2;border-left:4px solid #17703a;border-radius:6px;padding:8px 11px;margin:8px 0 4px;background:#f3f9f5;white-space:pre-wrap}
.callout{border:1.5px solid #b3261e;border-radius:8px;padding:8px 11px;text-align:center;font-weight:600;font-size:15px;color:#b3261e;margin:9px 0 2px;line-height:1.35;background:rgba(179,38,30,.04)}
.callout.g{border-color:#17703a;color:#17703a;background:rgba(23,112,58,.05)}.callout.b{border-color:#27479b;color:#27479b;background:rgba(39,71,155,.05)}
.callout code{background:rgba(0,0,0,.06)}
.big{font-size:21px;font-weight:600;text-align:center;color:#17703a;line-height:1.35;letter-spacing:-.2px;padding-top:6px}
.mut{color:#5b6573;font-size:14.5px;margin-top:5px}
code,pre,.code,.kv .code{font-variant-ligatures:none;font-feature-settings:'liga' 0,'calt' 0}
td code{white-space:nowrap}
svg{display:block;margin:6px auto 2px;max-width:100%}
svg text{font-family:'Inter','Helvetica Neue',Arial,sans-serif;fill:#1f2937;letter-spacing:-.01em}
.row{display:flex;gap:10px;align-items:flex-start}.row>*{flex:1;min-width:0}
"""
# Final font choice: Plus Jakarta Sans
FONT_IMPORT = "Plus+Jakarta+Sans:wght@400;500;600;700;800"
FONT_CSS = """body,svg text,.title,.sub,.big,.callout,h2,h3,th,td,.head .l,.head .r,.kv .k,li{font-family:'Plus Jakarta Sans','Inter',sans-serif}
.title{letter-spacing:-1.2px} h2{letter-spacing:.07em}"""

def esc(s): return html.escape(s, quote=False)
def inline(s):
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s

def ul(items, ok=False):
    out = []
    for it in items:
        sub = it.startswith("  ")
        cls = ' class="sub2"' if sub else (' class="ok"' if ok else "")
        out.append(f"<li{cls}>{inline(it.strip())}</li>")
    return "<ul>" + "".join(out) + "</ul>"

def kv(rows, codek=False):
    k = "k code" if codek else "k"
    return '<div class="kv">' + "".join(f'<div class="{k}">{inline(a)}</div><div>{inline(b)}</div>' for a, b in rows) + "</div>"

def table(head, rows):
    h = "<tr>" + "".join(f"<th>{inline(x)}</th>" for x in head) + "</tr>" if head else ""
    return "<table>" + h + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

def pre(t): return "<pre>" + esc(t.strip("\n")) + "</pre>"
def callout(t, c=""): return f'<div class="callout {c}">{inline(t).replace(chr(10), "<br>")}</div>'
def h3(t, c=None): return f'<h3 style="color:{COLORS[c]}">{inline(t)}</h3>' if c else f"<h3>{inline(t)}</h3>"
def p(t): return f"<p>{inline(t)}</p>"
def mut(t): return f'<p class="mut">{inline(t)}</p>'
def row(*cols): return '<div class="row">' + "".join(f"<div>{c}</div>" for c in cols) + "</div>"

def box(n, title, color, body, span=1):
    cls = "box" + (f" span{span}" if span > 1 else "")
    num = f"{n}. " if n else ""
    return f'<div class="{cls}"><h2 style="color:{COLORS[color]}">{num}{esc(title)}</h2>{body}</div>'

def page(meta, boxes):
    head = f"""<div class="head"><div class="l">{meta['left']}</div>
<div class="c"><div class="title{' long' if len(re.sub('<[^>]+>','',meta['title']))>24 else ''}">{meta['title']}</div><div class="sub">{meta['sub']}</div></div>
<div class="r">{meta['right']}</div></div>"""
    fonts = f"<style>@import url('https://fonts.googleapis.com/css2?family={FONT_IMPORT}&family=JetBrains+Mono:wght@400;500;600&display=swap');</style>"
    return f"<!doctype html><meta charset=utf-8>{fonts}<style>{CSS}</style><style>{FONT_CSS}</style><body><div id=poster>{head}<div class=grid>{''.join(boxes)}</div></div></body>"

def render(html_text, out_png):
    work = tempfile.mkdtemp(prefix="poster_")
    f = os.path.join(work, "p.html")
    probe = html_text.replace("</body>", "<script>window.addEventListener('load',()=>document.fonts.ready.then(()=>{setTimeout(()=>{document.title='H'+Math.ceil(document.getElementById('poster').getBoundingClientRect().height)+'W'+document.body.scrollWidth;let d=document.createElement('div');d.id='hh';d.textContent=document.title;document.body.appendChild(d)},300)}))</script></body>")
    open(f, "w", encoding="utf-8").write(probe)
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=15000",
                        "--window-size=1700,3000", "--dump-dom", "file://" + f], capture_output=True, text=True, timeout=120)
    m = re.search(r'id="hh">H(\d+)W(\d+)', r.stdout)
    if not m: raise SystemExit("height probe failed: " + r.stdout[-400:] + r.stderr[-400:])
    h = int(m.group(1)) + 44
    open(f, "w", encoding="utf-8").write(html_text)
    raw = os.path.join(work, "raw.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=15000",
                    "--force-device-scale-factor=2", f"--window-size=1700,{h}", f"--screenshot={raw}", "file://" + f],
                   capture_output=True, text=True, timeout=180)
    im = Image.open(raw).convert("RGB")
    im.save(out_png, optimize=True)
    return im.size
