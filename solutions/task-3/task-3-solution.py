from playwright.sync_api import sync_playwright, expect

def test_swag_labs_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        # Fill in the login form
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        # Click the backpack item
        page.locator("[data-test=\"item-4-title-link\"]").click()
        # Take a screenshot of the backpack item
        page.screenshot(path="screenshots/backpack_item.png")

        browser.close()
