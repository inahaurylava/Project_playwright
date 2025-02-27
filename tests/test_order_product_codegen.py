import page
from playwright.sync_api import sync_playwright, expect



def test_order_product():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="output/videos")
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
        page.locator("[data-test=\"shopping-cart-link\"]").click()
        page.locator("[data-test=\"checkout\"]").click()
        page.locator("[data-test=\"firstName\"]").click()
        page.locator("[data-test=\"firstName\"]").fill("Ina")
        page.locator("[data-test=\"lastName\"]").click()
        page.locator("[data-test=\"lastName\"]").fill("Test")
        page.locator("[data-test=\"postalCode\"]").click()
        page.locator("[data-test=\"postalCode\"]").fill("220059")
        page.locator("[data-test=\"continue\"]").click()
        page.locator("[data-test=\"finish\"]").click()
        expect(page.locator("[data-test=\"back-to-products\"]")).to_be_visible()
        expect(page.locator("[data-test=\"complete-header\"]")).to_be_visible()
        page.screenshot(path=f"output/screenshots/test_order_product/screenshot.png")


        # ---------------------
        context.close()
        browser.close()



