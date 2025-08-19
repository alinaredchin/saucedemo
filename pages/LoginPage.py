from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

expected_url = "https://www.saucedemo.com/inventory.html"


class LoginPage(BasePage):
    username_locator = (By.XPATH, '//input[@id="user-name"]')
    password_locator = (By.XPATH, "//input[@id='password']")
    login_locator = (By.XPATH, "//input[@id='login-button']")
    error_message_locator = (By.XPATH,
                             "//div[@class='error-message-container error']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_the_link(self):
        self.open("https://www.saucedemo.com/")

    def login(self, username, password):
        self.enter(self.username_locator, username)
        self.enter(self.password_locator, password)
        self.click(self.login_locator)

    @property
    def expected_url(self) -> str:
        return expected_url

    def get_current_url(self):
        return super().current_url

    def is_error_message_displayed(self) -> bool:
        return self.is_displayed(self.error_message_locator)

    def error_text_message(self):
        return self.get_text(self.error_message_locator)
