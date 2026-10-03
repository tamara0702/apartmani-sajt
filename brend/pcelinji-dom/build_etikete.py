import math, os, re, subprocess, sys
from podaci import *

INK="#3e2412"; GOLD="#e6a41c"; DEEP="#c97d0a"; CREAM="#fbf1d6"; SOFT="#7a5a10"
SERIF="'Liberation Serif','Times New Roman',serif"
TITLE="'DejaVu Serif',Georgia,serif"
HERE=os.path.dirname(os.path.abspath(__file__))

def hexp(cx,cy,r,rot=30):
    return " ".join(f"{cx+r*math.cos(math.radians(60*i+rot)):.2f},{cy+r*math.sin(math.radians(60*i+rot)):.2f}" for i in range(6))

def logo(cx,cy,s):
    """Pravi logo iz ../logo.svg (krug, viewBox 400x400). Bez natpisa ORGANIC dok ORGANSKI nije True."""
    src=open(os.path.join(HERE,"..","logo.svg"),encoding="utf-8").read()
    inner=src[src.index("<defs>"):src.rindex("</svg>")]
    if not ORGANSKI:
        inner=re.sub(r'<text[^>]*>\s*<textPath href="#bota"[^>]*>ORGANIC</textPath></text>\n?','',inner)
        assert "ORGANIC" not in inner
    return f'<g transform="translate({cx},{cy}) scale({s}) translate(-200,-200)">{inner}</g>'

def znacka(cx,cy,s):
    """Značka 'Srpski proizvod' iz ../srpski-proizvod.svg (krug, viewBox 400x400)."""
    src=open(os.path.join(HERE,"..","srpski-proizvod.svg"),encoding="utf-8").read()
    inner=src[src.index("<defs>"):src.rindex("</svg>")]
    return f'<g transform="translate({cx},{cy}) scale({s}) translate(-200,-200)">{inner}</g>'

def t(x,y,txt,size,fill=INK,weight="400",fam=SERIF,ls=0,anchor="middle",style=""):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" letter-spacing="{ls}" fill="{fill}" text-anchor="{anchor}" {style}>{txt}</text>'

