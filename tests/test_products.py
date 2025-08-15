from pages.ProductsPage import Products


class TestProducts:

    def test_side_menu_is_hidden_by_default(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        assert products_page.is_menu_hidden()

    def test_side_menu_items_names(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_menu()
        expected_menu_items = [
            "All Items", "About", "Logout", "Reset App State"]
        actual_menu_items = products_page.get_menu_items()
        assert actual_menu_items == expected_menu_items

    def test_redirection_of_about_link(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_menu()
        products_page.is_displayed(products_page.About_button_locator)
        products_page.click(products_page.About_button_locator)
        expected_url = "https://saucelabs.com/"
        current_url = products_page.get_current_url()
        assert expected_url == current_url

    def test_redirection_of_logout_button(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_menu()
        products_page.is_displayed(products_page.Logout_button_locator)
        products_page.click(products_page.Logout_button_locator)
        expected_url = "https://www.saucedemo.com/"
        current_url = products_page.get_current_url()
        assert expected_url == current_url

    def test_default_filter_option(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_filters()
        selected_filter = products_page.find(
            products_page.Selected_filter_option)
        assert selected_filter.text == "Name (A to Z)"

    def test_filter_options(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_filters()
        products_page.get_filter_options()
        expected_filter_options = [
            "Name (A to Z)", "Name (Z to A)",
            "Price (low to high)", "Price (high to low)"]
        actual_filter_options = products_page.get_filter_options()
        assert expected_filter_options == actual_filter_options

    def test_filter_az(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_filters()
        products_page.click(products_page.AZ_filter_option_locator)
        expected_product_names = products_page.get_product_names()
        actual_product_names = products_page.get_product_names()
        assert sorted(expected_product_names) == actual_product_names, (
            f'Products not sorted A-Z: {actual_product_names}')

    def test_filter_za(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_filters()
        products_page.click(products_page.ZA_filter_option_locator)
        expected_product_names = products_page.get_product_names()
        actual_product_names = products_page.get_product_names()
        assert sorted(
            expected_product_names, reverse=True
        ) == actual_product_names, (
            f'Products not sorted A-Z: {actual_product_names}')

    def test_filter_high_low_price(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_filters()
        products_page.click(products_page.HL_filter_option_locator)
        expected_product_price_order = products_page.get_product_price()
        actual_product_price_order = products_page.get_product_price()
        assert sorted(
            expected_product_price_order, reverse=True
        ) == actual_product_price_order, (
            f'Products not sorted H-L: {actual_product_price_order}')

    def test_filter_low_high_price(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.expand_filters()
        products_page.click(products_page.LH_filter_option_locator)
        expected_product_price_order = products_page.get_product_price()
        actual_product_price_order = products_page.get_product_price()
        assert sorted(
            expected_product_price_order
        ) == actual_product_price_order, (
            f'Products not sorted L-H: {actual_product_price_order}')

    def test_add_to_cart_button(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.add_to_cart()
        assert products_page.wait_for_text_to_be_present(
            products_page.Add_to_cart_locator, "Remove")

    def test_cart_icon_shows_number_of_products_added(self, driver):
        products_page = Products(driver)
        products_page.open_the_link()
        products_page.login("standard_user", "secret_sauce")
        products_page.add_to_cart()
        assert products_page.is_displayed(products_page.Cart_badge_locator)
