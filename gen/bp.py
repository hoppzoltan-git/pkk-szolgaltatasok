import json, os, sys
sys.path.insert(0,'.')
from content import *
import art
OUT='../src/'
CSS='''body{margin:0}
*{box-sizing:border-box}
a{color:inherit;text-decoration:none}
h1,h2,h3,h4,p{margin:0}
h1,h2,h3,h4{font-family:Montserrat,system-ui,sans-serif}
dc-import{display:block}
summary::-webkit-details-marker{display:none}
.faq-i::before{content:"+"}
details[open] .faq-i::before{content:"–"}'''
FONT='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Montserrat:wght@500;600;700;800&amp;display=swap">'
def doc(title,body,script,h,extra_css=''):
    return f'''<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>
{CSS}{extra_css}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{h}}}}}'>
{script}
</script>
</body>
</html>
'''
def J(o): return json.dumps(o,ensure_ascii=False)
def crop(url,cx,cy,zoom,ar,r=0,extra=''):
    top=50-cy*zoom*0.8667*ar*100; left=50-cx*zoom*100
    return f'<div style="position:relative;width:100%;aspect-ratio:{ar:.3f};overflow:hidden;border-radius:{r}px;background:#1a1a1a;{extra}"><img src="{url}" alt="" style="position:absolute;width:{zoom*100:.0f}%;left:{left:.1f}%;top:{top:.1f}%;max-width:none;display:block"></div>'
BTN='display:inline-flex;align-items:center;min-height:52px;padding:0 34px;border-radius:999px;font-size:15px;font-weight:700'
KEY={v:k for k,v in NAMES.items()}
ARROW='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
CHECK='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def eyebrow(t,c='#006633'): return f'<span style="font-size:14px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:{c}">{t}</span>'
def h2(t,c='#1a1a1a'): return f'<h2 style="font-size:clamp(32px,4vw,52px);line-height:1.1;font-weight:800;color:{c}">{t}</h2>'
def page_hero():
    body=f'''<section style="position:relative;width:100%;min-height:640px;background:#1a1a1a;color:#fff;font-family:Inter,system-ui,sans-serif;display:flex;align-items:center;overflow:hidden">
<div style="position:absolute;top:0;right:0;bottom:0;left:0;background:radial-gradient(ellipse at 85% 40%,rgba(105,181,41,.28),rgba(26,26,26,0) 60%)" aria-hidden="true"></div>
<div style="position:relative;width:100%;max-width:1440px;margin:0 auto;padding:80px;display:flex;flex-wrap:wrap;align-items:center;gap:48px 64px">
<div style="flex:1 1 440px;min-width:0;display:flex;flex-direction:column;align-items:flex-start;gap:28px">
<nav style="display:flex;flex-wrap:wrap;gap:10px;font-size:14px;font-weight:500;color:#69b529">
<a href="#">Kezdőlap</a>
<sc-if value="{{{{sub}}}}" hint-placeholder-val="{{{{ true }}}}"><span aria-hidden="true">/</span><a href="#">Szolgáltatásaink</a></sc-if>
<span aria-hidden="true">/</span><span style="color:#fff">{{{{heading}}}}</span>
</nav>
<h1 style="font-size:clamp(44px,6vw,80px);line-height:1.02;font-weight:800;color:#fff;overflow-wrap:break-word;max-width:100%">{{{{heading}}}}</h1>
<span style="width:96px;height:8px;border-radius:4px;background:linear-gradient(90deg,#69b529,#006633);display:block" aria-hidden="true"></span>
<p style="font-size:20px;line-height:1.6;color:rgba(255,255,255,.85);max-width:560px">{{{{lead}}}}</p>
<div style="display:flex;flex-wrap:wrap;gap:16px">
<a href="mailto:marketing@pecsikommunikacio.hu" style="{BTN};background:#69b529;color:#1a1a1a">Árajánlatot kérek</a>
<a href="#portfolio" style="{BTN};border:2px solid #fff;color:#fff">Lapozz bele portfóliónkba</a>
</div></div>
<div style="flex:1 1 440px;min-width:0"><div style="width:100%;aspect-ratio:600/520;border-radius:32px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.12)"><img src="{{{{img}}}}" alt="{{{{heading}}}} mockup" style="width:100%;height:100%;display:block;object-fit:cover"></div></div>
</div>
</section>'''
    script=f'''class Component extends DCLogic {{
renderVals() {{
const U = {J(U)};
const N = {J(NAMES)};
const L = {J(LEAD)};
const k = this.props.page ?? "grafika";
return {{ heading: this.props.heading ?? N[k], lead: L[k], img: U[k], sub: this.props.index !== true }};
}}
}}'''
    return doc('Hero',body,script,640)
