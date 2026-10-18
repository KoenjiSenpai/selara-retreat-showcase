import {readFile,stat} from 'node:fs/promises';
import {resolve} from 'node:path';
const root=resolve('.'), dir=resolve(root,'public');
const html=await readFile(resolve(dir,'index.html'),'utf8');
const css=await readFile(resolve(dir,'styles.css'),'utf8');
const js=await readFile(resolve(dir,'app.js'),'utf8');
const required=['home','story','sanctuaries','experiences','plan','guide','room-select','check-in','check-out','guest-count','download-trip','stay-dialog','experience-image','selected-experience','empty-saved'];
for(const id of required) if(!html.includes(`id="${id}"`)) throw Error(`Missing expected element: ${id}`);
const refs=new Set([...html.matchAll(/(?:src|href)="(\/assets\/[^"?#]+)"/g)].map(m=>m[1]));
for(const m of js.matchAll(/['"](\/assets\/[a-z0-9-]+\.(?:svg|png|webp))['"]/g)) refs.add(m[1]);
for(const ref of refs){const file=resolve(dir,ref.slice(1));if(!(await stat(file).catch(()=>null)))throw Error('Missing referenced asset: '+ref);}
if(!js.includes('estimate(')||!js.includes('showExperience(')||!js.includes('renderSavedVisibility('))throw Error('Core interactive features missing');
if(!css.includes('prefers-reduced-motion'))throw Error('Reduced-motion CSS missing');
if(!html.includes('Fictional property · No real booking or payment'))throw Error('Concept disclaimer missing');
const genericSvgPaths=['palm.svg','sunrise.svg','wave.svg'];
for(const ref of genericSvgPaths) if(html.includes(`/assets/${ref}`))throw Error('Old placeholder still used: '+ref);
console.log(`Structural QA passed: ${required.length} key elements, ${refs.size} referenced visual assets`);
