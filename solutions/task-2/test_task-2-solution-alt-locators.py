from playwright.sync_api import sync_playwright, expect

def test_swag_labs_screenshot_alt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        # Fill in the login form
        page.get_by_role("textbox", name="Username").fill('standard_user')
        page.get_by_role("textbox", name="Password").fill('secret_sauce')
        # Click the login button
        page.get_by_role("button", name="Login").click()
        # verify that the title is visible after login
        expect(page.get_by_text("Products")).to_be_visible()

        browser.close()