def intro_split():
    body=f'''<div style="width:100%;font-family:Inter,system-ui,sans-serif;color:#1a1a1a;background:#fff">
<section style="background:#fff"><div style="max-width:1440px;margin:0 auto;padding:96px 80px;display:flex;flex-direction:column;gap:56px">
<div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px 56px">
<div style="flex:1 1 480px;display:flex;flex-direction:column;gap:16px">{eyebrow('{{eyebrow}}')}<h2 style="font-size:clamp(32px,4vw,52px);line-height:1.1;font-weight:800;color:#1a1a1a">{{{{title}}}}</h2></div>
<p style="flex:1 1 420px;font-size:18px;line-height:1.65;color:rgba(26,26,26,.78)">{{{{text}}}}</p></div>
<div style="display:flex;flex-wrap:wrap;gap:20px">
<sc-for list="{{{{cards}}}}" as="c" hint-placeholder-count="5">
<div style="flex:1 1 220px;min-height:260px;display:flex;flex-direction:column;gap:18px;padding:28px;border-radius:24px;background:rgba(105,181,41,.09);border:1px solid rgba(0,102,51,.16)">
<span style="width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#69b529,#006633);display:inline-flex;align-items:center;justify-content:center;color:#fff;font-family:Montserrat,system-ui,sans-serif;font-weight:800;font-size:20px" aria-hidden="true">{{{{c.n}}}}</span>
<h3 style="font-size:20px;line-height:1.25;font-weight:700;color:#1a1a1a">{{{{c.title}}}}</h3>
<p style="font-size:15px;line-height:1.6;color:rgba(26,26,26,.78)">{{{{c.text}}}}</p></div>
</sc-for></div></div></section>
<section style="background:rgba(26,26,26,.04)"><div style="max-width:1440px;margin:0 auto;padding:96px 80px;display:flex;flex-wrap:wrap;flex-direction:{{{{dir}}}};align-items:center;gap:64px">
<div style="flex:1 1 480px;min-width:0"><div style="width:100%;aspect-ratio:600/520;border-radius:28px;overflow:hidden;box-shadow:0 24px 60px rgba(26,26,26,.18)"><img src="{{{{img}}}}" alt="" style="width:100%;height:100%;display:block;object-fit:cover"></div></div>
<div style="flex:1 1 480px;min-width:0;display:flex;flex-direction:column;align-items:flex-start;gap:24px">
{eyebrow('{{eyebrow2}}')}<h2 style="font-size:clamp(30px,3.6vw,44px);line-height:1.12;font-weight:800;color:#1a1a1a">{{{{title2}}}}</h2>
<p style="font-size:18px;line-height:1.65;color:rgba(26,26,26,.78)">{{{{text2}}}}</p>
<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px">
<sc-for list="{{{{checks}}}}" as="k" hint-placeholder-count="6"><li style="display:flex;align-items:center;gap:14px;font-size:17px;line-height:1.4;color:#1a1a1a"><span style="flex:none;width:28px;height:28px;border-radius:50%;background:#69b529;display:inline-flex;align-items:center;justify-content:center" aria-hidden="true">{CHECK}</span><span>{{{{k.text}}}}</span></li></sc-for></ul>
<div style="display:flex;flex-wrap:wrap;align-items:center;gap:16px 28px;padding-top:8px"><a href="mailto:marketing@pecsikommunikacio.hu" style="{BTN};background:#69b529;color:#1a1a1a">Árajánlatot kérek</a><a href="#portfolio" style="display:inline-flex;align-items:center;min-height:44px;font-size:15px;font-weight:700;color:#006633;border-bottom:2px solid #006633">Lapozz bele portfóliónkba</a></div>
</div></div></section>
</div>'''
    script=f'''class Component extends DCLogic {{
renderVals() {{
const U = {J(U)};
const D = {J(INTRO)};
const k = this.props.page ?? "grafika";
const d = D[k];
const r = this.props.reverse === true || this.props.reverse === "true";
return {{
dir: r ? "row-reverse" : "row", img: U[k],
eyebrow: d.e, title: d.h, text: d.p, eyebrow2: d.e2, title2: d.h2, text2: d.p2,
cards: d.cards.map((c, i) => ({{ n: i + 1, title: c[0], text: c[1] }})),
checks: d.checks.map((t) => ({{ text: t }}))
}};
}}
}}'''
    return doc('Bevezető és kiemelés',body,script,1420)