def label(W,H,neto,preview):
    b=BLEED; TW=W+2*b; TH=H+2*b; cx=TW/2
    top=b; bot=b+H
    band=H*0.285 if H>140 else H*0.30     # tamna traka sa logom
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TW} {TH}" width="{TW}mm" height="{TH}mm">']
    s.append(f'<rect width="{TW}" height="{TH}" fill="{CREAM}"/>')
    bandh=b+band
    s.append(f'<rect width="{TW}" height="{bandh}" fill="{INK}"/>')
    # saće u traci (prelazi preko preloma)
    hs=[]
    r=5.2; dx=r*math.sqrt(3); dy=r*1.5
    for row in range(-1,int(bandh/dy)+2):
        for col in range(-1,int(TW/dx)+2):
            x=col*dx+(dx/2 if row%2 else 0); y=row*dy
            hs.append(f'<polygon points="{hexp(x,y,r*0.93)}"/>')
    s.append(f'<clipPath id="bandclip"><rect width="{TW}" height="{bandh}"/></clipPath><g clip-path="url(#bandclip)" fill="none" stroke="{GOLD}" stroke-width=".18" opacity=".16">{"".join(hs)}</g>')
    # logo + naziv brenda (sve unutar sigurne zone, iznad talasa)
    R=min(band*0.40,(band+b-3-4)/2)
    cy=(b+3+bandh-4)/2
    zr=R*0.92; gap=5                          # logo i značka jedan pored drugog, centrirani
    x0=cx-(2*R+gap+2*zr)/2
    s.append(logo(x0+R,cy,R/196))
    s.append(znacka(x0+2*R+gap+zr,cy,zr/196))
    wy=bandh
    wave_bot=wy+2.8
    s.append(f'<path d="M0 {wy} Q{TW*.25} {wy+4.2} {TW*.5} {wy} T{TW} {wy} L{TW} {wy+1.2} Q{TW*.75} {wy+5.4} {TW*.5} {wy+1.2} T0 {wy+1.2}Z" fill="{GOLD}"/>')
    lines=[]
    if ORGANSKI: lines.append(("Organski proizvod",True))
    lines.append((f"Proizvođač: {PROIZVODJAC}",True))
    lines.append((ADRESA,False))
    if REG_BROJ: lines.append((f"Reg. broj: {REG_BROJ}",False))
    lines.append(("Zemlja porekla: Srbija",False))
    lines.append(("Čuvati na suvom i tamnom mestu, do 25 °C.",False))
    fs=2.75; lh=fs*1.42
    blockh=len(lines)*lh+lh*2.1+fs*0.5
    ystart=bot-4.2-blockh
    rule=ystart-2.0
    big=min(W*0.135,12.0)
    ph=H*0.062 if H>140 else H*0.068
    tfs=W*0.043
    def stack(tag):
        y=0; out=[]
        if tag: y+=tfs; out.append(("tag",y)); y+=big*1.0
        else: y+=big*0.8
        out.append(("title",y)); y+=big*0.6; out.append(("med",y)); y+=4.4; out.append(("orn",y)); y+=3.2; out.append(("pill",y)); y+=ph
        return out,y
    space=rule-wave_bot
    pos,sh=stack(True)
    if space-sh<7: pos,sh=stack(False)
    tag=any(k=="tag" for k,_ in pos)
    y0=wave_bot+(space-sh)/2
    P={k:y0+v for k,v in pos}
    if tag: s.append(t(cx,P["tag"],"pravi domaći med",tfs,DEEP,"400",SERIF,ls=W*0.006,style='font-style="italic"'))
    s.append(t(cx,P["title"],"Bagremov",big,INK,"700",TITLE))
    s.append(t(cx,P["med"],"MED",W*0.06,SOFT,"400",SERIF,ls=W*0.03))
    s.append(f'<g transform="translate({cx},{P["orn"]})"><line x1="{-W*.2}" x2="{-W*.06}" stroke="{GOLD}" stroke-width=".5"/><line x1="{W*.06}" x2="{W*.2}" stroke="{GOLD}" stroke-width=".5"/><polygon points="{hexp(0,0,2.0,90)}" fill="{GOLD}"/></g>')
    s.append(f'<rect x="{cx-W*.26}" y="{P["pill"]}" width="{W*.52}" height="{ph}" rx="{ph/2}" fill="{INK}"/>')
    s.append(t(cx,P["pill"]+ph*0.68,f"NETO {neto}",ph*0.55,CREAM,"700",TITLE))
    s.append(f'<line x1="{b+W*.12}" x2="{b+W*.88}" y1="{rule}" y2="{rule}" stroke="{GOLD}" stroke-width=".35"/>')
    yy=ystart+fs
    for txt,bold in lines:
        s.append(t(cx,yy,txt,fs,INK,"700" if bold else "400"))
        yy+=lh
    yy+=fs*0.4
    s.append(t(cx,yy,"Najbolje upotrebiti do: ____ / ____ / ______",fs*1.02,INK,"700"))
    yy+=lh*1.15
    s.append(t(cx,yy,"LOT: ______________",fs*1.02,INK,"700"))
    if preview:
        s.append(f'<rect x="{b}" y="{b}" width="{W}" height="{H}" fill="none" stroke="#e0007a" stroke-width=".25" stroke-dasharray="1.2 .8"/>')
        s.append(f'<rect x="{b+3}" y="{b+3}" width="{W-6}" height="{H-6}" fill="none" stroke="#0a7bd8" stroke-width=".2" stroke-dasharray=".8 .8"/>')
    s.append('</svg>')
    return "\n".join(s)


jobs=[]
for name,W,H,neto,_ in ETIKETE:
    for preview in (False,True):
        fn=f"{name}{'-pregled' if preview else ''}"
        svg=label(W,H,neto,preview)
        p=os.path.join(HERE,fn+".svg"); open(p,"w",encoding="utf-8").write(svg)
        jobs.append((fn,W+2*BLEED,H+2*BLEED))
import json; json.dump({"jobs":jobs,"dpi":DPI},open(os.path.join(HERE,".jobs.json"),"w"))
