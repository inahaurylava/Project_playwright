
from conftest import playwright
from pages.login_page import LoginPage


def test_positive_login(playwright):
    login_page = LoginPage(playwright)
    login_page.valid_login()
    playwright.screenshot(path=f"output/screenshots/test_positive_login/screenshot.png")


