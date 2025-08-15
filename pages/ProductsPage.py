from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage


class Products(LoginPage):

    OpenMenuBtn_locator = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    Closed_Menu_locator = (By.XPATH, "//div[@aria-hidden='true']")
    Menu_items = (By.XPATH, "//a[@class='bm-item menu-item']")
    All_items_button_locator = (By.XPATH, "//a[@id='inventory_sidebar_link']")
    About_button_locator = (By.XPATH, "//a[@id='about_sidebar_link']")
    Logout_button_locator = (By.XPATH, "//a[@id='logout_sidebar_link']")
    Reset_app_state_locator = (By.XPATH, "//a[@id='reset_sidebar_link']")
    Filter_locator = (By.XPATH, "//span[@class='select_container']")
    Filter_elements = (
        By.XPATH, "//select[@class='product_sort_container']/option")
    Selected_filter_option = (By.XPATH, "//span[@class='active_option']")
    Products_names_locator = (By.XPATH, "//div[@class='inventory_item_name ']")
    AZ_filter_option_locator = (By.XPATH, "//option[@value='az']")
    ZA_filter_option_locator = (By.XPATH, "//option[@value='za']")
    LH_filter_option_locator = (By.XPATH, "//option[@value='lohi']")
    HL_filter_option_locator = (By.XPATH, "//option[@value='hilo']")
    Products_price_locator = (By.XPATH, "//div[@class='inventory_item_price']")
    Add_to_cart_locator = (By.XPATH, "//button[contains(@id,'sauce-labs-backpack')]")
    Cart_badge_locator = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_alert(self):
        super().accept_alert()

    def is_menu_hidden(self):
        self.accept_alert()
        return self.find(self.Closed_Menu_locator)

    def expand_menu(self):
        self.accept_alert()
        self.click(self.OpenMenuBtn_locator)
        return self.find_all(self.Menu_items)

    def get_menu_items(self):
        items = self.find_all(self.Menu_items)
        return [a.text.strip() for a in items]

    def expand_filters(self):
        self.accept_alert()
        self.click(self.Filter_locator)

    def get_filter_options(self):
        filter_elements = self.find_all(self.Filter_elements)
        return [el.text.strip() for el in filter_elements]

    def get_product_names(self):
        product_names = self.find_all(self.Products_names_locator)
        return [el.text for el in product_names]

    def get_product_price(self):
        product_prices_text = self.find_all(self.Products_price_locator)
        prices_text = [el.text for el in product_prices_text]
        return [float(price.replace("$", "")) for price in prices_text]

    def add_to_cart(self):
        self.accept_alert()
        self.click(self.Add_to_cart_locator)
