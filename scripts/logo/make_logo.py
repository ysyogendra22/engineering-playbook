#!/usr/bin/env python3
"""Builds the logo files in assets/: the liquid-glass "EP" mark, the README wordmarks and the social card.

Run from anywhere:   python3 scripts/logo/make_logo.py
Needs: Google Chrome (set CHROME=/path/to/chrome if it is not at the macOS default), Pillow, internet for Google Fonts.

Writes: assets/logo-mark.svg, logo-mark.png, logo.png, logo-dark.png, social-preview.png
"""
import os, re, subprocess, tempfile
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

# ---------------------------------------------------------------- the mark
# One fused glyph: a vertical stem, a P-bowl on top and an E-base underneath (stroked path, round caps).
STEM_X, TOP, MID, BOTTOM, STROKE = 150, 124, 252, 388, 66
BOWL_R = (MID - TOP) / 2

# Warm sunset colour mesh: (cx, cy, radius, colour, opacity); the first colour also tints the inner glow.
BASE = "#1B0F4A"
BLOBS = [(430, 440, 260, "#FF8A3D", 1), (90, 430, 200, "#FF3D9A", .95), (420, 90, 240, "#7B4DFF", 1), (80, 90, 150, "#3D7BFF", .8)]


def glyph_path():
    bowl_right = STEM_X + 150 + BOWL_R
    left, right = STEM_X - STROKE / 2, bowl_right + STROKE / 2
    sx = STEM_X + 256 - (left + right) / 2
    return (f"M{sx:.1f} {TOP} V{BOTTOM} M{sx:.1f} {TOP} H{sx+150:.1f} A{BOWL_R} {BOWL_R} 0 0 1 {sx+150:.1f} {MID} H{sx:.1f} "
            f"M{sx:.1f} {BOTTOM} H{sx+140:.1f}")


def mark_svg(uid="ep"):
    d, W = glyph_path(), STROKE

    def st(w, col, extra=""):
        return f'<path d="{d}" fill="none" stroke="{col}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{w}" {extra}/>'
    grads = "".join(f'<radialGradient id="rb{i}" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{c}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'
                    for i, (x, y, r, c, o) in enumerate(BLOBS))
    bg = f'<rect width="512" height="512" fill="{BASE}"/>' + "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#rb{i})" opacity="{o}"/>' for i, (x, y, r, c, o) in enumerate(BLOBS))
    defs = f'''{grads}
<clipPath id="tile"><rect width="512" height="512" rx="120"/></clipPath>
<mask id="body"><rect width="512" height="512" fill="#000"/>{st(W, "#fff")}</mask>
<mask id="rim"><rect width="512" height="512" fill="#000"/>{st(W+3, "#fff")}{st(W-3, "#000")}</mask>
<mask id="rim2"><rect width="512" height="512" fill="#000"/>{st(W-10, "#fff")}{st(W-15, "#000")}</mask>
<linearGradient id="rimg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".45" stop-color="#fff" stop-opacity=".18"/><stop offset=".62" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#fff" stop-opacity=".95"/></linearGradient>
<linearGradient id="gl" x1="0" y1="0" x2="0.5" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity=".10"/><stop offset="1" stop-color="#fff" stop-opacity=".22"/></linearGradient>
<filter id="bl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="20"/></filter>
<filter id="bl2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9"/></filter>
<filter id="bl3" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="sh" x="-30%" y="-30%" width="160%" height="170%"><feGaussianBlur stdDeviation="16"/></filter>'''
    body = (
        f'<g clip-path="url(#tile)">{bg}'
        f'<g filter="url(#sh)" opacity=".55" transform="translate(0 16)">{st(W, "#2a0f3a")}</g>'                    # soft shadow
        f'<g mask="url(#body)"><g filter="url(#bl)">{bg}</g><rect width="512" height="512" fill="#fff" fill-opacity=".07"/></g>'  # frosted body
        f'<g mask="url(#body)"><rect width="512" height="512" fill="url(#gl)"/></g>'                                  # sheen
        f'<g mask="url(#body)"><g filter="url(#bl2)" opacity=".55" transform="translate(8 10)">{st(W*0.38, BLOBS[0][3])}</g></g>'  # inner glow
        f'<g mask="url(#body)"><g filter="url(#bl3)" opacity=".75" transform="translate(-{W*0.16:.0f} -{W*0.2:.0f})">{st(W*0.14, "#fff")}</g></g>'  # specular
        f'<g mask="url(#rim2)"><rect width="512" height="512" fill="#fff" fill-opacity=".28"/></g>'
        f'<g mask="url(#rim)"><rect width="512" height="512" fill="url(#rimg)"/></g>'                                 # lit rim
        f'</g><rect x="1.5" y="1.5" width="509" height="509" rx="118.5" fill="none" stroke="#fff" stroke-opacity=".2" stroke-width="3"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" role="img" aria-label="Engineering Playbook">'
           f'<defs>{defs}</defs>{body}</svg>')
    for i in set(re.findall(r'id="([^"]+)"', svg)):          # prefix ids so several marks can share one page
        svg = svg.replace(f'id="{i}"', f'id="{uid}_{i}"').replace(f'url(#{i})', f'url(#{uid}_{i})')
    return svg


def sized(svg, w, h=None):
    return svg.replace('width="512" height="512"', f'width="{w}" height="{h or w}"', 1)


