from pages.base_page import BasePage


class ProductsPage(BasePage):
    BASKET = "[data-test=\"shopping-cart-link\"]"
    BUTTON_BACKPACK = '[data-test="add-to-cart-sauce-labs-backpack"]'


    def __init__(self, playwright):
        super().__init__(playwright)


    def add_backpack_to_basket(self):
        self.playwright.locator(self.BUTTON_BACKPACK).click()

    def move_to_basket(self):
        self.playwright.locator(self.BASKET).click()