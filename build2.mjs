import fs from 'fs'; import path from 'path';
import { parseDocument } from 'htmlparser2';
import { DomUtils } from 'htmlparser2';
const SRC = process.argv[2], OUT = process.argv[3];
const VOID = new Set(['input','br','img','meta','link','hr','path']);
const SVGSELF = new Set(['path','circle','rect','line','polyline','polygon']);
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const escA = s => String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;');
const cache = {};
function load(name){
  if(cache[name]) return cache[name];
  const html = fs.readFileSync(path.join(SRC, name + '.dc.html'),'utf8');
  const doc = parseDocument(html);
  const xdc = DomUtils.findOne(e=>e.name==='x-dc', doc.children);
  const scr = DomUtils.findOne(e=>e.name==='script' && e.attribs['data-dc-script']!==undefined, doc.children);
  const code = scr ? DomUtils.textContent(scr) : 'class Component extends DCLogic{renderVals(){return{}}}';
  const Cls = new Function('DCLogic', code + '\nreturn Component;')(class{constructor(p){this.props=p}});
  return cache[name] = { xdc, Cls };
}
const lookup = (expr, scope) => {
  expr = expr.trim();
  if(expr==='true') return true; if(expr==='false') return false;
  return expr.split('.').reduce((o,k)=>o==null?undefined:o[k], scope);
};
const HOLE = /\{\{([^}]*)\}\}/g;
const interp = (s, scope) => s.replace(HOLE,(_,e)=>{const v=lookup(e,scope);return v==null?'':String(v)});
const styles = new Set(), links = new Set(["https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@300;500;600;700;800&display=swap"]);
function render(nodes, scope){
  let out='';
  for(const n of nodes){
    if(n.type==='text'){ out += esc(interp(n.data, scope)); continue; }
    if(n.type!=='tag' && n.type!=='script' && n.type!=='style') continue;
    const name = n.name;
    if(name==='helmet'){
      for(const c of n.children){
        if(c.name==='style') styles.add(DomUtils.textContent(c));
        if(c.name==='link') links.add(c.attribs.href.replace(/&amp;/g,'&'));
      } continue;
    }
    if(name==='sc-for'){
      const list = lookup(n.attribs.list.replace(/[{}]/g,''), scope) || [];
      for(const it of list) out += render(n.children, {...scope, [n.attribs.as]: it});
      continue;
    }
    if(name==='sc-if'){
      if(lookup(n.attribs.value.replace(/[{}]/g,''), scope)) out += render(n.children, scope);
      continue;
    }
    if(name==='dc-import'){
      const {xdc, Cls} = load(n.attribs.name);
      const props = {};
      for(const [k,v] of Object.entries(n.attribs)){
        if(k==='name'||k.startsWith('hint-')) continue;
        const m = v.match(/^\{\{(.*)\}\}$/);
        props[k] = m ? lookup(m[1], scope) : v;
      }
      const vals = new Cls(props).renderVals();
      out += render(xdc.children, {...vals}); continue;
    }
    let attrs='';
    for(const [k,v] of Object.entries(n.attribs)){
      if(k.startsWith('hint-')) continue;
      const m = v.match(/^\{\{(.*)\}\}$/);
      if(m && (k==='open')){ if(lookup(m[1],scope)) attrs+=` ${k}`; continue; }
      attrs += ` ${k}="${escA(interp(v,scope))}"`;
    }
    if(VOID.has(name) && !n.children.length){ out += `<${name}${attrs}>`; continue; }
    if(SVGSELF.has(name) && !n.children.length){ out += `<${name}${attrs}></${name}>`; continue; }
    out += `<${name}${attrs}>${render(n.children, scope)}</${name}>`;
  }
  return out;
}
const PAGES = [
 ['Main','grafika','Grafika'],['Videokeszites','videokeszites','Videókészítés'],['Webfejlesztes','webfejlesztes','Webfejlesztés'],
 ['Webhosting','webhosting','Webhosting'],['SocialMedia','social-media','Social media'],['MarketingManagement','marketing-management','Marketing management'],
 ['Reklamfeluletek','reklamfeluletek','Reklámfelületek'],['NyomdaiGyartas','nyomdai-gyartas','Nyomdai gyártás']];
