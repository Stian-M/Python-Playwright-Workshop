from playwright.sync_api import sync_playwright, expect

def test_swag_labs_shopping():
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
        # Add three items to cart
        # item 1:
        page.locator("[data-test=\"item-4-title-link\"]").click()
        page.locator("[data-test=\"add-to-cart\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        # item 2:
        page.locator("[data-test=\"item-5-title-link\"]").click()
        page.locator("[data-test=\"add-to-cart\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        # item 3:
        page.locator("[data-test=\"item-2-title-link\"]").click()
        page.locator("[data-test=\"add-to-cart\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        # Navigate to the cart page
        page.locator("[data-test=\"shopping-cart-link\"]").click()
        # Click the checkout button
        page.locator("[data-test=\"checkout\"]").click()
        # Fill in the checkout form
        page.locator("[data-test=\"firstName\"]").click()
        page.locator("[data-test=\"firstName\"]").fill("something")
        page.locator("[data-test=\"lastName\"]").click()
        page.locator("[data-test=\"lastName\"]").fill("something12")
        page.locator("[data-test=\"postalCode\"]").click()
        page.locator("[data-test=\"postalCode\"]").fill("1234")
        page.locator("[data-test=\"lastName\"]").click()
        page.locator("[data-test=\"lastName\"]").fill("something")
        # Click the continue button
        page.locator("[data-test=\"continue\"]").click()
        # Click the finish button
        page.locator("[data-test=\"finish\"]").click()
        # Take a screenshot of the finished page
        page.screenshot(path="screenshots/finished.png")
        expect(page.get_by_text("Thank you for your order!")).to_be_visible()

        browser.close()