# ---------------------------------------------------------------- rendering helpers
FONTS = ("<style>@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800"
         "&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap');</style>")
WORD_GRAD = "linear-gradient(90deg,#FF3D9A,#FF3D9A)"   # the word "playbook": solid magenta


def shot(html, out, w, h, transparent=False):
    f = Path(tempfile.mkdtemp(prefix="logo_")) / "p.html"
    f.write_text(html, encoding="utf-8")
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=15000",
           f"--window-size={w},{h}", f"--screenshot={out}"]
    if transparent: cmd.append("--default-background-color=00000000")
    subprocess.run(cmd + ["file://" + str(f)], capture_output=True, text=True, timeout=180)
    if not Path(out).exists(): raise SystemExit("Chrome did not write " + str(out))


def wordmark(dark, out):
    ink = "#F4F6FF" if dark else "#0B0D16"
    html = f'''<!doctype html><meta charset=utf-8>{FONTS}
<style>html,body{{margin:0;background:transparent}}
.row{{display:flex;align-items:center;gap:60px;padding:40px;width:max-content}}
.t{{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:158px;letter-spacing:-.045em;line-height:1;white-space:nowrap;color:{ink};font-variation-settings:'opsz' 96}}
.t span{{background:{WORD_GRAD};-webkit-background-clip:text;background-clip:text;color:transparent;padding-bottom:.12em}}</style>
<body><div class=row>{sized(mark_svg("wm"), 264)}<div class=t>engineering <span>playbook</span></div></div></body>'''
    tmp = Path(tempfile.mkdtemp(prefix="logo_")) / "raw.png"
    shot(html, tmp, 2600, 344, transparent=True)
    im = Image.open(tmp).convert("RGBA")
    box = im.getchannel("A").getbbox()
    left, right = max(box[0] - 40, 0), box[2] + 40
    im.crop((left, 0, right, 344)).save(out, optimize=True)


def social(out):
    posters = [ROOT / "04-backend-engineering" / "backend_cheatsheet.png", ROOT / "10-database" / "database_cheatsheet.png"]
    chips = ["Data Structures", "Algorithms", "LeetCode Patterns", "Backend", "System Design", "Mobile", "AI", "Architecture", "Databases", "OOP & Java", "Behavioral"]
    chip_html = "".join(f"<i>{c}</i>" for c in chips)
    html = f'''<!doctype html><meta charset=utf-8>{FONTS}
<style>*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1280px;height:640px;background:#FBFAF7;position:relative;overflow:hidden;font-family:'Plus Jakarta Sans',sans-serif;color:#1f2937}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:14px;background:linear-gradient(180deg,#FF9A3D,#FF3D9A 50%,#8F5BFF)}}
.mark{{position:absolute;left:64px;top:50px}}
.tag{{position:absolute;left:166px;top:78px;font-size:23px;font-weight:700;color:#7B4DFF}}
.h{{position:absolute;left:62px;top:146px;font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:98px;letter-spacing:-.045em;line-height:1.02;color:#0B0D16;font-variation-settings:'opsz' 96}}
.h span{{background:{WORD_GRAD};-webkit-background-clip:text;background-clip:text;color:transparent;display:inline-block;padding-bottom:.1em}}
.sub{{position:absolute;left:64px;top:392px;font-size:27px;font-weight:600;color:#4B5563}}
.chips{{position:absolute;left:64px;top:448px;width:640px;display:flex;flex-wrap:wrap;gap:12px 14px}}
.chips i{{font-style:normal;font-size:20px;font-weight:600;padding:6px 18px;border:1.5px solid #D9DAE2;border-radius:999px;background:#fff}}
.p{{position:absolute;background:#fff;border:1px solid #cfd2da;border-radius:6px;box-shadow:0 18px 44px rgba(20,16,40,.22)}}
.p img{{display:block;width:100%}}</style>
<body><div class=bar></div><div class=mark>{sized(mark_svg("sp"), 86)}</div>
<div class=tag>for FAANG interviews · Kotlin · 2026</div>
<div class=h>engineering<br><span>playbook</span></div>
<div class=sub>Simple notes · Clear diagrams · Cheat sheets</div>
<div class=chips>{chip_html}</div>
<div class=p style="left:800px;top:-70px;width:470px;transform:rotate(-3deg)"><img src="file://{posters[0]}"></div>
<div class=p style="left:858px;top:64px;width:500px;transform:rotate(2deg)"><img src="file://{posters[1]}"></div>
</body>'''
    shot(html, out, 1280, 640)


def main():
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "logo-mark.svg").write_text(mark_svg("ep"), encoding="utf-8")
    html = f"<!doctype html><meta charset=utf-8><style>html,body{{margin:0;background:transparent}}svg{{display:block}}</style>{sized(mark_svg('mk'), 1024)}"
    shot(html, ASSETS / "logo-mark.png", 1024, 1024, transparent=True)
    wordmark(False, ASSETS / "logo.png")
    wordmark(True, ASSETS / "logo-dark.png")
    social(ASSETS / "social-preview.png")
    for n in ["logo-mark.png", "logo.png", "logo-dark.png", "social-preview.png"]:
        print(n, Image.open(ASSETS / n).size)


if __name__ == "__main__":
    main()
