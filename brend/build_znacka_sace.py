"""Znacka 'Srpski proizvod' u obliku saca - samo linije, providna pozadina, sav tekst pretvoren u krive.
Pokretanje: python3 build_znacka_sace.py   (potreban fonttools; skripta fontova: Liberation Sans Bold, Dancing Script 700)"""
import math, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE=os.path.dirname(os.path.abspath(__file__))
SANS=TTFont("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf")
SCRIPT=TTFont(os.environ.get("SCRIPT_FONT","/tmp/claude-0/fx/package/files/dancing-script-latin-700-normal.woff"))

def glyphs(font,text,size,ls=0):
    """-> lista (glyphname, x_pomeraj, sirina) i ukupna sirina; ls = razmak izmedju slova"""
    cmap=font.getBestCmap(); gs=font.getGlyphSet(); upm=font["head"].unitsPerEm; k=size/upm
    out=[]; x=0
    for ch in text:
        n=cmap.get(ord(ch))
        if n is None: raise SystemExit(f"nema glifa za {ch!r}")
        w=font["hmtx"][n][0]*k
        out.append((n,x,w)); x+=w+ls
    return out,x-ls,gs,k

def text_path(font,text,size,ls,cx,cy,mode,pathpts=None,anchor_s=None):
    """mode 'flat': centrirano na (cx,cy) (cy = osnovna linija). mode 'path': po tacki-nizu pathpts, centrirano na duzini anchor_s."""
    gl,total,gs,k=glyphs(font,text,size,ls)
    d=[]
    for n,x,w in gl:
        if mode=="flat":
            ox=cx-total/2+x; oy=cy; ang=0
            M=(k,0,0,-k,ox,oy)
        else:
            s_mid=anchor_s-total/2+x+w/2
            (px,py),ang=at(pathpts,s_mid)
            c,sn=math.cos(ang),math.sin(ang)
            # glif centriran po sirini: lokalno (X-w/2/k, ...) -> rotacija -> pozicija
            hx=w/2
            M=(k*c, k*sn, k*sn, -k*c, px - hx*c, py - hx*sn)
            # (X,Y)->(k*X-hx , -k*Y) rotirano: x'=c*(kX-hx)-sn*(-kY)=c*kX+sn*kY-c*hx ; y'=sn*(kX-hx)+c*(-kY)
            M=(k*c, k*sn, k*sn, -k*c, px-hx*c, py-hx*sn)
        pen=SVGPathPen(gs,ntos=lambda v:f"{v:.2f}")
        gs[n].draw(TransformPen(pen,M))
        d.append(pen.getCommands())
    return " ".join(d),total

# ---- zaobljeni sestougao (flat-top), uzorkovan u tacke ----
def hexloop(R,rc,cx=200,cy=200,n=40):
    V=[(cx+R*math.cos(math.radians(60*i)),cy+R*math.sin(math.radians(60*i))) for i in range(6)]
    pts=[]
    for i in range(6):
        p0,p1,p2=V[i-1],V[i],V[(i+1)%6]
        def toward(a,b,dist):
            L=math.dist(a,b); return (a[0]+(b[0]-a[0])*dist/L,a[1]+(b[1]-a[1])*dist/L)
        a=toward(p1,p0,rc); b=toward(p1,p2,rc)
        for j in range(n+1):
            t=j/n
            pts.append(((1-t)**2*a[0]+2*t*(1-t)*p1[0]+t*t*b[0],(1-t)**2*a[1]+2*t*(1-t)*p1[1]+t*t*b[1]))
    return pts   # redosled: vrh po vrh, u smeru kazaljke na satu (y nadole), pocinje na desnom vrhu (i=0 je od V[5] ka V[0])

def poly_d(pts): return "M"+" L".join(f"{x:.2f} {y:.2f}" for x,y in pts)+"Z"

def at(pts,s):
    """tacka i ugao na duzini s duz otvorene polilinije pts"""
    acc=0
    for a,b in zip(pts,pts[1:]):
        L=math.dist(a,b)
        if acc+L>=s:
            t=(s-acc)/L; return (a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t),math.atan2(b[1]-a[1],b[0]-a[0])
        acc+=L
    return pts[-1],0

def arclen(pts): return sum(math.dist(a,b) for a,b in zip(pts,pts[1:]))

def build(color):
    R_OUT,R_IN,RC=192,162,34
    R_TXT_TOP,R_TXT_BOT=171,182      # osnovne linije teksta (gore unutra, dole spolja)
    parts=[]
    parts.append(f'<path d="{poly_d(hexloop(R_OUT,RC))}" fill="none" stroke="{color}" stroke-width="3.2" stroke-linejoin="round"/>')
    parts.append(f'<path d="{poly_d(hexloop(R_IN,RC))}" fill="none" stroke="{color}" stroke-width="1.6" stroke-linejoin="round"/>')
    # tekst po putanji: prozor oko sredine gornje/donje ivice (indeks 5n, odnosno 2n u zatvorenoj petlji)
    def window(loop,mid,half):
        N=len(loop); fw=[loop[mid]]; bw=[loop[mid]]; acc=0; i=mid
        while acc<half: acc+=math.dist(loop[i%N],loop[(i+1)%N]); i+=1; fw.append(loop[i%N])
        acc=0; i=mid
        while acc<half: acc+=math.dist(loop[i%N],loop[(i-1)%N]); i-=1; bw.append(loop[i%N])
        return list(reversed(bw))[:-1]+fw      # zaokruzeno, u smeru kazaljke
    def mid_insert(loop,i):      # dodaje tacku na sredini duzi izmedju i-1 i i
        a,b=loop[i-1],loop[i%len(loop)]; return loop[:i]+[((a[0]+b[0])/2,(a[1]+b[1])/2)]+loop[i:]
    loop=hexloop(R_TXT_TOP,RC); n=len(loop)//6
    loop=mid_insert(loop,5*n)
    top=window(loop,5*n,170)
    d_top,_=text_path(SANS,"PROIZVEDENO U SRCU SRBIJE",13,1.6,0,0,"path",top,arclen(top)/2)
    parts.append(f'<path d="{d_top}" fill="{color}"/>')
    loop=mid_insert(hexloop(R_TXT_BOT,RC),2*n)
    bot=list(reversed(window(loop,2*n,150)))   # s leva na desno
    d_bot,_=text_path(SANS,"DOMAĆEG POREKLA",13,3.0,0,0,"path",bot,arclen(bot)/2)
    parts.append(f'<path d="{d_bot}" fill="{color}"/>')
    # sredina: Srpski (pismo) + PROIZVOD
    d_sr,w=text_path(SCRIPT,"Srpski",120,0,200,222,"flat")
    sc=min(1.0,250/w)
    parts.append(f'<g transform="translate(200 0) scale({sc}) translate(-200 0)"><path d="{d_sr}" fill="{color}"/></g>')
    d_pv,wp=text_path(SANS,"PROIZVOD",19,6,200,268,"flat")
    parts.append(f'<path d="{d_pv}" fill="{color}"/>')
    parts.append(f'<line x1="{200-wp/2-26}" x2="{200-wp/2-8}" y1="261" y2="261" stroke="{color}" stroke-width="1.6"/><line x1="{200+wp/2+8}" x2="{200+wp/2+26}" y1="261" y2="261" stroke="{color}" stroke-width="1.6"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="800" height="800">\n'+"\n".join(parts)+"\n</svg>\n"

for name,col in (("tamna","#3e2412"),("svetla","#fbf1d6")):
    open(os.path.join(HERE,f"srpski-proizvod-sace-{name}.svg"),"w",encoding="utf-8").write(build(col))
print("ok")
