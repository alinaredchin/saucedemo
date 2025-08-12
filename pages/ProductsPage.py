from selenium.webdriver.common.by import By
from pages import LoginPage


class Products(LoginPage):

    Products_list_locator = (By.XPATH, "//div[@class='inventory_list']")
    Inventory_item_locator = (By.XPATH, "//div[@class='inventory_item']")

    def __init__(self, driver):
        super().__init__(driver)