def packages():
    body=f'''<section style="width:100%;background:#fff;color:#1a1a1a;font-family:Inter,system-ui,sans-serif;border-top:1px solid rgba(26,26,26,.1)">
<div style="max-width:1440px;margin:0 auto;padding:96px 80px;display:flex;flex-direction:column;gap:56px">
<div style="display:flex;flex-direction:column;align-items:center;gap:16px;text-align:center">{eyebrow('{{eyebrow}}')}<h2 style="font-size:clamp(32px,4vw,52px);line-height:1.1;font-weight:800;color:#1a1a1a;max-width:800px">{{{{title}}}}</h2><p style="font-size:18px;line-height:1.65;color:rgba(26,26,26,.78);max-width:640px">{{{{text}}}}</p></div>
<div style="display:flex;flex-wrap:wrap;align-items:stretch;gap:24px">
<sc-for list="{{{{plans}}}}" as="p" hint-placeholder-count="3">
<div style="flex:1 1 320px;display:flex;flex-direction:column;gap:24px;padding:40px;border-radius:28px;background:{{{{p.bg}}}};color:{{{{p.fg}}}};border:2px solid {{{{p.border}}}}">
<div style="display:flex;align-items:center;justify-content:space-between;gap:12px"><h3 style="font-size:24px;line-height:1.2;font-weight:800;color:{{{{p.fg}}}}">{{{{p.name}}}}</h3><sc-if value="{{{{p.featured}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="padding:6px 14px;border-radius:999px;background:#69b529;color:#1a1a1a;font-size:12px;font-weight:700">Ajánlott</span></sc-if></div>
<div style="display:flex;flex-direction:column;gap:4px"><span style="font-family:Montserrat,system-ui,sans-serif;font-size:30px;line-height:1.1;font-weight:800;color:{{{{p.fg}}}}">Egyedi árajánlat</span><span style="font-size:14px;color:{{{{p.fg}}}};opacity:.8">a feladatod igényei szerint</span></div>
<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px;flex:1">
<sc-for list="{{{{p.items}}}}" as="i" hint-placeholder-count="5"><li style="display:flex;align-items:center;gap:12px;font-size:16px;line-height:1.4"><span style="flex:none;width:24px;height:24px;border-radius:50%;background:#69b529;display:inline-flex;align-items:center;justify-content:center" aria-hidden="true">{CHECK.replace('width="14" height="14"','width="12" height="12"')}</span><span>{{{{i.t}}}}</span></li></sc-for></ul>
<a href="mailto:marketing@pecsikommunikacio.hu" style="display:inline-flex;align-items:center;justify-content:center;min-height:52px;border-radius:999px;background:{{{{p.btnBg}}}};color:{{{{p.btnFg}}}};font-size:15px;font-weight:700;border:2px solid #69b529">Árajánlatot kérek</a>
</div></sc-for></div></div></section>'''
    script=f'''class Component extends DCLogic {{
renderVals() {{
const D = {J({k:{'e':v[0],'t':v[1],'x':v[2],'plans':[[n,i] for n,i in v[3]]} for k,v in PKG.items()})};
const k = this.props.page ?? "grafika";
const d = D[k];
const light = {{ bg: "#ffffff", fg: "#1a1a1a", border: "rgba(26,26,26,0.15)", btnBg: "transparent", btnFg: "#1a1a1a", featured: false }};
const dark = {{ bg: "#1a1a1a", fg: "#ffffff", border: "#69b529", btnBg: "#69b529", btnFg: "#1a1a1a", featured: true }};
return {{ eyebrow: d.e, title: d.t, text: d.x,
plans: d.plans.map((p, i) => Object.assign({{ name: p[0], items: p[1].map((t) => ({{ t: t }})) }}, i === 1 ? dark : light)) }};
}}
}}'''
    return doc('Csomagajánlatok',body,script,960)
