from pages.CheckoutPage import Checkout


class TestCheckoutPage:

    def test_fill_in_the_checkout_form_with_valid_data(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        assert checkout_page.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    def test_click_continue_without_filling_in_the_first_name(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("", "Test", "12345")
        checkout_page.click_continue()
        error_message = checkout_page.find(checkout_page.Error_message_locator)
        assert error_message.text == "Error: First Name is required"

    def test_click_continue_without_filling_in_the_last_name(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "", "12345")
        checkout_page.click_continue()
        error_message = checkout_page.find(checkout_page.Error_message_locator)
        assert error_message.text == "Error: Last Name is required"
        