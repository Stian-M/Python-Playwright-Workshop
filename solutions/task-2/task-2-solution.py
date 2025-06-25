from playwright.sync_api import sync_playwright, expect

def test_swag_labs_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        # Fill in the login form
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        # Click the login button
        page.locator("[data-test=\"login-button\"]").click()
        # Verify that the title is visible after login
        expect(page.locator("[data-test=\"title\"]")).to_be_visible()
        browser.close()