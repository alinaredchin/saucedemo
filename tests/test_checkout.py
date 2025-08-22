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
        error_message = checkout_page.find_visible(checkout_page.Error_message_locator)
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
        error_message = checkout_page.find_visible(checkout_page.Error_message_locator)
        assert error_message.text == "Error: Last Name is required"

    def test_click_continue_without_filling_in_the_postal_code(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "")
        checkout_page.click_continue()
        error_message = checkout_page.find_visible(checkout_page.Error_message_locator)
        assert error_message.text == "Error: Postal Code is required"

    def test_click_cancel_without_filling_in_the_checkout_form(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.click_cancel()
        cart_url = "https://www.saucedemo.com/cart.html"
        assert checkout_page.current_url == cart_url

    def test_go_back_to_cart_from_the_checkout_form(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.return_to_previous_page()
        assert checkout_page.current_url == "https://www.saucedemo.com/cart.html"