def folyamat():
    rows=''
    for i in range(8):
        rows+=f'''<li data-fs="{{{{uid}}}}" style="position:relative;display:flex;align-items:center;gap:28px;min-height:210px">
<span style="{{{{d{i}}}}}">{i+1}</span>
<div style="flex:1 1 280px;min-width:0;display:flex;flex-wrap:wrap;align-items:center;gap:20px 36px;opacity:{{{{o{i}}}}};transform:{{{{t{i}}}}};transition:transform .5s ease,opacity .5s ease">
<div style="flex:1 1 260px;min-width:0;display:flex;flex-direction:column;gap:10px"><span style="font-family:Montserrat,system-ui,sans-serif;font-size:14px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#006633">{i+1:02d} / 08</span><h3 style="font-size:clamp(24px,2.6vw,34px);line-height:1.15;font-weight:800;color:#1a1a1a">{STEPNAMES[i]}</h3><p style="font-size:16px;line-height:1.65;color:rgba(26,26,26,.82)">{{{{x{i}}}}}</p></div>
<div style="flex:0 0 220px;width:220px;height:160px;border-radius:20px;overflow:hidden;background:#edf3e8;transform:scale({{{{s{i}}}}});transition:transform .5s ease,box-shadow .5s ease;box-shadow:{{{{b{i}}}}}">{art.step(i)}</div></div></li>'''
    body=f'''<section style="background:#fff;font-family:Inter,system-ui,sans-serif;color:#1a1a1a"><div style="max-width:1440px;margin:0 auto;padding:96px 80px;display:flex;flex-direction:column;gap:48px">
<div style="display:flex;flex-direction:column;gap:16px;max-width:760px">{eyebrow('Munkamenet')}<h2 style="font-size:clamp(32px,4vw,52px);line-height:1.1;font-weight:800;color:#1a1a1a">Hogyan zajlik majd a közös munka?</h2><p style="font-size:17px;line-height:1.65;color:rgba(26,26,26,.78)">Nyolc lépésben visszük végig a projektet. Görgess lefelé, és a lépések sorban kiemelődnek, felfelé görgetve pedig visszalépsz.</p></div>
<div style="position:relative"><div style="position:absolute;left:27px;top:105px;bottom:105px;width:4px;border-radius:2px;background:#d9d9d9" aria-hidden="true"><div style="width:4px;border-radius:2px;background:linear-gradient(180deg,#69b529,#006633);height:{{{{fill}}}}%;transition:height .25s linear"></div></div>
<ol style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column">{rows}</ol></div>
<div><a href="#kapcsolat" style="{BTN};background:#69b529;color:#1a1a1a">Vágjunk bele!</a></div>
</div></section>'''
    script=f'''class Component extends DCLogic {{
constructor(props) {{
super(props);
this.uid = "fs" + Math.random().toString(36).slice(2, 8);
this.state = {{ active: 0, fill: 0 }};
this.onScroll = this.onScroll.bind(this);
}}
componentDidMount() {{
document.addEventListener("scroll", this.onScroll, true);
window.addEventListener("resize", this.onScroll);
this.onScroll();
}}
componentWillUnmount() {{
document.removeEventListener("scroll", this.onScroll, true);
window.removeEventListener("resize", this.onScroll);
}}
onScroll() {{
const rows = document.querySelectorAll('[data-fs="' + this.uid + '"]');
if (!rows.length) return;
const vh = window.innerHeight || 800;
const mid = vh * 0.5;
let a = 0;
const c = [];
rows.forEach((r, i) => {{
const b = r.getBoundingClientRect();
const m = b.top + b.height / 2;
c.push(m);
if (m <= mid + b.height * 0.25) a = i;
}});
const span = c[c.length - 1] - c[0];
const f = span > 0 ? Math.max(0, Math.min(1, (mid - c[0]) / span)) * 100 : 0;
if (a !== this.state.active || Math.abs(f - this.state.fill) > 1) this.setState({{ active: a, fill: f }});
}}
renderVals() {{
const A = this.state.active;
const D = {J(STEPS)};
const k = this.props.page ?? "grafika";
const out = {{ uid: this.uid, fill: this.state.fill }};
for (let i = 0; i < 8; i++) {{
const on = i === A, done = i < A;
out["o" + i] = on ? 1 : done ? 0.6 : 0.35;
out["t" + i] = "translateX(" + (on ? 0 : -14) + "px)";
out["s" + i] = on ? 1.06 : 0.94;
out["b" + i] = on ? "0 18px 40px rgba(0,102,51,.28)" : "none";
out["x" + i] = D[k][i];
out["d" + i] = "flex:none;position:relative;z-index:1;width:58px;height:58px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-family:Montserrat,system-ui,sans-serif;font-size:22px;font-weight:800;border:3px solid " + (on ? "#006633" : done ? "#69b529" : "#bdbdbd") + ";background:" + (on ? "#006633" : done ? "#69b529" : "#fff") + ";color:" + (on ? "#fff" : done ? "#1a1a1a" : "#6b6b6b") + ";transform:scale(" + (on ? 1.15 : 1) + ");box-shadow:" + (on ? "0 0 0 8px rgba(105,181,41,.3)" : "none") + ";transition:all .4s ease";
}}
return out;
}}
}}'''
    return doc('Munkamenet (görgetésre váltó)',body,script,1900)