const MAP = Object.fromEntries(PAGES.map(p=>[p[2],'/'+p[1]])); MAP['Kezdőlap']='/'; MAP['Szolgáltatásaink']='/';
const SMAP=new Map();
function classify(html){
  return html.replace(/<([a-z0-9-]+)((?:\s[^>]*?)?)\sstyle="([^"]*)"([^>]*)>/g,(m,tag,pre,st,post)=>{
    let id=SMAP.get(st); if(!id){id='s'+SMAP.size.toString(36);SMAP.set(st,id);}
    const all=pre+post; const cm=all.match(/\sclass="([^"]*)"/);
    if(cm) return `<${tag}${all.replace(cm[0],' class="'+cm[1]+' '+id+'"')}>`;
    return `<${tag}${all} class="${id}">`;
  });
}
function fixLinks(html){
  return html.replace(/<a href="#"([^>]*)>((?:(?!<\/a>).)*)<\/a>/gs,(m,attrs,inner)=>{
    const t = inner.replace(/<[^>]*>/g,'').trim();
    const h = MAP[t]; return h ? `<a href="${h}"${attrs}>${inner}</a>` : m;
  });
}
const BLOB = JSON.parse(fs.readFileSync(path.join(path.dirname(new URL(import.meta.url).pathname),'blobs.json'),'utf8'));
function deblob(h){
  h = h.replace(/\/_blob\/([0-9a-f]{32})/g,(m,id)=>'/img/'+(BLOB[id]||id)+'.svg');
  h = h.replace(/href="([A-Za-z]+)\.dc\.html"/g,(m,f)=>{const p=PAGES.find(p=>p[0]===f);return p?`href="/${p[1]}"`:m;});
  return h;
}
const SCRIPT = `<script>(function(){var lis=[].slice.call(document.querySelectorAll('li[data-fs]'));if(!lis.length)return;var ol=lis[0].parentNode,fill=ol.previousElementSibling&&ol.previousElementSibling.firstElementChild;
function upd(){var vh=window.innerHeight||800,mid=vh/2,a=0,c=[];lis.forEach(function(r,i){var b=r.getBoundingClientRect(),m=b.top+b.height/2;c.push(m);if(m<=mid+b.height*.25)a=i});
var span=c[c.length-1]-c[0],f=span>0?Math.max(0,Math.min(1,(mid-c[0])/span))*100:0;if(fill)fill.style.height=f+'%';
lis.forEach(function(r,i){var on=i===a,done=i<a,d=r.children[0],ct=r.children[1],bx=ct.children[1];
ct.style.opacity=on?1:done?.6:.35;ct.style.transform='translateX('+(on?0:-14)+'px)';
bx.style.transform='scale('+(on?1.06:.94)+')';bx.style.boxShadow=on?'0 18px 40px rgba(0,102,51,.28)':'none';
d.style.borderColor=on?'#006633':done?'#69b529':'#bdbdbd';d.style.background=on?'#006633':done?'#69b529':'#fff';d.style.color=on?'#fff':done?'#1a1a1a':'#6b6b6b';
d.style.transform='scale('+(on?1.15:1)+')';d.style.boxShadow=on?'0 0 0 8px rgba(105,181,41,.3)':'none'})}
window.addEventListener('scroll',upd,{passive:true});window.addEventListener('resize',upd);upd()})()</script>`;
function wrap(title, body, desc, slug){
  body = deblob(classify(body));
  const css = [...styles].join('\n');
  return `<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>${esc(title)} – Pécsi Kommunikációs Központ</title><meta name="description" content="${escA(desc)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>${[...links].map(l=>`<link rel="stylesheet" href="${escA(l)}">`).join('')}<link rel="stylesheet" href="/s.css"><style>${css}</style></head><body class="pg pg-${slug}">${body}${body.includes('data-fs=')?SCRIPT:''}</body></html>`;
}
fs.mkdirSync(OUT,{recursive:true});
const DESC={'grafika':'Arculat, logó és kiadványok tervezése.','videokeszites':'Imázsfilmek, reklámok és közösségi videók.','webfejlesztes':'Reszponzív weboldalak és webshopok.','webhosting':'Biztonságos tárhely és üzemeltetés.','social-media':'Tartalomgyártás és közösségépítés.','marketing-management':'Stratégia, kampányok és mérés.','reklamfeluletek':'Kültéri reklámfelületek Pécsen.','nyomdai-gyartas':'Nyomtatott kiadványok a tervezéstől a kiszállításig.'};
for(const [file,slug,title] of PAGES){
  styles.clear();
  const {xdc, Cls} = load(file);
  let body = fixLinks(render(xdc.children, new Cls({}).renderVals()));
  fs.writeFileSync(path.join(OUT,slug+'.html'), wrap(title, body, DESC[slug], slug));
}
styles.clear();
{const {xdc, Cls} = load('Eredeti');
 let body = fixLinks(render(xdc.children, new Cls({}).renderVals()));
 fs.writeFileSync(path.join(OUT,'index.html'), wrap('Kezdőlap', body, 'Marketing, grafika, web és nyomda egy helyen.', 'index'));}
fs.writeFileSync(path.join(OUT,'robots.txt'),'User-agent: *\nDisallow: /\n');
let sc='',m900='',m560='';
for(const [st,id] of SMAP){
  sc+=`.${id}{${st}}\n`;
  if(st.includes('padding:96px 80px')) {m900+=`.${id}{padding:64px 24px!important}`; m560+=`.${id}{padding:48px 20px!important}`;}
  if(st.includes('padding:80px;')) {m900+=`.${id}{padding:56px 24px!important}`; m560+=`.${id}{padding:40px 20px!important}`;}
  if(st.includes('padding:72px 80px')) m900+=`.${id}{padding:56px 24px 32px!important}`;
  if(st.includes('padding:22px 80px')) {m900+=`.${id}{padding:16px 24px!important}`; m560+=`.${id}{padding:14px 20px!important}`;}
  if(/gap:(56|40|48)px 80px/.test(st)) m900+=`.${id}{gap:40px!important}`;
  if(/padding:(48|40|36|56)px;border-radius:(32|28)px/.test(st)) m560+=`.${id}{padding:24px!important}`;
}
sc+=`html{scroll-behavior:smooth}\nimg,svg,input,textarea{max-width:100%}\n@media(max-width:900px){${m900}}\n@media(max-width:560px){${m560}}\n`;
fs.writeFileSync(path.join(OUT,'s.css'),sc);
console.log('ok',SMAP.size);
