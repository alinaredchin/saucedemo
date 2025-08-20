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