def process_faq():
    body=f'''<div style="width:100%;font-family:Inter,system-ui,sans-serif;color:#1a1a1a;background:#fff">
<section id="portfolio" style="background:rgba(26,26,26,.05)"><div style="max-width:1440px;margin:0 auto;padding:96px 80px">
<div style="display:flex;flex-wrap:wrap;align-items:center;gap:40px;padding:48px;border-radius:32px;background:#1a1a1a;color:#fff">
<div style="flex:1 1 380px;min-width:0"><div style="width:100%;aspect-ratio:600/520;max-height:340px;border-radius:20px;overflow:hidden"><img src="{{{{img}}}}" alt="" style="width:100%;height:100%;display:block;object-fit:cover"></div></div>
<div style="flex:1 1 380px;min-width:0;display:flex;flex-direction:column;align-items:flex-start;gap:18px"><h3 style="font-size:clamp(26px,3vw,36px);line-height:1.15;font-weight:800;color:#fff">Lapozz bele online portfóliónkba</h3><p style="font-size:17px;line-height:1.65;color:rgba(255,255,255,.78)">{{{{port}}}}</p><a href="#" style="{BTN};background:#69b529;color:#1a1a1a">Megnézem</a></div></div></div></section>
<section style="background:rgba(105,181,41,.08)"><div style="max-width:1440px;margin:0 auto;padding:96px 80px;display:flex;flex-wrap:wrap;gap:48px 80px">
<div style="flex:1 1 320px;display:flex;flex-direction:column;gap:16px;align-self:flex-start">{eyebrow('GYIK')}<h2 style="font-size:clamp(32px,4vw,52px);line-height:1.1;font-weight:800;color:#1a1a1a">Gyakran Ismételt Kérdések</h2><p style="font-size:17px;line-height:1.65;color:rgba(26,26,26,.78)">Nem találod a választ? Írj nekünk, szívesen segítünk.</p></div>
<div style="flex:2 1 560px;min-width:0;display:flex;flex-direction:column;gap:14px">
<sc-for list="{{{{faq}}}}" as="f" hint-placeholder-count="4"><details open="{{{{f.open}}}}" style="padding:24px 28px;border-radius:20px;background:#fff;border:1px solid rgba(26,26,26,.1)"><summary style="display:flex;align-items:center;justify-content:space-between;gap:20px;cursor:pointer;list-style:none;min-height:44px"><h3 style="font-size:18px;line-height:1.35;font-weight:700;color:#1a1a1a">{{{{f.q}}}}</h3><span class="faq-i" style="flex:none;width:36px;height:36px;border-radius:50%;background:#1a1a1a;color:#69b529;display:inline-flex;align-items:center;justify-content:center;font-size:22px;font-weight:600;line-height:1" aria-hidden="true"></span></summary><p style="margin-top:14px;font-size:16px;line-height:1.65;color:rgba(26,26,26,.78)">{{{{f.a}}}}</p></details></sc-for>
</div></div></section></div>'''
    script=f'''class Component extends DCLogic {{
renderVals() {{
const U = {J(U)};
const P = {J(PORT)};
const F = {J({k:[list(x) for x in v] for k,v in FAQ.items()})};
const k = this.props.page ?? "grafika";
return {{ img: U[k], port: P[k], faq: F[k].map((q, i) => ({{ q: q[0], a: q[1], open: i === 0 }})) }};
}}
}}'''
    return doc('Portfólió és GYIK',body,script,1100)
