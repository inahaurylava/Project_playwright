from pages.base_page import (BasePage)


class BasketPage(BasePage):
    PRODUCTS_IN_BASKET_CONTAINER = 'div[data-test="cart-list"]'
    PRODUCTS_IN_BASKET_ITEM = '[data-test="inventory-item"]'
    ORDERED_PRODUCT = '//div[@class="cart_item_label"]//a//div'

    def assert_product(self, expected_text):
        products_list_container = self.playwright.locator(self.PRODUCTS_IN_BASKET_CONTAINER)
        product_list = products_list_container.locator(self.PRODUCTS_IN_BASKET_ITEM)
        assert product_list.count() > 0
        first_product = product_list.first
        product_title_div = first_product.locator(self.ORDERED_PRODUCT)
        assert product_title_div.inner_text() == expected_text
