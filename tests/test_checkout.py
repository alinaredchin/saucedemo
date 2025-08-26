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

    def test_clicking_on_the_cart_badge_from_the_checkout_form_redirects_to_the_cart(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.click_on_the_cart_icon()
        assert checkout_page.current_url == "https://www.saucedemo.com/cart.html"

    def test_click_cancel_from_the_second_checkout_step_redirects_to_products_list(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.click_cancel()
        assert checkout_page.current_url == "https://www.saucedemo.com/inventory.html"

    def test_clicking_on_the_item_name_shows_product_details(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.open_product_details()
        assert checkout_page.is_displayed(checkout_page.Product_details_container_locator)

    def test_clicking_back_to_products_btn_redirects_to_products_list(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.open_product_details()
        checkout_page.click_back_to_products()
        assert checkout_page.current_url == "https://www.saucedemo.com/inventory.html"

    def test_remove_btn_changes_to_add_to_cart_in_the_checkout_page(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.open_product_details()
        checkout_page.remove_item()
        assert checkout_page.verify_element_not_visible(checkout_page.Remove_button_locator)

    def test_clicking_finish_completes_checkout(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.finish_checkout()
        assert checkout_page.current_url == "https://www.saucedemo.com/checkout-complete.html"

    def test_checkout_complete_container_is_displayed_after_finishing_checkout(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.finish_checkout()
        assert checkout_page.is_displayed(checkout_page.Checkout_complete_container_locator)

    def test_back_home_btn_redirects_to_the_homepage(self, driver):
        checkout_page = Checkout(driver)
        checkout_page.open_the_link()
        checkout_page.login("standard_user", "secret_sauce")
        checkout_page.add_to_cart()
        checkout_page.go_to_cart()
        checkout_page.go_to_checkout()

        checkout_page.fill_in_the_form("Test", "Test", "12345")
        checkout_page.click_continue()
        checkout_page.finish_checkout()
        checkout_page.go_back_to_home_page()
        assert checkout_page.current_url == "https://www.saucedemo.com/inventory.html"
