from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox','--disable-dev-shm-usage'])
    for width,height in [(1440,900),(390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height}, device_scale_factor=1)
        errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.goto('http://localhost:4173/', wait_until='load',timeout=25000)
        page.screenshot(path=str(root/f'selara-{width}.png'),full_page=True)
        print(width,'title',page.title(),'scrollWidth',page.evaluate('document.documentElement.scrollWidth'),'errors',errors)
        if width==1440:
            page.locator('[data-filter="family"]').click()
            assert page.locator('.room-card:visible').count()==1
            page.locator('[data-filter="all"]').click()
            page.locator('[data-save="grove"]').click()
            assert page.locator('#fav-counter').inner_text()=='1'
            page.locator('#room-select').select_option('grove')
            assert page.locator('#total-price').inner_text().startswith('RM')
            page.locator('#download-trip').click()
        page.close()
    browser.close()
