import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def playwright():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="output/videos")
        page = context.new_page()
        yield page
        context.close()
        browser.close()