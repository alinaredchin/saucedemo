from selenium.webdriver.common.by import By

from pages.CartPage import Cart


class Checkout(Cart):

    First_name_locator = (By.XPATH, "//input[@id='first-name']")
    Last_name_locator = (By.XPATH, "//input[@id='last-name']")
    Postal_code_locator = (By.XPATH, "//input[@id='postal-code']")
    Continue_button_locator = (By.XPATH, "//input[@id='continue']")
    Cancel_button_locator = (By.XPATH, "//input[@id='cancel']")
    Error_message_locator = (By.XPATH, "//div[contains(@class,'error-message')]")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_the_form(self, first_name, last_name, postal_code):
        self.enter(self.First_name_locator, first_name)
        self.enter(self.Last_name_locator, last_name)
        self.enter(self.Postal_code_locator, postal_code)

    def click_continue(self):
        self.click(self.Continue_button_locator)

    def click_cancel(self):
        self.click(self.Cancel_button_locator)

    def click_on_the_cart_icon(self):
        self.click(self.Cart_badge_locator)
