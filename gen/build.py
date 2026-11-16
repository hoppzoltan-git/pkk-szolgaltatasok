import art
BTN='display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 30px;border-radius:999px;font-size:13px;font-weight:800;letter-spacing:.06em;text-transform:uppercase'
GB=BTN+';background:linear-gradient(90deg,#69b529,#3fa534);color:#1a1a1a'
WB=BTN+';background:#fff;color:#006633'
PANEL='padding:56px;border-radius:32px;background:#f7f7f7'
H2='font-size:clamp(34px,5vw,64px);line-height:1.1;font-weight:800;color:#1a1a1a'
SOC='width:40px;height:40px;border-radius:50%;border:1px solid rgba(255,255,255,.4);display:inline-flex;align-items:center;justify-content:center;font-size:13px;font-weight:700'
LK='font-size:14px;color:rgba(255,255,255,.85)'
IN='height:44px;padding:0 16px;border-radius:8px;border:0;background:rgba(255,255,255,.1);color:#fff'
ARROW='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
EXT='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"></path></svg>'

services=[
 ('Marketing','MarketingManagement.dc.html',None,art.marketing(),'Stratégia, kampányok és mérhető eredmények.'),
 ('Grafika','Main.dc.html',None,art.grafika(),'Arculat, logó és minden vizuális kiadvány.'),
 ('Videókészítés','Videokeszites.dc.html',None,art.video(),'Imázsfilmek, reklámok és közösségi videók.'),
 ('Webfejlesztés','Webfejlesztes.dc.html',None,art.web(),'Gyors, reszponzív és könnyen kezelhető weboldalak.'),
 ('Webhosting','Webhosting.dc.html',None,art.hosting(),'Biztonságos tárhely és megbízható üzemeltetés.'),
 ('Social media management','SocialMedia.dc.html',None,art.social(),'Tartalomgyártás és közösségépítés a csatornáidon.'),
 ('Buszreklám','https://pecsibuszreklam.hu/','pecsibuszreklam.hu',art.bus(),'Mozgó reklámfelület Pécs közlekedési hálózatán.'),
 ('Reklámfelületek','Reklamfeluletek.dc.html',None,art.billboard(),'Óriásplakátok, citylightok és más kültéri felületek.'),
 ('Nyomdai gyártás','NyomdaiGyartas.dc.html',None,art.nyomda(),'Nyomtatott kiadványok a tervezéstől a kézbesítésig.'),
 ('Tüke Kártya','https://pecsitukekartya.hu/','pecsitukekartya.hu',art.tuke(),'Hűségkártya kedvezményekkel helyi partnereknél.'),
]
tiles=''
for name,href,ext,svg,desc in services:
    tgt=' target="_blank" rel="noopener"' if ext else ''
    extra=f'<span style="font-size:12px;font-weight:700;letter-spacing:.04em;color:#006633">{ext} ↗</span>' if ext else ''
    tiles+=(f'<a href="{href}"{tgt} style="flex:1 1 240px;display:flex;flex-direction:column;border-radius:24px;background:#f6f6f6;overflow:hidden">'
            f'<div style="height:240px;overflow:hidden">{svg.replace("height:100%","height:240px")}</div>'
            f'<div style="padding:18px 24px 24px;display:flex;flex-direction:column;gap:8px;flex:1"><div style="display:flex;align-items:center;justify-content:space-between;gap:12px"><h3 style="font-size:19px;line-height:1.2;font-weight:800;letter-spacing:.02em;text-transform:uppercase;color:#1a1a1a">{name}</h3><span style="flex:none;width:36px;height:36px;border-radius:50%;background:#69b529;display:inline-flex;align-items:center;justify-content:center" aria-hidden="true">{EXT if ext else ARROW}</span></div>'
            f'<p style="font-size:14px;line-height:1.55;color:rgba(26,26,26,.78)">{desc}</p>{extra}</div></a>')
footlinks=''.join(f'<a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if e else ""} style="{LK}">{n}</a>' for n,h,e,_,_ in services)

steps=[('Brief','Egyeztetünk veled: megismerjük a céljaidat, a cégedet és az elvárásaidat.'),
('Elemzés','Áttekintjük a jelenlegi helyzetet, a versenytársakat és a kínálkozó lehetőségeket.'),
('Kutatás','Megvizsgáljuk a célközönséget, a releváns csatornákat és a jó példákat.'),
('Tervezés','Kidolgozzuk a stratégiát, az ütemtervet és a költségkeretet.'),
('Prezentálás','Bemutatjuk a javaslatot, és közösen finomítjuk, amíg minden a helyére nem kerül.'),
('Optimalizálás','Elindítjuk a megvalósítást, és menet közben folyamatosan hangoljuk a működést.'),
('Mérés','Követjük az eredményeket, és rendszeresen beszámolunk a tapasztalatokról.'),
('Eredmények','Összegezzük a tanulságokat, és megtervezzük a következő lépéseket.')]
panels=''
steps=[]
for i,(t,tx) in enumerate(steps):
    panels+=(f'<div style="{{{{ps{i}}}}}" aria-hidden="{{{{pa{i}}}}}"><div style="display:flex;flex-wrap:wrap;align-items:center;gap:24px 32px"><div style="flex:1 1 220px;min-width:0;display:flex;flex-direction:column;gap:12px">'
             f'<span style="font-family:Montserrat,system-ui,sans-serif;font-size:72px;line-height:1;font-weight:800;color:#69b529">0{i+1}<span style="font-size:24px;color:#1a1a1a;opacity:.5"> / 08</span></span>'
             f'<h3 style="font-size:clamp(26px,3vw,38px);line-height:1.15;font-weight:800;color:#1a1a1a">{t}</h3><p style="font-size:16px;line-height:1.65;color:rgba(26,26,26,.82)">{tx}</p></div>'
             f'<div style="flex:1 1 260px;min-width:0;height:220px;border-radius:20px;overflow:hidden;background:#edf3e8">{art.step(i)}</div></div></div>')

HTML=open('tpl.html').read().replace('<<FOLYAMAT>>',open('folyamat.svg').read())
for k,v in {'BTN':BTN,'GB':GB,'WB':WB,'PANEL':PANEL,'H2':H2,'SOC':SOC,'LK':LK,'IN':IN,'TILES':tiles,'FOOTLINKS':footlinks,'PANELS':panels,'HEROMOCK':art.hero_mock(),'DESK':art.desk().replace('display:block;width:100%;height:100%','position:absolute;top:0;left:0;width:100%;height:100%')}.items():
    HTML=HTML.replace(f'<<{k}>>',v)
open('../src/Eredeti.dc.html','w').write(HTML)
print(len(HTML))
