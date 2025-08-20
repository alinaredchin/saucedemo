from pages.ProductsPage import Products
from selenium.webdriver.common.by import By


class Cart(Products):

    Cart_item_locator = (By.XPATH, "//div[@class='cart_item']")
    Continue_shopping_button_locator = (By.XPATH, "//button[@name='continue-shopping']")
    Remove_button_locator = (By.XPATH, "//button[contains(@id,'remove')]")
    Item_name_locator = (By.XPATH, "//a[@id='item_4_title_link']")
    Product_details_container_locator = (By.XPATH, "//div[@class='inventory_details_container']")
    Checkout_button_locator = (By.XPATH, "//button[@id='checkout']")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_alert(self):
        super().accept_alert()

    def add_to_cart(self):
        super().add_to_cart()

    def go_to_cart(self):
        self.click(self.Cart_locator)

    def verify_element_not_visible(self, locator):
        return self.wait_until_element_is_not_visible(10, locator)

    def open_product_details(self):
        self.click(self.Item_name_locator)

    def go_to_checkout(self):
        self.click(self.Checkout_button_locator)
