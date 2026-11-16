G1,G2,K='#69b529','#006633','#1a1a1a'
def defs(p):
    return (f'<defs><linearGradient id="{p}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{G1}"/><stop offset="1" stop-color="{G2}"/></linearGradient>'
            f'<linearGradient id="{p}d" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#333"/><stop offset="1" stop-color="{K}"/></linearGradient>'
            f'<filter id="{p}s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#1a1a1a" flood-opacity=".22"/></filter></defs>')
def bg(w,h,c='#edf3e8'):
    return f'<rect width="{w}" height="{h}" fill="{c}"/><circle cx="{w*.86:.0f}" cy="{h*.12:.0f}" r="{h*.46:.0f}" fill="{G1}" opacity=".16"/><circle cx="{w*.06:.0f}" cy="{h*1.05:.0f}" r="{h*.38:.0f}" fill="{G2}" opacity=".1"/>'
def R(x,y,w,h,f,rx=0,o=1,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" opacity="{o}" {extra}/>'
def C(x,y,r,f,o=1,extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" opacity="{o}" {extra}/>'
def L(d,s,w=3,o=1,extra=''):
    return f'<path d="{d}" fill="none" stroke="{s}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{o}" {extra}/>'
def sh(p,inner): return f'<g filter="url(#{p}s)">{inner}</g>'
HEART='M0 4C0-3 8-3 8 3 8-3 16-3 16 4 16 12 8 17 8 17S0 12 0 4Z'
def svg(p,w,h,body,label,style='display:block;width:100%;height:100%',slice_=True):
    par='xMidYMid slice' if slice_ else 'xMidYMid meet'
    return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="{par}" style="{style}" role="img" aria-label="{label}">{defs(p)}{bg(w,h)}{body}</svg>'
def marketing():
    p='m'; b=sh(p,R(36,30,250,170,'#fff',14))
    b+=C(54,46,3.5,'#d6d6d6')+C(66,46,3.5,'#d6d6d6')+C(78,46,3.5,'#d6d6d6')+R(96,42,90,8,'#e4e4e4',4)
    for i,hh in enumerate([40,62,50,88,110]):
        b+=R(56+i*38,186-hh,24,hh,f'url(#{p}g)' if i==4 else ['#c9e1b2','#b3d794','#c9e1b2','#9fcf74'][i],6)
    b+=L('M68 140L106 118L144 128L182 98L220 70',K,3)+''.join(C(x,y,4.5,'#fff',1,f'stroke="{K}" stroke-width="2"') for x,y in [(68,140),(106,118),(144,128),(182,98),(220,70)])
    b+=sh(p,R(262,118,116,96,'#fff',14))+C(300,166,22,'none',1,'stroke="#e6efe0" stroke-width="9"')+C(300,166,22,'none',1,f'stroke="url(#{p}g)" stroke-width="9" stroke-dasharray="96 138" stroke-linecap="round" transform="rotate(-90 300 166)"')
    b+=R(334,152,32,7,K,3.5,.85)+R(334,166,24,6,'#ccc',3)+R(334,180,28,6,'#ccc',3)
    b+=sh(p,C(334,60,28,'#fff'))+C(334,60,19,'none',1,f'stroke="{G1}" stroke-width="5"')+C(334,60,8,G2)+L('M334 60L360 34',K,3)+L('M352 32L362 32L362 42',K,3)
    return svg(p,400,240,b,'Marketing irányítópult mockup')
def grafika():
    p='g'; b=f'<g transform="rotate(-10 150 130)">{sh(p,R(70,70,190,110,f"url(#{p}g)",10))}{R(88,90,40,40,"#fff",8,.2)}{R(88,146,110,7,"#fff",3.5,.8)}{R(88,160,70,6,"#fff",3,.5)}</g>'
    b+=f'<g transform="rotate(6 215 140)">{sh(p,R(120,84,190,110,"#fff",10))}{C(150,114,13,G1)}{C(164,114,13,G2,.9)}{R(140,144,92,8,K,4,.85)}{R(140,159,122,5,"#bbb",2.5)}{R(140,171,100,5,"#ccc",2.5)}</g>'
    for i,c in enumerate([G1,G2,K,'#fff']): b+=C(356,50+i*34,12,c,1,'stroke="#1a1a1a" stroke-opacity=".25" stroke-width="1.5"')
    b+=L('M20 214C80 168 140 232 210 196',K,3)+R(14,208,12,12,'#fff',2,1,f'stroke="{K}" stroke-width="2"')+R(204,190,12,12,'#fff',2,1,f'stroke="{K}" stroke-width="2"')
    return svg(p,400,240,b,'Arculat és névjegykártya mockup')
def video():
    p='v'; b=sh(p,R(60,24,280,164,f'url(#{p}d)',12))
    b+=R(70,34,260,122,f'url(#{p}g)',6)+f'<path d="M70 156L130 100 170 132 220 84 330 156Z" fill="{G2}" opacity=".85"/>'+C(292,66,16,'#fff',.85)
    b+=C(200,96,26,'#fff',.92)+f'<path d="M192 84l22 12-22 12z" fill="{G2}"/>'
    b+=R(70,168,260,6,'#444',3)+R(70,168,112,6,G1,3)+C(182,171,6,'#fff')+R(180,188,40,16,'#cfcfcf')+R(150,203,100,8,'#bdbdbd',4)
    b+=f'<g transform="rotate(-8 340 200)">{sh(p,R(300,172,72,48,K,6))}{R(300,158,72,16,"#fff",3)}<path d="M308 158h12l-8 16h-12zM328 158h12l-8 16h-12zM348 158h12l-8 16h-12z" fill="{G1}"/>{R(310,186,40,5,"#fff",2.5,.8)}{R(310,198,28,5,"#fff",2.5,.5)}</g>'
    return svg(p,400,240,b,'Videó lejátszó és klapp mockup')
def web():
    p='w'; b=sh(p,R(30,28,280,182,'#fff',12))+R(30,28,280,24,'#f0f0f0',12)+R(30,40,280,12,'#f0f0f0')
    b+=C(46,40,3.5,'#e57373')+C(58,40,3.5,'#f2c14e')+C(70,40,3.5,G1)+R(88,34,150,12,'#fff',6)
    b+=R(42,62,256,62,f'url(#{p}g)',8)+R(56,74,100,9,'#fff',4.5,.95)+R(56,90,140,6,'#fff',3,.6)+R(56,104,48,12,K,6)+C(262,92,22,'#fff',.15)
    for i in range(3): b+=R(42+i*88,134,80,64,'#f2f2f2',8)+R(50+i*88,142,24,24,[G1,G2,K][i],6)+R(50+i*88,172,60,6,'#bbb',3)+R(50+i*88,184,40,5,'#ddd',2.5)
    b+=sh(p,R(284,64,90,164,K,16))+R(290,72,78,148,'#fff',11)+R(290,72,78,48,f'url(#{p}g)',11)+R(290,100,78,20,f'url(#{p}g)')+R(298,128,48,6,K,3,.8)+R(298,140,62,5,'#bbb',2.5)+R(298,152,34,22,'#f0f0f0',5)+R(336,152,26,22,'#f0f0f0',5)+R(318,66,28,4,'#444',2)
    return svg(p,400,240,b,'Reszponzív weboldal mockup')
def hosting():
    p='h'; b=''
    for i in range(3):
        y=38+i*54; b+=sh(p,R(36,y,196,44,f'url(#{p}d)',8))+C(54,y+22,5,G1)+C(70,y+22,5,G1 if i!=1 else '#666')+R(90,y+16,110,5,'#666',2.5)+R(90,y+26,80,5,'#555',2.5)+R(208,y+12,14,20,'#222',3)
    b+=L('M232 60C250 60 262 66 278 74',G2,3,.8,'stroke-dasharray="5 5"')+L('M232 114C256 114 268 112 278 100',G2,3,.8,'stroke-dasharray="5 5"')
    b+=sh(p,f'<path d="M290 96a22 22 0 0 1 4-43 30 30 0 0 1 56-4 24 24 0 0 1 12 47z" fill="url(#{p}g)"/>')+L('M310 76l10 10 20-22','#fff',4)
    b+=sh(p,R(262,116,116,92,'#fff',14))+C(290,146,14,G1)+L('M283 146l5 5 9-10',K,3)+R(312,138,52,7,K,3.5,.85)+R(312,152,36,6,'#ccc',3)+R(274,174,92,8,'#e6efe0',4)+R(274,174,70,8,f'url(#{p}g)',4)+R(274,190,56,6,'#ccc',3)
    return svg(p,400,240,b,'Szerver és felhő tárhely mockup')
def social():
    p='s'; b=sh(p,R(140,12,120,218,K,22))+R(146,22,108,198,'#fff',15)+C(162,40,8,f'url(#{p}g)')+R(176,34,60,6,K,3,.8)+R(176,44,38,5,'#bbb',2.5)
    b+=R(152,56,96,78,f'url(#{p}g)',6)+f'<path d="M152 134L186 96 208 116 232 88 248 106V134Z" fill="{G2}" opacity=".85"/>'+C(228,72,9,'#fff',.85)
    b+=f'<g transform="translate(154 142)"><path d="{HEART}" fill="{G1}"/></g>'+C(186,150,7,'none',1,f'stroke="{K}" stroke-width="2"')+L('M206 144l14 6-14 6z',K,2)
    b+=R(152,170,92,6,K,3,.55)+R(152,182,64,6,'#ccc',3)+R(152,198,92,12,'#f0f0f0',6)
    b+=sh(p,R(30,56,100,42,'#fff',14))+C(52,77,12,G1)+f'<g transform="translate(46 70) scale(.85)"><path d="{HEART}" fill="#fff"/></g>'+R(70,68,50,6,K,3,.8)+R(70,80,34,5,'#bbb',2.5)
    b+=sh(p,R(266,128,106,46,K,14))+R(280,142,70,7,'#fff',3.5,.9)+R(280,156,44,7,G1,3.5)
    b+=sh(p,C(352,60,22,G1))+f'<g transform="translate(344 52) scale(1)"><path d="{HEART}" fill="#fff"/></g>'
    return svg(p,400,240,b,'Közösségi média poszt telefonon')
def bus():
    p='b'; b=R(0,40,400,150,'#dcebd0',0,.6)+''.join(R(20+i*60,70-(i*13%30),40,120,'#cfe3bd',3,.9) for i in range(7))
    b+=R(0,188,400,52,'#2b2b2b')+''.join(R(10+i*60,212,30,4,'#fff',2,.8) for i in range(7))
    b+=sh(p,R(26,62,348,124,'#fff',16))+R(26,62,348,14,'#f0f0f0',7)
    for i in range(6): b+=R(44+i*42,82,34,22,'#cfe3f0',4)
    b+=R(318,82,48,60,'#cfe3f0',6)+R(311,82,2,100,'#ddd')
    b+=R(40,110,262,50,f'url(#{p}g)',6)+R(52,120,120,9,'#fff',4.5)+R(52,136,84,6,'#fff',3,.7)+R(52,147,50,8,K,4)+C(262,135,26,'#fff',.15)+R(242,126,46,10,'#fff',5,.9)
    b+=R(318,150,48,6,G1,3)+R(358,160,12,10,'#ffd54f',3)+R(300,72,50,8,K,4,.85)
    for x in (92,300): b+=C(x,186,22,K)+C(x,186,10,'#bbb')+C(x,186,4,K)
    return svg(p,400,240,b,'Buszreklám mockup – autóbusz oldalán reklámfelület')
def billboard():
    p='r'; b=R(0,206,400,34,'#cfe0c2')+R(124,130,12,80,'#8a8a8a',2)+R(252,130,12,80,'#8a8a8a',2)+R(108,24,170,6,'#555',3)+''.join(R(118+i*52,28,10,6,'#ffd54f',2) for i in range(4))
    b+=sh(p,R(50,36,280,106,K,8))+R(58,44,264,90,f'url(#{p}g)',4)+R(74,60,120,16,'#fff',6)+R(74,84,86,8,'#fff',4,.7)+R(74,102,58,18,K,9)+C(272,86,34,'#fff',.18)+C(272,86,18,'#fff',.28)
    b+=sh(p,R(334,66,56,134,'#fff',6))+R(340,74,44,100,f'url(#{p}d)',3)+R(346,82,32,34,f'url(#{p}g)',2)+R(346,122,28,5,'#fff',2.5,.8)+R(346,132,20,5,'#fff',2.5,.5)+R(332,196,60,8,'#bbb',3)+R(354,66,16,4,'#999',2)
    return svg(p,400,240,b,'Óriásplakát és citylight mockup')
def nyomda():
    p='n'; b=f'<g transform="rotate(-14 140 130)">{sh(p,R(70,34,116,160,G2,6))}</g><g transform="rotate(-5 140 130)">{sh(p,R(82,30,116,160,G1,6))}</g>'
    b+=sh(p,R(96,26,116,160,'#fff',6))+R(108,40,56,56,f'url(#{p}g)',8)+R(108,108,90,7,K,3.5,.75)+R(108,122,78,6,'#bbb',3)+R(108,134,84,6,'#ccc',3)+R(108,164,40,12,K,6)
    b+=sh(p,R(300,36,64,150,'#fff',4))+R(300,36,64,62,f'url(#{p}g)',4)+R(310,108,44,6,K,3,.8)+R(310,120,32,5,'#bbb',2.5)+R(310,150,44,16,G1,8)+R(290,186,84,10,'#9a9a9a',4)
    for i,c in enumerate(['#00aeef','#ec008c','#ffd800',K]): b+=C(36+i*22,214,8,c)
    b+=L('M12 12h18M12 12v18M388 228h-18M388 228v-18',K,2,.6)+C(250,196,16,'none',1,f'stroke="{K}" stroke-width="2" stroke-opacity=".5"')+L('M250 176v40M230 196h40',K,2,.5)
    return svg(p,400,240,b,'Nyomtatott kiadványok és roll-up mockup')
def tuke():
    p='t'; b=f'<g transform="rotate(8 250 120)">{sh(p,R(170,50,200,124,"#fff",14))}{R(186,66,60,60,"#f0f0f0",6)}'+''.join(R(192+(i%4)*14,72+(i//4)*14,10,10,K,2) for i in range(16))+f'{R(262,70,92,8,K,4,.8)}{R(262,86,70,6,"#bbb",3)}'+''.join(R(190+i*6,140,3+(i%3),24,K,0,.8) for i in range(24))+'</g>'
    b+=f'<g transform="rotate(-10 150 140)">{sh(p,R(40,76,210,130,f"url(#{p}g)",14))}{R(60,98,38,30,"#ffd54f",6)}{R(60,112,38,2,"#c9a227")}{R(78,98,2,30,"#c9a227")}'+f'<text x="60" y="170" font-family="Montserrat,Inter,sans-serif" font-weight="800" font-size="22" fill="#fff" letter-spacing="1.5">TÜKE</text><text x="60" y="188" font-family="Inter,sans-serif" font-weight="600" font-size="10" fill="#fff" opacity=".85" letter-spacing="1.2">KÁRTYA</text>'+L('M212 98a14 14 0 0 1 0 22M220 92a22 22 0 0 1 0 34','#fff',3,.9)+'</g>'
    b+=C(364,36,14,G1)+f'<path d="M364 29l2.2 4.8 5.2.6-3.9 3.5 1.1 5.2-4.6-2.7-4.6 2.7 1.1-5.2-3.9-3.5 5.2-.6z" fill="#fff"/>'
    return svg(p,400,240,b,'Tüke Kártya hűségkártya mockup')
def hero_mock():
    p='x'; w,h=520,380
    b=sh(p,R(10,10,420,270,'#232323',16))+R(10,10,420,28,'#2e2e2e',16)+R(10,26,420,12,'#2e2e2e')+C(30,24,4,'#e57373')+C(44,24,4,'#f2c14e')+C(58,24,4,G1)+R(80,17,160,14,'#1a1a1a',7)
    b+=R(10,38,420,242,K,0)+R(10,262,420,18,'#1a1a1a',0)+R(30,60,60,6,'#fff',3,.5)+R(250,56,48,10,'#2e2e2e',5)+R(304,56,48,10,'#2e2e2e',5)+R(358,52,52,18,f'url(#{p}g)',9)
    b+=R(30,110,210,26,'#fff',6)+R(30,146,180,16,G1,5,.9)+R(30,176,160,7,'#fff',3.5,.5)+R(30,190,130,7,'#fff',3.5,.4)+R(30,214,70,20,f'url(#{p}g)',10)
    b+=L('M230 280C270 230 330 230 430 150',G1,6)+L('M230 290C275 242 335 242 430 164',G2,4,.7)
    b+=sh(p,R(360,92,150,264,K,26))+R(368,102,134,244,'#fff',19)+R(368,102,134,70,f'url(#{p}g)',19)+R(368,150,134,22,f'url(#{p}g)')+R(380,184,60,7,K,3.5,.85)+R(380,198,100,6,'#bbb',3)
    for i in range(2): b+=R(380+i*58,216,52,52,'#f0f0f0',8)+C(406+i*58,236,10,[G1,G2][i])+R(388+i*58,254,36,5,'#bbb',2.5)
    b+=R(380,278,110,8,'#e6efe0',4)+R(380,278,70,8,f'url(#{p}g)',4)+R(420,98,30,5,'#444',2.5)
    b+=sh(p,R(30,250,140,86,'#fff',14))+R(44,264,60,7,K,3.5,.85)+''.join(R(46+i*20,322-[20,36,28,48][i],12,[20,36,28,48][i],G1 if i==3 else '#bfdca3',3) for i in range(4))
    b+=sh(p,R(180,288,132,44,'#fff',14))+C(204,310,12,G1)+f'<g transform="translate(198 303) scale(.8)"><path d="{HEART}" fill="#fff"/></g>'+R(224,302,70,6,K,3,.8)+R(224,314,46,5,'#bbb',2.5)
    return f'<svg viewBox="0 0 {w} {h}" style="display:block;width:100%;height:auto" role="img" aria-label="Weboldal, mobilalkalmazás és statisztika mockup">{defs(p)}{b}</svg>'
def desk():
    p='d'; b=R(0,170,400,70,'#d9c9b0',0,.0)+R(0,190,400,50,'#cfe0c2')
    b+=sh(p,R(70,50,220,132,K,10))+R(78,58,204,116,'#fff',4)+R(78,58,204,18,'#f0f0f0',4)+C(90,67,3,'#e57373')+C(100,67,3,'#f2c14e')+C(110,67,3,G1)
    b+=R(90,86,80,50,f'url(#{p}g)',6)+R(180,88,90,8,K,4,.8)+R(180,102,70,6,'#bbb',3)+R(180,114,80,6,'#ccc',3)+R(90,146,50,16,K,8)+R(150,146,60,16,'#e6efe0',8)
    b+=R(50,182,260,10,'#bdbdbd',5)+R(120,180,120,6,'#9a9a9a',3)
    b+=sh(p,R(316,128,52,60,'#fff',8))+R(316,128,52,12,G1,8)+R(316,134,52,6,G1)+R(326,150,32,5,'#bbb',2.5)+R(326,162,24,5,'#ccc',2.5)
    b+=sh(p,R(318,64,44,50,'#fff',6))+R(318,64,44,50,'none',6)+R(326,74,28,6,K,3,.8)+R(326,86,20,5,'#bbb',2.5)+L('M330 40C326 30 338 26 334 16','#9a9a9a',3,.7)+L('M346 40C342 30 354 26 350 16','#9a9a9a',3,.7)
    b+=f'<g transform="rotate(-18 36 160)">{R(14,150,46,10,G2,4)}{R(14,150,10,10,G1,4)}</g>'
    return svg(p,400,240,b,'Munkaasztal laptoppal és jegyzetekkel')
def step(i):
    p=f'q{i}'; w,h=320,220; b=''
    if i==0:
        b+=sh(p,R(90,16,140,190,'#fff',10))+R(120,8,80,18,K,8)
        for j in range(4): b+=R(106,48+j*36,16,16,f'url(#{p}g)' if j<3 else '#fff',4,1,f'stroke="{G2}" stroke-width="2"')+R(132,52+j*36,70,6,K,3,.75)+R(132,64+j*36,48,5,'#ccc',2.5)
        b+=L('M112 56l4 4 8-9','#fff',2.5)+L('M112 92l4 4 8-9','#fff',2.5)+L('M112 128l4 4 8-9','#fff',2.5)
        b+=sh(p,R(236,40,70,40,'#fff',12))+R(246,52,50,5,K,2.5,.7)+R(246,62,34,5,'#bbb',2.5)+f'<g transform="rotate(35 60 150)">{R(40,140,90,12,G1,4)}<path d="M130 140l14 6-14 6z" fill="{K}"/></g>'
    elif i==1:
        b+=sh(p,R(30,30,210,150,'#fff',12))+''.join(R(52+j*38,150-v,24,v,f'url(#{p}g)' if j==3 else '#c9e1b2',5) for j,v in enumerate([40,64,50,92,72]))+L('M64 112L102 90L140 100L178 66L216 80',K,3)
        b+=C(232,128,42,'#fff',.55,f'stroke="{K}" stroke-width="10"')+L('M262 158L298 194',K,12)
    elif i==2:
        b+=sh(p,R(30,24,250,38,'#fff',19))+C(56,43,9,'none',1,f'stroke="{K}" stroke-width="3"')+L('M63 50l8 8',K,3)+R(82,38,120,8,'#ccc',4)
        for j in range(3): b+=sh(p,R(30+j*88,84,78,110,'#fff',12))+C(69+j*88,114,16,[G1,G2,K][j])+R(48+j*88,142,42,6,K,3,.75)+R(48+j*88,156,30,5,'#bbb',2.5)+R(48+j*88,172,42,10,'#e6efe0',5)
    elif i==3:
        b+=sh(p,R(36,22,200,160,'#fff',10))+R(36,22,200,20,'#f0f0f0',10)+R(36,32,200,10,'#f0f0f0')+R(50,54,172,40,'#e6efe0',6,1,f'stroke="{G2}" stroke-width="2" stroke-dasharray="6 5"')+R(50,104,52,60,'#f2f2f2',6,1,'stroke="#9a9a9a" stroke-width="2" stroke-dasharray="6 5"')+R(110,104,52,60,'#f2f2f2',6,1,'stroke="#9a9a9a" stroke-width="2" stroke-dasharray="6 5"')+R(170,104,52,60,'#f2f2f2',6,1,'stroke="#9a9a9a" stroke-width="2" stroke-dasharray="6 5"')
        b+=f'<g transform="rotate(40 270 120)">{R(210,112,90,14,G1,3)}<path d="M300 112l16 7-16 7z" fill="{K}"/>{R(210,112,14,14,K,3)}</g>'+R(250,170,56,10,'#d6c28a',2)
    elif i==4:
        b+=sh(p,R(30,20,230,140,'#fff',8))+R(44,34,110,12,K,4,.85)+R(44,54,80,7,'#bbb',3.5)+''.join(R(44+j*30,140-v,20,v,f'url(#{p}g)' if j==4 else '#c9e1b2',4) for j,v in enumerate([20,34,28,50,70]))+C(220,70,28,'none',1,f'stroke="url(#{p}g)" stroke-width="12" stroke-dasharray="110 176" transform="rotate(-90 220 70)"')+R(130,160,6,40,'#8a8a8a',2)+R(100,198,66,8,'#8a8a8a',4)
        b+=sh(p,C(284,150,24,G1))+L('M274 150h20M286 142l8 8-8 8','#fff',3.5)
    elif i==5:
        for j,(x,wv) in enumerate([(70,.3),(130,.7),(190,.5)]):
            y=50+j*38; b+=R(40,y,150,8,'#d9e6cf',4)+R(40,y,150*wv,8,f'url(#{p}g)',4)+C(40+150*wv,y+4,10,'#fff',1,f'stroke="{G2}" stroke-width="3"')
        b+=sh(p,C(250,110,44,'#fff'))+C(250,110,28,'none',1,f'stroke="{K}" stroke-width="12" stroke-dasharray="7 6.4"')+C(250,110,22,'none',1,f'stroke="{K}" stroke-width="6"')+C(250,110,9,G1)+L('M52 176h140',K,3,.0)
        b+=sh(p,R(40,168,110,30,'#fff',15))+C(58,183,8,G1)+R(74,179,60,6,K,3,.7)+R(74,189,36,4,'#bbb',2)
    elif i==6:
        b+=sh(p,R(40,24,240,172,'#fff',14))+L('M80 140A60 60 0 0 1 240 140','#e6efe0',16)+L('M80 140A60 60 0 0 1 200 96',f'url(#{p}g)',16)+L('M160 140L200 96',K,5)+C(160,140,9,K)
        for j in range(3): b+=R(60+j*70,160,58,24,'#f2f2f2',6)+R(66+j*70,168,28,5,K,2.5,.8)
    else:
        b+=sh(p,R(40,108,60,88,f'url(#{p}g)',8))+sh(p,R(106,76,60,120,'#9fcf74',8))+sh(p,R(172,140,60,56,'#c9e1b2',8))+R(60,126,20,6,'#fff',3,.8)+R(126,94,20,6,'#fff',3,.8)
        b+=sh(p,f'<path d="M250 40h50v26a25 25 0 0 1-50 0z" fill="{G1}"/>')+R(268,92,14,22,G1,2)+R(256,114,38,10,G2,4)+L('M250 48h-12a14 14 0 0 0 14 24',G1,5)+L('M300 48h12a14 14 0 0 1-14 24',G1,5)+f'<path d="M275 50l3.5 7 7.5 1-5.5 5 1.5 7.500-7-4-7 4 1.500-7.500-5.500-5 7.500-1z" fill="#fff"/>'
    return svg(p,w,h,b,['Brief checklist','Elemzés grafikon nagyítóval','Kutatás: célközönség kártyák','Tervezés: drótváz vázlat','Prezentáció kivetítőn','Optimalizálás: csúszkák és fogaskerék','Mérés: műszer és mutatók','Eredmények: oszlopok és serleg'][i],'display:block;width:100%;height:100%',False)
