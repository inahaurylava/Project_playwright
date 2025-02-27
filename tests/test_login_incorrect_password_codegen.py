
from playwright.sync_api import sync_playwright, expect


def test_login_incorrect_password():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="output/videos")
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret")
        page.locator("[data-test=\"login-button\"]").click()
        expect(page.locator("[data-test=\"error\"]")).to_be_visible()
        page.screenshot(path=f"output/screenshots/test_login_incorrect_password/screenshot.png")
        # ---------------------
        context.close()
        browser.close()