def site_footer():
    old=open('../old/SiteFooter.dc.html').read()
    a=old.index('<div style="width:100%;font-family'); b=old.index('</x-dc>')
    body=old[a:b]
    body=body.replace('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\n</div>\n<div style="display:flex;flex-wrap:wrap;gap:24px">','Nézd meg a többi szolgáltatásunkat is: egy csapatban dolgozunk, így a munkáid egymásra épülnek, és a megjelenésed mindenhol egységes marad.</p>\n</div>\n<div style="display:flex;flex-wrap:wrap;gap:24px">',1)
    body=body.replace('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','Mesélj a céljaidról, és megmutatjuk, hogyan segíthetünk. Az első egyeztetés után részletes, átlátható árajánlatot küldünk.')
    body=body.replace('<div class="ph" style="height:220px;border-radius:24px;display:flex;align-items:center;justify-content:center"><span class="chip">Kép</span></div>','<div style="height:220px;border-radius:24px;overflow:hidden"><img src="{{r.img}}" alt="" style="width:100%;height:100%;display:block;object-fit:cover"></div>')
    body=body.replace('<a href="#" style="flex:1 1 260px;','<a href="{{r.href}}" style="flex:1 1 260px;')
    body=body.replace('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.','Töltsd ki az űrlapot, vagy írj nekünk e-mailt, és hamarosan felvesszük veled a kapcsolatot.')
    assert 'Lorem' not in body, body[body.index('Lorem')-100:body.index('Lorem')+100]
    helm=old[old.index('<helmet>')+8:old.index('</helmet>')]
    script=f'''class Component extends DCLogic {{
renderVals() {{
const U = {J(U)};
const N = {J(NAMES)};
const F = {J(FILES)};
const keys = Object.keys(N);
const cur = this.props.current ?? "Grafika";
let i = keys.findIndex((k) => N[k] === cur);
if (i < 0) i = 0;
const related = [1, 2, 3, 4].map((o) => {{ const k = keys[(i + o) % keys.length]; return {{ name: N[k], img: U[k], href: F[k] + ".dc.html" }}; }});
return {{ related: related }};
}}
}}'''
    return f'''<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<title>Kapcsolódó szolgáltatások, kapcsolat, lábléc</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>{helm}</helmet>
{body}</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"current":{{"editor":"text","default":"Grafika"}},"$preview":{{"width":1440,"height":1780}}}}'>
{script}
</script>
</body>
</html>
'''
for name,fn in [('PageHero',page_hero),('IntroSplit',intro_split),('Packages',packages),('Folyamat',folyamat),('ProcessFaq',process_faq),('SiteFooter',site_footer)]:
    open(OUT+name+'.dc.html','w').write(fn())
print('shared ok')
