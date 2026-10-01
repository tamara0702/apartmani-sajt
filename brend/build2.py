import math
def hexpts(cx,cy,r):
    return " ".join(f"{cx+r*math.cos(math.radians(60*i+30)):.1f},{cy+r*math.sin(math.radians(60*i+30)):.1f}" for i in range(6))

THEMES={
 "svetla":dict(bg="#fbf6e9",ink="#3e2412",gold="#b98417",soft="#8a6a2c",drip="#d9a32b",pill="#3e2412",pilltxt="#fbf6e9",ring="#3e2412"),
 "tamna":dict(bg="#1a110a",ink="#f3e7c9",gold="#d9a93a",soft="#c9b27a",drip="#d9a93a",pill="#d9a93a",pilltxt="#1a110a",ring="#d9a93a"),
}

def bee(c,sw=3.5,s=1.0):
    g=c["gold"]
    return f'''<g transform="scale({s}) rotate(-12)" fill="none" stroke="{g}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">
<ellipse cx="-8" cy="-38" rx="26" ry="14" transform="rotate(-28 -8 -38)"/>
<ellipse cx="22" cy="-36" rx="26" ry="14" transform="rotate(22 22 -36)"/>
<ellipse cx="0" cy="0" rx="40" ry="28"/>
<path d="M-12 -26.7 Q-19 0 -12 26.7 M10 -27.1 Q3 0 10 27.1 M28 -20 Q22 0 28 20"/>
<circle cx="-54" cy="0" r="14"/>
<path d="M-62 -12 Q-68 -30 -80 -30 M-52 -14 Q-52 -34 -64 -40"/>
<path d="M40 0 L56 0"/>
<circle cx="-58" cy="-3" r="2" fill="{g}" stroke="none"/>
</g>'''

def emblem(c,uid,d=400):
    ring=c["ring"]; g=c["gold"]; ink=c["ink"]
    hexes="".join(f'<polygon points="{hexpts(200+i*0,200,0)}"/>' for i in [])
    return f'''<defs><path id="t{uid}" d="M 50 200 A 150 150 0 0 1 350 200"/><path id="b{uid}" d="M 36 200 A 164 164 0 0 0 364 200"/></defs>
<circle cx="200" cy="200" r="196" fill="none" stroke="{ring}" stroke-width="5"/>
<circle cx="200" cy="200" r="184" fill="none" stroke="{g}" stroke-width="2"/>
<circle cx="200" cy="200" r="122" fill="none" stroke="{g}" stroke-width="2"/>
<text font-family="Georgia,serif" font-weight="700" font-size="46" letter-spacing="6" fill="{ink}" text-anchor="middle"><textPath href="#t{uid}" startOffset="50%">DEDIN MED</textPath></text>
<text font-family="Georgia,serif" font-weight="700" font-size="27" letter-spacing="12" fill="{g}" text-anchor="middle"><textPath href="#b{uid}" startOffset="50%">ORGANIC</textPath></text>
<polygon points="{hexpts(48,214,9)}" fill="{g}"/><polygon points="{hexpts(352,214,9)}" fill="{g}"/>
<g transform="translate(205,200)">{bee(c,3.2,1.55)}</g>'''

def drip(W,base,drops,fill):
    r=14; d=f"M0 0 L{W} 0 L{W} {base} "
    for x,l,hw in sorted(drops,reverse=True):
        d+=f"L{x+hw+r} {base} Q{x+hw} {base} {x+hw} {base+r} L{x+hw} {base+l-hw} A{hw} {hw} 0 0 1 {x-hw} {base+l-hw} L{x-hw} {base+r} Q{x-hw} {base} {x-hw-r} {base} "
    d+=f"L0 {base} Z"
    return f'<path d="{d}" fill="{fill}"/>'

def label(theme,kind,sub,net,W,H,name,big=True):
    c=THEMES[theme]; s=W/950
    em=W*0.44; es=em/400
    top=int(H*0.05)
    drops=[(W*f,H*l,W*w) for f,l,w in [(.08,.075,.016),(.2,.115,.02),(.33,.06,.014),(.46,.095,.018),(.58,.13,.02),(.7,.07,.015),(.83,.11,.019),(.93,.06,.014)]]
    y0=H*0.15
    out=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W/10}mm" height="{H/10}mm">
<defs><clipPath id="r"><rect width="{W}" height="{H}" rx="{36*s}"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="{c['bg']}"/>
{drip(W,H*0.07,drops,c['drip'])}
<rect x="{28*s}" y="{28*s}" width="{W-56*s}" height="{H-56*s}" rx="{22*s}" fill="none" stroke="{c['gold']}" stroke-width="{2.5*s}" opacity="0.7"/>
<g transform="translate({(W-em)/2},{H*0.215}) scale({es})">{emblem(c,name)}</g>'''
    y=H*0.215+em+H*0.055
    out+=f'<text x="{W/2}" y="{y}" font-family="Georgia,serif" font-size="{30*s}" letter-spacing="{7*s}" fill="{c["gold"]}" text-anchor="middle" font-style="italic">pravi domaći med</text>'
    y+=H*0.085
    out+=f'<text x="{W/2}" y="{y}" font-family="Georgia,serif" font-weight="700" font-size="{104*s}" fill="{c["ink"]}" text-anchor="middle">{kind}</text>'
    y+=H*0.048
    out+=f'<text x="{W/2}" y="{y}" font-family="Georgia,serif" font-size="{40*s}" letter-spacing="{16*s}" fill="{c["gold"]}" text-anchor="middle">MED</text>'
    y+=H*0.03
    out+=f'<g transform="translate({W/2},{y})"><line x1="{-150*s}" x2="{-34*s}" y1="0" y2="0" stroke="{c["gold"]}" stroke-width="{3*s}"/><line x1="{34*s}" x2="{150*s}" y1="0" y2="0" stroke="{c["gold"]}" stroke-width="{3*s}"/><polygon points="{hexpts(0,0,16*s)}" fill="{c["gold"]}"/></g>'
    y+=H*0.04
    out+=f'<text x="{W/2}" y="{y}" font-family="Georgia,serif" font-size="{34*s}" fill="{c["soft"]}" text-anchor="middle">{sub}</text>'
    y+=H*0.06
    pw=300*s;ph=66*s
    out+=f'<rect x="{W/2-pw/2}" y="{y-ph*0.72}" width="{pw}" height="{ph}" rx="{ph/2}" fill="{c["pill"]}"/><text x="{W/2}" y="{y}" font-family="Georgia,serif" font-weight="700" font-size="{38*s}" fill="{c["pilltxt"]}" text-anchor="middle">NETO {net}</text>'
    y+=H*0.052
    out+=f'<text x="{W/2}" y="{y}" font-family="Georgia,serif" font-size="{31*s}" fill="{c["ink"]}" text-anchor="middle">Tel: 062 755 336  ·  @dedin.med.organic</text>'
    out+='</g></svg>'
    return out

def main():
    for th in THEMES:
        open(f"emblem-{th}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -10 420 420" width="600" height="600"><rect x="-10" y="-10" width="420" height="420" fill="{THEMES[th]["bg"]}"/>{emblem(THEMES[th],"e")}</svg>')
        open(f"etiketa-900ml-{th}.svg","w").write(label(th,"Livadski","sa cvetnih livada","1200 g",950,1250,"a"))
        open(f"etiketa-390ml-sestougaona-{th}.svg","w").write(label(th,"Livadski","sa cvetnih livada","500 g",700,900,"b"))

if __name__=='__main__':
    main()
