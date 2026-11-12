"""Small SVG helpers for the posters (flow chips, trees, layers)."""

def flow(labels, colors=None, w=330):
    n = len(labels); gap = 14; avail = w - 8 - (n - 1) * gap
    wts = [len(l) + 3.5 for l in labels]; tot = sum(wts)
    bws = [avail * x / tot for x in wts]
    fs = min(13.5, min((bw - 14) / (len(l) * 0.6) for bw, l in zip(bws, labels)))
    out = [f'<svg viewBox="0 0 {w} 50" width="{int((w-30)*1.28)}">']
    x = 4
    for i, (l, bw) in enumerate(zip(labels, bws)):
        c = (colors or ["#27479b", "#17703a", "#b3261e", "#6a2c91", "#b4560a"])[i % 5]
        out.append(f'<rect x="{x:.1f}" y="8" width="{bw:.1f}" height="32" rx="15" fill="#fff" stroke="{c}" stroke-width="2"/>')
        out.append(f'<text x="{x+bw/2:.1f}" y="28.5" font-size="{fs:.1f}" text-anchor="middle">{l}</text>')
        if i < n - 1: out.append(f'<path d="M{x+bw:.1f} 24 L{x+bw+gap:.1f} 24" stroke="#555" stroke-width="2"/>')
        x += bw + gap
    out.append("</svg>"); return "".join(out)

def tree(vals=("1", "2", "3", "4", "5", "6", "7"), color="#b3261e"):
    pos = [(150, 18), (75, 62), (225, 62), (38, 108), (112, 108), (188, 108), (262, 108)]
    ed = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    o = ['<svg viewBox="0 0 300 130" width="230"><g stroke="#444" stroke-width="1.8">']
    for a, b in ed: o.append(f'<path d="M{pos[a][0]} {pos[a][1]+11} L{pos[b][0]} {pos[b][1]-11}"/>')
    o.append('</g>')
    for (x, y), v in zip(pos, vals): o.append(f'<circle cx="{x}" cy="{y}" r="14" fill="#fff" stroke="{color}" stroke-width="2"/><text x="{x}" y="{y+5}" font-size="15" text-anchor="middle">{v}</text>')
    o.append('</svg>'); return "".join(o)


def boxes_row(vals, color="#27479b", labels=None):
    n = len(vals); o = [f'<svg viewBox="0 0 {n*46+20} 60" width="{min(300, n*46+20)}">']
    for i, v in enumerate(vals):
        o.append(f'<rect x="{10+i*46}" y="8" width="44" height="30" fill="#fff" stroke="{color}" stroke-width="2"/><text x="{32+i*46}" y="29" font-size="16" text-anchor="middle">{v}</text>')
        if labels and i < len(labels) and labels[i]: o.append(f'<text x="{32+i*46}" y="54" font-size="13" text-anchor="middle" fill="#b3261e">{labels[i]}</text>')
    o.append('</svg>'); return "".join(o)
