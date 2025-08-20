from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    # --------------------
    # FIND METHODS
    # --------------------

    def find(self, locator, timeout=10):
        """Wait until element is visible and return it."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return None

    def find_all(self, locator, timeout=10):
        """Wait until all elements are visible and return them."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    # --------------------
    # ACTION METHODS
    # --------------------

    def enter(self, locator, text: str, timeout=10):
        element = self.find(locator, timeout)
        if not element:
            raise Exception(f"Cannot enter text, element not found: {locator}")
        element.clear()
        element.send_keys(text)

    def click(self, locator, timeout=10):
        try:
            element = self.find(locator, timeout)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            raise Exception(f"Element not clickable: {locator}")

    def get_text(self, locator, timeout=10):
        element = self.find(locator, timeout)
        return element.text if element else ""

    # --------------------
    # CHECK METHODS
    # --------------------

    def is_displayed(self, locator, timeout=5) -> bool:
        element = self.find(locator, timeout)
        return element.is_displayed() if element else False

    def is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 5)
        try:
            return wait.until(EC.element_to_be_clickable(locator))
        except (NoSuchElementException, TimeoutException):
            return False

    # --------------------
    # WAIT HELPERS
    # --------------------

    def wait_until_element_is_not_visible(self, time, locator):
        wait = WebDriverWait(self.driver, time)
        try:
            return wait.until(EC.invisibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False

    def wait_for_text_to_be_present(self, locator, text):
        wait = WebDriverWait(self.driver, 5)

        try:
            return wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False

    # --------------------
    # OTHER UTILITIES
    # --------------------

    @property
    def current_url(self) -> str:
        self.driver.implicitly_wait(10)
        return self.driver.current_url

    def switch_to_a_new_tab(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def accept_alert(self):
        WebDriverWait(self.driver, 5)
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.wait_until_element_is_not_visible(10, alert)
        except NoAlertPresentException:
            pass
