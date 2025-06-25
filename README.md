# Python Playwright Workshop

Welcome to the Python Playwright Workshop! This workshop is your hands-on introduction to [Playwright](https://playwright.dev/python/), a modern framework for browser automation and end-to-end testing with Python.

## What is Playwright?

Playwright is an open-source automation library developed by Microsoft. It enables you to control browsers (Chromium, Firefox, and WebKit) using a single, unified API. With Playwright, you can automate tasks such as navigating web pages, filling out forms, clicking buttons, taking screenshots, and running comprehensive tests across multiple browsers.

Playwright is especially useful for:

- End-to-end testing of web applications
- Automating repetitive browser tasks
- Scraping web content
- Testing across different browsers and devices

## Workshop Overview

In this workshop, you will:

- **Learn the basics of Playwright's API**: Understand how to launch browsers, open pages, and interact with web elements.
- **Automate real-world scenarios**: Practice automating logins, navigation, form submissions, and more.
- **Capture screenshots and debug**: Use Playwright's tools to capture screenshots and debug your scripts.
- **Build robust tests**: Write scripts that can be used for automated testing of web applications.

You will find exercises in the `tasks/` directory and solutions in the `solutions/` directory. Jupyter notebooks are also available in the `notebooks/` folder for interactive exploration.

## How Browser Automation Works

Playwright scripts interact with browsers by:

1. **Launching a browser instance** (headless or with a visible UI)
2. **Opening a new page/tab**
3. **Navigating to a URL**
4. **Locating and interacting with elements** (click, type, select, etc.)
5. **Asserting conditions** (for testing)
6. **Closing the browser**

## Common Playwright Commands

Here are some useful Playwright commands you’ll use throughout the workshop:

```python
from playwright.sync_api import sync_playwright, expect

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=500)
        page = browser.new_page()
        page.goto("https://example.com")
        expect(page.get_by_text("Example Domain")).to_be_visible()
        browser.close()
```

**Other useful commands:**

- `page.title()` — Get the page title
- `page.locator("selector")` — Find an element
- `page.wait_for_selector("selector")` — Wait for an element to appear
- `browser_context = browser.new_context()` — Create isolated browser sessions
- `page.screenshot(path=")` — Take a screenshot of the current page and save it to 'path'

## Working with Locators

Locators are a core concept in Playwright, allowing you to find and interact with elements on the page in a robust and readable way. Playwright provides several methods to locate elements:

- **get_by_role**: Find elements by their [ARIA role](https://www.w3.org/TR/wai-aria/#roles), useful for accessible web apps.
  ```python
  page.get_by_role("button", name="Submit").click()
  ```
- **get_by_text**: Find elements by their visible text.
  ```python
  page.get_by_text("Sign in").click()
  ```
- **get_by_label**: Find form controls by their associated label text.
  ```python
  page.get_by_label("Username").fill("myuser")
  ```
- **get_by_placeholder**: Find input fields by their placeholder text.
  ```python
  page.get_by_placeholder("Search").fill("Playwright")
  ```
- **get_by_test_id**: Find elements by a custom `data-testid` attribute.
  ```python
  page.get_by_test_id("login-button").click()
  ```

You can also use standard CSS selectors with `page.locator("selector")` for more advanced queries.

**Tip:** Using these locator methods makes your tests more reliable and easier to read, especially when the UI changes.

## Assertions in Playwright

Assertions are essential for verifying that your automation scripts behave as expected. Playwright provides built-in assertion methods to check the state of elements, text content, visibility, and more.

```python
expect(page.get_by_text("Welcome")).to_be_visible()
expect(page.get_by_role("heading")).to_have_text("Dashboard")
```

You can use these assertions directly in your pytest test functions.

## Generating Tests and Locators

Playwright provides powerful tools to help you generate tests and locators quickly and interactively:

### 1. Using `playwright codegen` - This is the method I recommend for this workshop

The `playwright codegen` command opens a browser and records your actions, automatically generating code for you. This is a great way to get started with Playwright scripts or to discover the right locators for elements.

To start codegen, run:
```sh
playwright codegen https://example.com
```
- Interact with the page; Playwright will generate code in real time.
- You can copy and paste the generated code into your tests.

### 2. Playwright Codegen in VS Code

If you use Visual Studio Code, the [Playwright Test for VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright) provides an integrated codegen experience:
- Record user actions and generate code directly in your editor.
- Easily insert locators and actions into your test files.

### 3. Using `page.pause()` for Interactive Debugging

You can add `page.pause()` in your script to pause execution and open the Playwright Inspector. This lets you:
- Explore the page interactively.
- Hover over elements to get suggested locators.
- Resume script execution when ready.
- Important! page.pause() will not work when running tests with pytest.

Example:
```python
page.goto("https://example.com")
page.pause()  # Opens the inspector for interactive exploration
```

---

## Running the Tests

To run all Playwright tests using pytest, simply execute:
```sh
pytest
```
This will automatically discover and run all test files and functions following the `test_*.py` naming convention.

Ready to start? Open your first task in the `tasks/` folder or launch a notebook from the `notebooks/` directory. Happy automating!

If you wish to run the solution files, simply rename each python file and add `test_` at the beginning of the name.