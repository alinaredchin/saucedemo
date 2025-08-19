from pages.ProductsPage import Products
from selenium.webdriver.common.by import By


class Cart(Products):

    Cart_item_locator = (By.XPATH, "//div[@class='cart_item']")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_alert(self):
        super().accept_alert()

    def add_to_cart(self):
        super().add_to_cart()
