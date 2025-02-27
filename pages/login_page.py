from pages.base_page import BasePage


class LoginPage(BasePage):
    INPUT_USER_NAME = "[data-test=\"username\"]"
    INPUT_PASSWORD = "[data-test=\"password\"]"
    CLICK_BUTTON = "[data-test=\"login-button\"]"
    ERROR_MESSAGE = "[data-test=\"error-message-container\"]"


    def __init__(self, playwright):
        super().__init__(playwright)

    def success_login(self, username, password):
        self.fill_user_name(username)
        self.fill_password(password)
        self.click_login_button()

    def get_login_page(self):
        self.playwright.goto('https://www.saucedemo.com')

    def fill_user_name(self, user_name):
        self.playwright.locator(self.INPUT_USER_NAME).fill(user_name)

    def fill_password(self, password):
        self.playwright.locator(self.INPUT_PASSWORD).fill(password)

    def click_login_button(self):
        self.playwright.locator(self.CLICK_BUTTON).click()

    def get_error_message(self):
        return self.playwright.locator(self.ERROR_MESSAGE).text

    def valid_login(self):
        self.get_login_page()
        self.fill_user_name('standard_user')
        self.fill_password('secret_sauce')
        self.click_login_button()
        assert "inventory" in self.playwright.url, "Ошибка: страница инвентори не открылась"



