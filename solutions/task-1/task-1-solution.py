from playwright.sync_api import sync_playwright, expect

def test_swag_labs_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        expect(page.get_by_text("Swag Labs")).to_be_visible()
        browser.close()