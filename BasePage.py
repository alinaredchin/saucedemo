from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        self.wait_until_element_is_visible(10, locator)
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        self.wait_until_element_is_visible(10, locator)
        return self.driver.find_elements(*locator)

    def enter(self, locator, text: str):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.wait_until_element_is_visible(10, locator)
        self.find(locator).click()

    def wait_until_element_is_visible(self, time, locator):
        wait = WebDriverWait(self.driver, time)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False

    def wait_until_element_is_not_visible(self, time, locator):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_all_elements_are_visible(self, time, locator):
        wait = WebDriverWait(self.driver, time)
        try:
            return wait.until(EC.visibility_of_all_elements_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False

    @property
    def current_url(self) -> str:
        self.driver.implicitly_wait(10)
        return self.driver.current_url

    def get_text(self, locator):
        self.wait_until_element_is_visible(10, locator)
        return self.find(locator).text

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 5)
        try:
            return wait.until(EC.element_to_be_clickable(locator))
        except (NoSuchElementException, TimeoutException):
            return False

    def switch_to_a_new_tab(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def accept_alert(self):
        WebDriverWait(self.driver, 5)
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
