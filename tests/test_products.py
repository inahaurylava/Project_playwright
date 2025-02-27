
from conftest import playwright
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_to_basket(playwright):
    login_page = LoginPage(playwright)
    login_page.get_login_page()
    login_page.success_login('standard_user', 'secret_sauce')

    product_page = ProductsPage(playwright)
    product_page.add_backpack_to_basket()
    product_page.move_to_basket()

    basket_page = BasketPage(playwright)
    basket_page.assert_product("Sauce Labs Backpack")
    playwright.screenshot(path=f"output/screenshots/test_add_to_basket/screenshot.png")


