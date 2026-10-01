import math
BROWN="#3e2412"; GOLD="#e6a41c"; AMBER="#c97d0a"; CREAM="#fbf1d6"; GREEN="#5b6b2f"

def hexpts(cx,cy,r):
    return " ".join(f"{cx+r*math.cos(math.radians(60*i+30)):.1f},{cy+r*math.sin(math.radians(60*i+30)):.1f}" for i in range(6))

def bee():
    return f'''
<g transform="translate(205,208) rotate(-20) scale(1.35)">
  <ellipse cx="-14" cy="-34" rx="26" ry="15" fill="#fff" stroke="{BROWN}" stroke-width="3" transform="rotate(-25 -14 -34)"/>
  <ellipse cx="18" cy="-36" rx="26" ry="15" fill="#fff" stroke="{BROWN}" stroke-width="3" transform="rotate(25 18 -36)"/>
  <ellipse cx="0" cy="0" rx="42" ry="30" fill="{GOLD}" stroke="{BROWN}" stroke-width="4"/>
  <clipPath id="bc"><ellipse cx="0" cy="0" rx="42" ry="30"/></clipPath>
  <g clip-path="url(#bc)" fill="{BROWN}"><rect x="-18" y="-32" width="11" height="64"/><rect x="2" y="-32" width="11" height="64"/><rect x="21" y="-32" width="11" height="64"/></g>
  <ellipse cx="0" cy="0" rx="42" ry="30" fill="none" stroke="{BROWN}" stroke-width="4"/>
  <circle cx="-50" cy="-2" r="17" fill="{BROWN}"/>
  <circle cx="-56" cy="-7" r="3.5" fill="{CREAM}"/>
  <path d="M-58 5 Q-52 11 -45 5" stroke="{CREAM}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M-58 -17 Q-66 -34 -76 -32 M-50 -19 Q-52 -38 -62 -42" stroke="{BROWN}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M42 0 L58 0" stroke="{BROWN}" stroke-width="5" stroke-linecap="round"/>
</g>'''

def logo(uid="a"):
    hexes=""
    r=34
    for dx,dy in [(0,0),(1,0),(-1,0),(0.5,1),(-0.5,1),(0.5,-1),(-0.5,-1),(1.5,1),(-1.5,1),(1.5,-1),(-1.5,-1),(2,0),(-2,0)]:
        cx=200+dx*r*math.sqrt(3); cy=200+dy*r*1.5
        if math.hypot(cx-200,cy-200)<108:
            hexes+=f'<polygon points="{hexpts(cx,cy,r-2)}" fill="{GOLD}" fill-opacity="0.35" stroke="{AMBER}" stroke-width="2"/>'
    return f'''
<defs>
<path id="top{uid}" d="M 52 200 A 148 148 0 0 1 348 200"/>
<path id="bot{uid}" d="M 40 200 A 160 160 0 0 0 360 200"/>
<clipPath id="in{uid}"><circle cx="200" cy="200" r="112"/></clipPath>
</defs>
<circle cx="200" cy="200" r="196" fill="{BROWN}"/>
<circle cx="200" cy="200" r="186" fill="none" stroke="{GOLD}" stroke-width="3"/>
<circle cx="200" cy="200" r="128" fill="{GOLD}"/>
<circle cx="200" cy="200" r="122" fill="{CREAM}"/>
<g clip-path="url(#in{uid})">{hexes}</g>
{bee()}
<text font-family="Georgia,'Times New Roman',serif" font-weight="700" font-size="44" letter-spacing="5" fill="{CREAM}" text-anchor="middle"><textPath href="#top{uid}" startOffset="50%">DEDIN MED</textPath></text>
<text font-family="Georgia,'Times New Roman',serif" font-weight="700" font-size="26" letter-spacing="11" fill="{GOLD}" text-anchor="middle"><textPath href="#bot{uid}" startOffset="50%">ORGANIC</textPath></text>
<g fill="{GOLD}"><circle cx="46" cy="214" r="5"/><circle cx="354" cy="214" r="5"/></g>'''

open("logo.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="800" height="800">{logo()}</svg>')

# label 90x120 mm  -> units: 1mm = 10
def label(kind,sub,accent,fn):
    W,H=900,1200
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W/10}mm" height="{H/10}mm">
<defs><clipPath id="r"><rect width="{W}" height="{H}" rx="40"/></clipPath></defs>
<g clip-path="url(#r)">
<rect width="{W}" height="{H}" fill="{CREAM}"/>
<rect width="{W}" height="330" fill="{BROWN}"/>
<g opacity="0.12">{"".join(f'<polygon points="{hexpts(x*52*1.732+(26*1.732 if y%2 else 0),y*78+10,30)}" fill="none" stroke="{GOLD}" stroke-width="3"/>' for x in range(0,18) for y in range(0,5))}</g>
<g transform="translate(301,14) scale(0.76)">{logo("L")}</g>
<path d="M0 330 Q225 400 450 330 T900 330 L900 345 Q675 415 450 345 T0 345Z" fill="{GOLD}"/>
<rect x="40" y="385" width="{W-80}" height="{H-425}" rx="24" fill="none" stroke="{BROWN}" stroke-width="5"/>
<text x="450" y="500" font-family="Georgia,serif" font-size="34" letter-spacing="8" fill="{AMBER}" text-anchor="middle" font-style="italic">pravi domaći med</text>
<text x="450" y="630" font-family="Georgia,serif" font-weight="700" font-size="116" fill="{BROWN}" text-anchor="middle">{kind}</text>
<text x="450" y="705" font-family="Georgia,serif" font-size="46" letter-spacing="14" fill="{accent}" text-anchor="middle">MED</text>
<g transform="translate(450,770)"><line x1="-170" x2="-40" y1="0" y2="0" stroke="{GOLD}" stroke-width="4"/><line x1="40" x2="170" y1="0" y2="0" stroke="{GOLD}" stroke-width="4"/><polygon points="{hexpts(0,0,20)}" fill="{GOLD}"/></g>
<text x="450" y="840" font-family="Georgia,serif" font-size="40" fill="{BROWN}" text-anchor="middle">{sub}</text>
<rect x="300" y="880" width="300" height="80" rx="40" fill="{BROWN}"/>
<text x="450" y="934" font-family="Georgia,serif" font-weight="700" font-size="46" fill="{CREAM}" text-anchor="middle">NETO 900 g</text>
<text x="450" y="1030" font-family="Georgia,serif" font-weight="700" font-size="36" fill="{BROWN}" text-anchor="middle">Proizvođač: Dedin med organic</text>
<text x="450" y="1085" font-family="Georgia,serif" font-size="36" fill="{BROWN}" text-anchor="middle">Tel: 062 755 336  ·  IG: @dedin.med.organic</text>
<text x="450" y="1138" font-family="Georgia,serif" font-size="28" fill="{BROWN}" text-anchor="middle">Datum punjenja: ____________   Rok upotrebe: ____________</text>
</g></svg>'''
for k,s,a,f in [("Livadski","sa cvetnih livada","#7a5a10","livadski"),("Bagremov","od cvetova bagrema","#7a5a10","bagremov"),("Lipov","od cvetova lipe","#5b6b2f","lipov")]:
    open(f"etiketa-{f}.svg","w").write(label(k,s,a,f))
