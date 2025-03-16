from playwright.sync_api import sync_playwright, expect


def test_positive_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
        page.screenshot(path=f"output/screenshots/test_positive_login/screenshot.png")
    # ---------------------
        context.close()
        browser.close()


def test_negative_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="output/videos")
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"login-button\"]").click()
        expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")
        page.screenshot(path=f"output/screenshots/test_negative_login/screenshot.png")
        # ---------------------
        context.close()
        browser.close()


