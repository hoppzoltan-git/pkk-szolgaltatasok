G1,G2,K='#69b529','#006633','#1a1a1a'
def R(x,y,w,h,f,rx=0,o=1,e=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" opacity="{o}" {e}/>'
def C(x,y,r,f,o=1,e=''): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" opacity="{o}" {e}/>'
def E(x,y,rx,ry,f,o=1,e=''): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{f}" opacity="{o}" {e}/>'
def P(d,f,o=1,e=''): return f'<path d="{d}" fill="{f}" opacity="{o}" {e}/>'
def L(d,s,w=3,o=1,e=''): return f'<path d="{d}" fill="none" stroke="{s}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{o}" {e}/>'
def T(x,y,t,sz,f='#fff',w=800,e='',fam='Montserrat,Inter,sans-serif'): return f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{w}" font-size="{sz}" fill="{f}" {e}>{t}</text>'
def G(t,body): return f'<g transform="{t}">{body}</g>'
def defs(p):
    return (f'<defs>'
    f'<linearGradient id="{p}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7fc83a"/><stop offset="1" stop-color="{G2}"/></linearGradient>'
    f'<linearGradient id="{p}gv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fc83a"/><stop offset="1" stop-color="{G2}"/></linearGradient>'
    f'<linearGradient id="{p}al" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9ebed"/><stop offset=".5" stop-color="#c6c9cd"/><stop offset="1" stop-color="#a9adb2"/></linearGradient>'
    f'<linearGradient id="{p}bk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b2c2e"/><stop offset="1" stop-color="#0d0d0e"/></linearGradient>'
    f'<linearGradient id="{p}gl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset=".45" stop-color="#fff" stop-opacity=".08"/><stop offset=".46" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    f'<linearGradient id="{p}pp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e9e9e4"/></linearGradient>'
    f'<radialGradient id="{p}st" cx=".35" cy=".25" r=".95"><stop offset="0" stop-color="#fbfbf9"/><stop offset=".6" stop-color="#e4e6e1"/><stop offset="1" stop-color="#b9bdb6"/></radialGradient>'
    f'<radialGradient id="{p}dk" cx=".4" cy=".3" r=".95"><stop offset="0" stop-color="#46504a"/><stop offset=".6" stop-color="#1d201e"/><stop offset="1" stop-color="#0a0b0a"/></radialGradient>'
    f'<radialGradient id="{p}vg" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".38"/></radialGradient>'
    f'<linearGradient id="{p}sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ec7e6"/><stop offset=".7" stop-color="#f3e7d3"/><stop offset="1" stop-color="#f0d9b8"/></linearGradient>'
    f'<linearGradient id="{p}dsk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c3550"/><stop offset=".6" stop-color="#b5645a"/><stop offset="1" stop-color="#f1b66f"/></linearGradient>'
    f'<filter id="{p}gr" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .55 -.18"/></filter>'
    f'<filter id="{p}wd" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".008 .28" numOctaves="3" seed="7"/><feColorMatrix type="matrix" values=".5 0 0 0 .52  .3 0 0 0 .33  .12 0 0 0 .17  0 0 0 0 1"/></filter>'
    f'<filter id="{p}b4"><feGaussianBlur stdDeviation="4"/></filter><filter id="{p}b10"><feGaussianBlur stdDeviation="10"/></filter><filter id="{p}b2"><feGaussianBlur stdDeviation="2"/></filter>'
    f'<filter id="{p}s" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#000" flood-opacity=".32"/></filter>'
    f'<filter id="{p}s2" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity=".3"/></filter>'
    f'</defs>')
def sh(p,x): return f'<g filter="url(#{p}s)">{x}</g>'
def sh2(p,x): return f'<g filter="url(#{p}s2)">{x}</g>'
def contact(cx,cy,rx,ry,o=.35,p=None): return E(cx,cy,rx,ry,'#000',o,f'filter="url(#{p}b10)"' if p else '')
def bg_studio(p,w,h): return R(0,0,w,h,f'url(#{p}st)')+R(0,h*.74,w,h*.26,'#c9ccc5')+R(0,h*.74,w,h*.26,'#000',0,.06)+L(f'M0 {h*.74} H{w}','#fff',2,.6)
def bg_wood(p,w,h): return R(0,0,w,h,'#6b4a2f')+R(0,0,w,h,'#000',0,1,f'filter="url(#{p}wd)"')+R(0,0,w,h,'#fff',0,.06)+E(w*.3,h*.2,w*.6,h*.5,'#fff',.14,f'filter="url(#{p}b10)"')
def bg_dark(p,w,h): return R(0,0,w,h,f'url(#{p}dk)')
def bokeh(p,w,h,cols,seed=1,n=14):
    out=''
    for i in range(n):
        x=(i*977+seed*131)%int(w); y=(i*613+seed*71)%int(h*.6); r=14+(i*37)%34
        out+=C(x,y,r,cols[i%len(cols)],.35,f'filter="url(#{p}b4)"')
    return out
def bg_dusk(p,w,h):
    b=R(0,0,w,h,f'url(#{p}dsk)')
    for i in range(9):
        x=i*w/8-20; hh=h*(.25+((i*53)%40)/100); b+=R(x,h*.72-hh,w/8+10,hh,'#12202e',0,.75,f'filter="url(#{p}b4)"')
        for j in range(5): b+=R(x+10+(j%2)*18,h*.72-hh+14+j*22,8,10,'#ffd9a0',2,.8,f'filter="url(#{p}b2)"')
    return b+R(0,h*.72,w,h*.28,'#262a2e')+R(0,h*.72,w,3,'#fff',.15)
def bg_day(p,w,h):
    b=R(0,0,w,h,f'url(#{p}sk)')
    for i in range(8):
        x=i*w/7-30; hh=h*(.22+((i*47)%35)/100); b+=R(x,h*.7-hh,w/7+10,hh,['#b9c4cc','#a9b6bf','#c8cfd3'][i%3],0,.85,f'filter="url(#{p}b4)"')
    return b+R(0,h*.7,w,h*.3,'#a7a9a3')+R(0,h*.7,w,4,'#fff',.35)
def finish(p,w,h): return R(0,0,w,h,'#000',0,.5,f'filter="url(#{p}gr)"')+R(0,0,w,h,f'url(#{p}vg)')
def scene(p,w,h,bg,body,label,slice_=True,style='display:block;width:100%;height:100%'):
    par='xMidYMid slice' if slice_ else 'xMidYMid meet'
    return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="{par}" style="{style}" role="img" aria-label="{label}">{defs(p)}{bg}{body}{finish(p,w,h)}</svg>'
def scr_web(p,w,h,title='Pécsi Kommunikációs Központ'):
    s=R(0,0,w,h,'#fff')+R(0,0,w,h*.1,'#fff')+R(w*.05,h*.03,w*.07,h*.045,f'url(#{p}g)',3)+''.join(R(w*(.5+i*.11),h*.045,w*.08,h*.015,'#9aa',2) for i in range(3))+R(w*.86,h*.028,w*.1,h*.05,f'url(#{p}g)',h*.025)
    s+=R(0,h*.1,w,h*.5,K)+R(0,h*.1,w,h*.5,f'url(#{p}dk)')+L(f'M{w*.45} {h*.1} C{w*.6} {h*.45} {w*.8} {h*.5} {w} {h*.55}',G1,w*.012)
    s+=T(w*.06,h*.3,'Full-service',w*.075,'#fff',800)+T(w*.06,h*.4,'marketing ügynökség',w*.04,G1,300)+R(w*.06,h*.46,w*.16,h*.06,f'url(#{p}g)',h*.03)
    for i in range(3): s+=R(w*.05+i*w*.31,h*.65,w*.28,h*.28,'#f3f3f1',8)+R(w*.07+i*w*.31,h*.68,w*.24,h*.12,[f'url(#{p}g)','#2b2b2b',f'url(#{p}gv)'][i],5)+R(w*.07+i*w*.31,h*.84,w*.14,h*.02,K,2,.7)+R(w*.07+i*w*.31,h*.88,w*.2,h*.015,'#aaa',2)
    return s
def scr_dash(p,w,h):
    s=R(0,0,w,h,'#f4f6f3')+R(0,0,w*.18,h,K)+''.join(R(w*.03,h*.12+i*h*.09,w*.12,h*.03,'#fff',3,.5 if i else 1) for i in range(5))+C(w*.045,h*.05,h*.025,G1)
    s+=T(w*.22,h*.09,'Kampány áttekintés',w*.03,K,700,'',"Inter,sans-serif")
    for i in range(3): s+=R(w*.22+i*w*.26,h*.14,w*.24,h*.17,'#fff',8)+R(w*.235+i*w*.26,h*.18,w*.1,h*.02,'#9a9',2)+R(w*.235+i*w*.26,h*.23,w*.14,h*.045,[G1,G2,K][i],3)
    s+=R(w*.22,h*.36,w*.5,h*.58,'#fff',8)+''.join(R(w*.25+i*w*.06,h*.88-hh,w*.035,hh,f'url(#{p}gv)' if i==7 else '#c9e1b2',3) for i,hh in enumerate([h*.12,h*.2,h*.16,h*.3,h*.26,h*.38,h*.34,h*.46]))
    s+=L(f'M{w*.26} {h*.7} L{w*.34} {h*.62} L{w*.4} {h*.66} L{w*.5} {h*.52} L{w*.58} {h*.55} L{w*.66} {h*.43}',K,2.5)
    s+=R(w*.75,h*.36,w*.21,h*.58,'#fff',8)+C(w*.855,h*.6,h*.12,'none',1,f'stroke="#e6efe0" stroke-width="{h*.04}"')+C(w*.855,h*.6,h*.12,'none',1,f'stroke="{G1}" stroke-width="{h*.04}" stroke-dasharray="{h*.5} {h*.3}" transform="rotate(-90 {w*.855} {h*.6})"')
    return s
def scr_video(p,w,h):
    s=R(0,0,w,h,f'url({"#"+p}dsk)')+P(f'M0 {h*.72} L{w*.2} {h*.5} L{w*.38} {h*.66} L{w*.58} {h*.38} L{w*.82} {h*.64} L{w} {h*.5} V{h} H0Z','#10202c',.85)+C(w*.76,h*.28,h*.07,'#ffe6b0',.95,f'filter="url(#{p}b4)"')
    s+=C(w*.5,h*.5,h*.1,'#fff',.9)+P(f'M{w*.5-h*.03} {h*.5-h*.05} L{w*.5+h*.06} {h*.5} L{w*.5-h*.03} {h*.5+h*.05}Z',K)
    s+=R(0,h*.9,w,h*.1,'#000',.55)+R(w*.04,h*.945,w*.92,h*.012,'#fff',.35,)+R(w*.04,h*.945,w*.38,h*.012,G1)+C(w*.42,h*.951,h*.014,'#fff')
    return s
def scr_feed(p,w,h,kind='ig'):
    s=R(0,0,w,h,'#fff')
    if kind=='in': s+=R(0,0,w,h*.08,'#fff')+T(w*.05,h*.055,'in',h*.04,G2,800)
    else: s+=R(0,0,w,h*.09,'#fff')+T(w*.05,h*.06,'Pécsi KK',h*.036,K,800)
    s+=C(w*.1,h*.15,w*.05,f'url(#{p}g)')+R(w*.18,h*.125,w*.3,h*.016,K,2,.8)+R(w*.18,h*.15,w*.2,h*.012,'#bbb',2)
    s+=R(0,h*.2,w,h*.4,f'url({"#"+p}dsk)')+P(f'M0 {h*.6} L{w*.3} {h*.42} L{w*.5} {h*.54} L{w*.75} {h*.36} L{w} {h*.52} V{h*.6}Z','#10202c',.85)+C(w*.78,h*.3,w*.07,'#ffe6b0',.9,f'filter="url(#{p}b2)"')
    s+=G(f'translate({w*.05} {h*.635}) scale({w/200})','<path d="M0 4C0-3 8-3 8 3 8-3 16-3 16 4 16 12 8 17 8 17S0 12 0 4Z" fill="#e0245e"/>')+C(w*.2,h*.655,w*.025,'none',1,f'stroke="{K}" stroke-width="1.6"')+R(w*.05,h*.7,w*.8,h*.014,K,2,.8)+R(w*.05,h*.73,w*.55,h*.012,'#bbb',2)
    s+=R(0,h*.78,w,h*.22,'#f6f6f4')+C(w*.1,h*.86,w*.05,G1)+R(w*.18,h*.84,w*.5,h*.014,K,2,.7)+R(w*.18,h*.87,w*.35,h*.012,'#bbb',2)
    return s
def phone(p,x,y,sc,content,rot=0):
    w,h=100,206
    b=f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">'
    b+=sh(p,R(0,0,w,h,'#1a1b1c',16))+R(1.5,1.5,w-3,h-3,f'url(#{p}bk)',15)+R(-1.5,48,2,22,'#444',1)+R(w-.5,64,2,34,'#444',1)
    b+=f'<g transform="translate(4 4)"><clipPath id="{p}pc{x}{y}"><rect width="92" height="198" rx="12"/></clipPath><g clip-path="url(#{p}pc{x}{y})">{content(92,198)}</g></g>'
    b+=R(34,8,32,9,'#000',4.5)+P(f'M4 4 H60 L10 200 H4Z',f'url(#{p}gl)',1,f'clip-path="url(#{p}pc{x}{y})"')+'</g>'
    return b
def laptop(p,cx,cy,sc,content,w=300,h=186):
    g=f'<g transform="translate({cx-w/2*sc} {cy-(h+16)*sc}) scale({sc})">'
    g+=contact(w/2,h+18,w*.62,10,.4,p)
    g+=sh(p,R(0,0,w,h,f'url(#{p}al)',12))+R(7,7,w-14,h-14,'#050505',6)
    g+=f'<g transform="translate(14 13)"><clipPath id="{p}lc{int(cx)}"><rect width="{w-28}" height="{h-26}" rx="2"/></clipPath><g clip-path="url(#{p}lc{int(cx)})">{content(w-28,h-26)}</g></g>'
    g+=P(f'M7 7 H{w*.55} L{w*.2} {h-7} H7Z',f'url(#{p}gl)',.8)
    g+=P(f'M-14 {h} H{w+14} L{w+6} {h+10} Q{w/2} {h+16} 6 {h+10}Z',f'url(#{p}al)')+R(w/2-26,h,52,4,'#8b8f94',2)+'</g>'
    return g
def monitor(p,cx,cy,sc,content,w=360,h=210):
    g=f'<g transform="translate({cx-w/2*sc} {cy-(h+56)*sc}) scale({sc})">'+contact(w/2,h+52,w*.35,8,.35,p)
    g+=sh(p,R(0,0,w,h,'#111',10))+f'<g transform="translate(8 8)"><clipPath id="{p}mc{int(cx)}"><rect width="{w-16}" height="{h-24}" rx="2"/></clipPath><g clip-path="url(#{p}mc{int(cx)})">{content(w-16,h-24)}</g></g>'
    g+=R(w*.4,h,w*.2,30,f'url(#{p}al)')+R(w*.3,h+28,w*.4,8,f'url(#{p}al)',4)+P(f'M8 8 H{w*.5} L{w*.25} {h-10} H8Z',f'url(#{p}gl)',.7)+'</g>'
    return g
def sheet(p,x,y,w,h,rot,content='',fill=None,shadow=True):
    f=fill or f'url(#{p}pp)'
    o=R(0,0,w,h,f,2)+content+P(f'M{w} {h} L{w-26} {h} L{w} {h-26}Z','#000',.06)
    o=sh2(p,o) if shadow else o
    return f'<g transform="translate({x} {y}) rotate({rot})">{o}</g>'
def bcard(p,x,y,w,h,rot,fill,content=''):
    return f'<g transform="translate({x} {y}) rotate({rot})">'+sh2(p,R(0,0,w,h,fill,3)+R(0,h-2,w,2,'#000',.18,0)+content+P(f'M0 0 H{w*.7} L0 {h*.6}Z','#fff',.1))+'</g>'
def mug(p,x,y,s=1,col='#fff'):
    return f'<g transform="translate({x} {y}) scale({s})">'+contact(40,66,50,9,.4,p)+R(0,0,80,66,col,10,1,'')+R(0,0,80,66,'#000',10,.0)+E(40,4,40,8,'#d9d9d6')+E(40,6,34,6,'#3b2416')+L('M80 18 C106 16 106 52 78 52',col,9)+R(6,6,12,52,'#fff',6,.5,f'filter="url(#{p}b2)"')+R(58,6,14,54,'#000',6,.1)+'</g>'
def plant(p,x,y,s=1):
    leaves=''.join(P(f'M0 0 C{-30+i*14} {-50-i*8} {-14+i*10} {-96} {i*8-6} {-110-i*6} C{14+i*6} {-70} {10} {-30} 0 0Z',[G2,'#2f8f3a','#1c6b3a'][i%3],.95) for i in range(6))
    return f'<g transform="translate({x} {y}) scale({s})">'+contact(0,4,44,8,.4,p)+leaves+P('M-30 0 H30 L24 -40 H-24Z','#d8d4ca')+R(-32,-44,64,8,'#cfcbc0',3)+'</g>'
def pen(p,x,y,rot,col=K):
    return f'<g transform="translate({x} {y}) rotate({rot})">'+sh2(p,R(0,0,120,9,col,4.5))+R(0,0,120,3,'#fff',2,.35)+P('M120 0 L136 4.5 L120 9Z','#e8cfa9')+'</g>'
def bag(p,x,y,s,col,logo=True):
    return f'<g transform="translate({x} {y}) scale({s})">'+contact(70,166,70,9,.4,p)+sh(p,P('M10 40 H130 L136 164 H4Z',col))+P('M10 40 H130 L136 164 H4Z','#000',.06)+L('M42 40 C42 -6 98 -6 98 40',col,7)+L('M42 40 C42 -4 98 -4 98 40','#000',2,.2)+(f'<circle cx="70" cy="100" r="22" fill="#fff"/><circle cx="64" cy="98" r="9" fill="{G1}"/><circle cx="77" cy="98" r="9" fill="{G2}" opacity=".9"/>' if logo else '')+P('M10 40 H130 L136 164 H4Z',f'url(#{p}gl)',.4)+'</g>'
def box(p,x,y,w,h,d,top,front,side,content=''):
    return (f'<g transform="translate({x} {y})">'+contact(w/2+d/2,h+d*.6,w*.7,9,.35,p)+sh(p,P(f'M0 {d} L{d} 0 H{w+d} L{w} {d}Z',top)+R(0,d,w,h,front)+P(f'M{w} {d} L{w+d} 0 V{h-d*0+0} L{w} {h+d}Z',side))+content+'</g>')
W,H=600,520
def sc_grafika(p='a1'):
    b=bg_wood(p,W,H)
    b+=sheet(p,40,40,240,320,-6,R(20,24,90,90,f'url(#{p}g)',10)+T(24,170,'Arculati',34,K,800)+T(24,206,'kézikönyv',34,G2,800)+R(24,236,140,5,'#bbb',2)+R(24,252,110,5,'#ccc',2))
    b+=sheet(p,300,60,150,210,5,R(0,0,150,210,f'url(#{p}gv)',2)+T(18,120,'Pécsi',24,'#fff',800)+T(18,148,'KK',24,'#fff',300))
    b+=bcard(p,250,360,170,100,-12,f'url(#{p}g)',C(34,34,14,'#fff',.9)+R(20,62,90,6,'#fff',3,.85)+R(20,76,60,5,'#fff',3,.5))
    b+=bcard(p,282,372,170,100,-4,'#fff',R(18,18,26,26,G1,5)+R(18,62,90,6,K,3,.8)+R(18,76,60,5,'#aaa',3))
    b+=bcard(p,320,384,170,100,5,K,C(30,30,12,G1)+R(18,62,90,6,'#fff',3,.8))
    for i,c in enumerate([G1,G2,K,'#fff','#d0d6c8']):
        b+=f'<g transform="translate({470+i*16} {150+i*6}) rotate({-14+i*7})">'+sh2(p,R(0,0,26,150,c,5))+R(4,8,18,30,'#fff',3,.35)+'</g>'
    b+=mug(p,40,410,1.0,'#e9e7e1')+pen(p,330,498,-4)
    return scene(p,W,H,'',b,'Arculati kézikönyv, névjegykártyák és színminták fa asztalon')
def sc_video(p='a2'):
    b=bg_dark(p,W,H)+bokeh(p,W,H,[G1,'#ffd9a0','#6ab0ff'],3)
    b+=monitor(p,300,400,1.25,lambda w,h:scr_video(p,w,h),360,210)
    tl=R(0,0,430,70,'#101112',8)+''.join(R(10+i*68,10,62,22,[G1,G2,'#2b6b8f','#c98b2b'][i%4],4,.9)+R(10+i*68,38,62,18,'#333',4) for i in range(6))+R(190,2,3,66,'#ff4d4d')
    b+=f'<g transform="translate(85 430)">'+sh2(p,tl)+'</g>'
    b+=f'<g transform="translate(480 330) rotate(-8)">'+sh2(p,R(0,0,90,70,'#1b1c1d',4)+P('M0 0 H90 L84 -22 H6Z','#2a2b2d')+''.join(P(f'M{i*22} -22 l10 0 l-8 22 h-10Z','#fff',.9) for i in range(4)))+'</g>'
    return scene(p,W,H,'',b,'Videóvágó monitor idővonallal és klapnival')
def sc_web(p='a3'):
    b=bg_studio(p,W,H)
    b+=monitor(p,260,360,1.0,lambda w,h:scr_web(p,w,h),360,210)
    b+=laptop(p,400,470,.78,lambda w,h:scr_dash(p,w,h),300,186)
    b+=phone(p,60,250,1.0,lambda w,h:scr_web(p,w,h),-4)
    b+=plant(p,545,440,.8)+mug(p,84,462,.5,'#fff')
    return scene(p,W,H,'',b,'Weboldal monitoron, laptopon és telefonon')
def sc_hosting(p='a4'):
    b=bg_dark(p,W,H)
    for k in range(3):
        x=40+k*180
        b+=sh(p,R(x,30,160,460,f'url(#{p}bk)',8))+R(x+8,38,144,444,'#050505',5)
        for j in range(9):
            y=48+j*48
            b+=R(x+12,y,136,38,'#202224',3)+R(x+12,y,136,2,'#fff',.12)+''.join(R(x+20+q*6,y+10,3,18,'#000',1,.6) for q in range(16))
            for q,c in enumerate([G1,G1,'#ffb020' if (j+k)%4==0 else G1]): b+=C(x+130+q*0,y+10+q*9,2.6,c)+C(x+130,y+10+q*9,6,c,.35,f'filter="url(#{p}b4)"')
    b+=E(300,500,300,18,G1,.12,f'filter="url(#{p}b10)"')
    b+=L('M20 500 H580',G1,2,.4)
    return scene(p,W,H,'',b,'Szerverszekrények zöld státuszfényekkel')
def sc_social(p='a5'):
    b=bg_studio(p,W,H)
    b+=phone(p,60,120,1.3,lambda w,h:scr_feed(p,w,h,'ig'),-6)
    b+=phone(p,230,70,1.5,lambda w,h:scr_feed(p,w,h,'fb'),0)
    b+=phone(p,430,130,1.3,lambda w,h:scr_feed(p,w,h,'in'),6)
    b+=C(205,90,26,'#e0245e')+G('translate(195 82) scale(1)','<path d="M0 4C0-3 8-3 8 3 8-3 16-3 16 4 16 12 8 17 8 17S0 12 0 4Z" fill="#fff"/>')
    b+=C(520,100,24,G1)+T(510,108,'+1k',13,'#fff',800)
    return scene(p,W,H,'',b,'Három telefon közösségi médiás posztokkal')
def sc_marketing(p='a6'):
    b=bg_wood(p,W,H)
    b+=laptop(p,300,400,1.25,lambda w,h:scr_dash(p,w,h),300,186)
    b+=sheet(p,30,300,170,200,-8,T(16,34,'Kampányterv',15,K,800)+''.join(R(16,52+i*22,120-i*10,6,'#bbb',3)+C(150,55+i*22,4,[G1,G2][i%2]) for i in range(6)))
    b+=mug(p,480,380,.9,'#f2f0ea')+plant(p,545,330,.7)+pen(p,60,500,-6,G2)
    return scene(p,W,H,'',b,'Laptop kampány dashboarddal, jegyzettel és kávéval')
def sc_reklam(p='a7'):
    b=bg_dusk(p,W,H)
    b+=R(296,300,16,170,'#1c1c1c')+R(240,300,128,14,'#1c1c1c')
    b+=sh(p,R(70,90,460,210,'#141414',6))+R(80,100,440,190,f'url(#{p}g)',3)
    b+=P('M80 290 L80 200 C180 170 260 260 360 200 C430 160 480 230 520 190 V290Z','#fff',.1)
    b+=T(110,180,'Hirdess',50,'#fff',800)+T(110,236,'Pécsen!',50,'#fff',300)+R(380,200,110,40,'#fff',20)+T(398,227,'Hívj',20,K,800)
    for i in range(7): b+=C(90+i*66,96,3,'#ffe6b0')+C(90+i*66,96,10,'#ffe6b0',.5,f'filter="url(#{p}b4)"')
    b+=P('M70 300 L530 300 L560 330 H40Z','#000',.3)
    return scene(p,W,H,'',b,'Óriásplakát naplementekor')
def sc_nyomda(p='a8'):
    b=bg_studio(p,W,H)
    b+=sheet(p,40,230,230,270,-5,R(0,0,230,120,f'url(#{p}g)',2)+T(18,168,'Katalógus',28,K,800)+R(18,190,150,5,'#bbb',2)+R(18,206,110,5,'#ccc',2))
    b+=sheet(p,70,200,220,260,3,R(0,0,220,110,K,2)+C(40,50,16,G1)+T(20,160,'Szórólap',26,K,800)+R(20,184,140,5,'#bbb',2))
    b+=box(p,300,290,140,110,36,'#e7d5b1','#d8c29a','#bda677',R(26,28,98,60,'#fff',4)+C(55,58,12,G1)+R(78,50,36,5,K,2)+R(78,62,26,5,'#999',2))
    b+=bag(p,440,250,.95,G2)+bag(p,510,290,.6,'#fff',True)
    b+=bcard(p,320,450,120,70,-6,'#fff',R(12,12,16,16,G1,4)+R(12,44,70,5,K,2))+bcard(p,350,455,120,70,4,G1)
    return scene(p,W,H,'',b,'Nyomtatott katalógus, szórólap, doboz és szatyrok')
SC={'grafika':sc_grafika,'video':sc_video,'web':sc_web,'hosting':sc_hosting,'social':sc_social,'marketing':sc_marketing,'reklam':sc_reklam,'nyomda':sc_nyomda}
def svgdoc(k,wide=False):
    return SC[k](),
