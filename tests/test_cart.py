from pages.CartPage import Cart


class TestCartPage:

    def test_product_is_shown_in_the_cart_after_being_added(self, driver):
        cart_page = Cart(driver)
        cart_page.open_the_link()
        cart_page.login("standard_user", "secret_sauce")
        cart_page.add_to_cart()
        cart_page.click(cart_page.Cart_badge_locator)
        assert cart_page.is_displayed(cart_page.Cart_item_locator)
