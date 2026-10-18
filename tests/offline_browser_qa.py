"""Offline Chromium visual and interaction audit for restricted navigation environments.
Embeds the site's own HTML/CSS/JS/assets in an about:blank document via Playwright.
No external dependencies except playwright + beautifulsoup4; works without localhost.
This is NOT a substitute for checking actual deployed network headers/URLs.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import base64,mimetypes,re,json

ROOT=Path(__file__).resolve().parents[1]
PUBLIC=ROOT/'public';SHOTS=ROOT/'qa-screenshots';SHOTS.mkdir(exist_ok=True)
html=BeautifulSoup((PUBLIC/'index.html').read_text(encoding='utf-8'),'html.parser')
style_text=(PUBLIC/'styles.css').read_text(encoding='utf-8')
model=(PUBLIC/'model.mjs').read_text(encoding='utf-8').replace('export ','')
app=(PUBLIC/'app.js').read_text(encoding='utf-8')
app=re.sub(r"^import\s*\{rooms,estimate,formatMYR\}\s*from\s*'/model\.mjs';",'',app)
assert "from'/model.mjs'" not in app
# App-generated images also need to resolve in this offline document.
for match in set(re.findall(r'/assets/[a-z0-9-]+\.svg',app)):
 file=PUBLIC/match.lstrip('/')
 if file.exists():
  app=app.replace(match,'data:image/svg+xml;base64,'+base64.b64encode(file.read_bytes()).decode())
for link in html.find_all('link'):
 if link.get('rel')==['stylesheet']:
  el=html.new_tag('style');el.string=style_text;link.replace_with(el)
 elif link.get('rel')==['manifest']:
  link.decompose()
for im in html.find_all('img'):
 src=im.get('src','')
 if src.startswith('/assets/'):
  file=PUBLIC/src.lstrip('/'); assert file.exists(),f'Missing {file}'
  mime=mimetypes.guess_type(str(file))[0] or 'image/svg+xml'
  im['src']='data:'+mime+';base64,'+base64.b64encode(file.read_bytes()).decode()
for script in html.find_all('script'):
 if script.get('src','')=='/app.js':
  script.attrs.pop('src');script.attrs.pop('type',None);script.string=model+'\n'+app
page_html=str(html)

with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for width,height in [(1440,900),(900,900),(390,844)]:
  pg=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1,accept_downloads=True)
  pg.add_init_script('''(() => { let values={}; Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:(k)=>values[k]??null,setItem:(k,v)=>{values[k]=String(v)},removeItem:(k)=>{delete values[k]},clear:()=>{values={}}}}); })()''')
  errors=[];pg.on('pageerror',lambda e:errors.append(str(e)))
  pg.set_content(page_html,wait_until='load',timeout=25000)
  pg.locator('.room-card').first.wait_for(timeout=8000)
  pg.locator('img').evaluate_all('ims=>ims.forEach(im=>im.loading="eager")')
  pg.wait_for_timeout(1000)
  pg.screenshot(path=str(SHOTS/f'selara-{width}.png'),full_page=True,animations='disabled')
  scroll=pg.evaluate('document.documentElement.scrollWidth')
  if scroll>width+2:raise AssertionError(f'Horizontal overflow {scroll} at width {width}')
  # Ensure newly added assets really render
  images=pg.locator('img')
  invalid=images.evaluate_all('ims=>ims.filter(im=>!im.complete||im.naturalWidth===0).map(im=>im.alt)')
  assert not invalid, f'Broken images: {invalid}'
  if width==1440:
   assert pg.locator('.room-card:visible').count()==3
   pg.locator('[data-filter="family"]').click();assert pg.locator('.room-card:visible').count()==1
   pg.locator('[data-filter="all"]').click();pg.locator('[data-save="grove"]').click();assert pg.locator('#fav-counter').inner_text()=='1'
   pg.locator('[data-filter="saved"]').click();assert pg.locator('.room-card:visible').count()==1
   pg.locator('[data-filter="all"]').click()
   pg.locator('[data-details="grove"]').click();assert pg.locator('#stay-dialog').evaluate('(el)=>el.open');assert 'Grove' in pg.locator('#stay-dialog-title').inner_text()
   pg.locator('#stay-dialog-close').click()
   pg.locator('[data-experience="nature"]').click();assert 'rainforest' in pg.locator('#experience-image').get_attribute('alt').lower();assert 'forest' in pg.locator('#selected-experience').inner_text().lower()
   pg.locator('#room-select').select_option('grove');assert pg.locator('#total-price').inner_text().startswith('RM')
   with pg.expect_download(timeout=8000) as dl:pg.locator('#download-trip').click()
   contents=Path(dl.value.path()).read_text();info=json.loads(contents)
   assert info['room']=='Grove Suite';assert info['experience']=='A forest morning'
  if width==390:
   pg.locator('#menu-toggle').click();assert pg.locator('#mobile-nav').is_visible();pg.locator('#mobile-nav a[href="#sanctuaries"]').click();assert not pg.locator('#mobile-nav').is_visible()
  assert not errors,f'JS errors: {errors}'
  print(json.dumps({'viewport':width,'scrollWidth':scroll,'allImagesLoaded':True,'jsErrors':errors}))
  pg.close()
 browser.close()
