from playwright.sync_api import sync_playwright, expect

def test_swag_labs_shopping_alt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        # Fill in the login form
        page.get_by_role("textbox", name="Username").fill('standard_user')
        page.get_by_role("textbox", name="Password").fill('secret_sauce')
        # Click the login button
        page.get_by_role("button", name="Login").click()
        # Add three items to cart
        page.get_by_text("Sauce Labs Backpack").click()
        page.get_by_role("button", name="Add to cart").click()
        page.get_by_role("button", name="Go back Back To Products").click()
        page.get_by_text("Sauce Labs Bike Light").click()
        page.get_by_role("button", name="Add to cart").click()
        page.get_by_role("button", name="Go back Back To Products").click()
        page.get_by_text("Sauce Labs Onesie").click() 
        page.get_by_role("button", name="Add to cart").click()
        page.get_by_role("button", name="Go back Back To Products").click()
        # Navigate to the cart page
        page.locator("[data-test=\"shopping-cart-link\"]").click()
        page.get_by_role("button", name="Checkout").click()
        # Fill in the checkout form
        page.get_by_role("textbox", name="First Name").fill("something")
        page.get_by_role("textbox", name="Last Name").fill("something12")
        page.get_by_role("textbox", name="Postal Code").fill("1234")
        # Click the continue button
        page.get_by_role("button", name="Continue").click()
        # Click the finish button
        page.get_by_role("button", name="Finish").click()
        # Take a screenshot of the finished page
        page.screenshot(path="screenshots/finished_alt.png")
        expect(page.get_by_text("Thank you for your order!")).to_be_visible()

        browser.close()
