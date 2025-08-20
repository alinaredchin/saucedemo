from pages.CartPage import Cart


class TestCartPage:

    def test_product_is_shown_in_the_cart_after_being_added(self, driver):
        cart_page = Cart(driver)
        cart_page.open_the_link()
        cart_page.login("standard_user", "secret_sauce")
        cart_page.add_to_cart()
        cart_page.go_to_cart()
        assert cart_page.is_displayed(cart_page.Cart_item_locator)

    def test_continue_shopping_btn_redirects_to_products_list(self, driver):
        cart_page = Cart(driver)
        cart_page.open_the_link()
        cart_page.login("standard_user", "secret_sauce")
        cart_page.add_to_cart()
        cart_page.go_to_cart()
        cart_page.is_displayed(cart_page.Cart_item_locator)
        cart_page.click(cart_page.Continue_shopping_button_locator)
        current_url = cart_page.get_current_url()
        assert current_url == "https://www.saucedemo.com/inventory.html"

    def test_remove_btn_removes_product_from_the_cart(self, driver):
        cart_page = Cart(driver)
        cart_page.open_the_link()
        cart_page.login("standard_user", "secret_sauce")
        cart_page.add_to_cart()
        cart_page.go_to_cart()
        cart_page.is_displayed(cart_page.Cart_item_locator)
        cart_page.click(cart_page.Remove_button_locator)
        assert cart_page.verify_element_not_visible(cart_page.Cart_item_locator)

    def test_clicking_on_the_item_name_shows_product_details(self, driver):
        cart_page = Cart(driver)
        cart_page.open_the_link()
        cart_page.login("standard_user", "secret_sauce")
        cart_page.add_to_cart()
        cart_page.go_to_cart()
        cart_page.is_displayed(cart_page.Cart_item_locator)
        cart_page.open_product_details()
        assert cart_page.is_displayed(cart_page.Product_details_container_locator)
