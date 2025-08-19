from pages.ProductsPage import Products
from selenium.webdriver.common.by import By


class Cart(Products):

    Cart_item_locator = (By.XPATH, "//div[@class='cart_item']")
    Continue_shopping_button_locator = (
        By.XPATH, "//button[@name='continue-shopping']"
    )
    Remove_button_locator = (By.XPATH, "//button[@name='remove-sauce-labs-backpack']")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_alert(self):
        super().accept_alert()

    def add_to_cart(self):
        super().add_to_cart()

    def verify_element_not_visible(self, locator):
        return self.wait_until_element_is_not_visible(10, locator)
