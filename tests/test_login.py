from pages.LoginPage import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_the_link()
        login_page.login("standard_user", "secret_sauce")
        expected_url = login_page.expected_url
        current_url = login_page.get_current_url()

        assert current_url == expected_url

    def test_login_with_invalid_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open_the_link()
        login_page.login("standard_user1", "secret_sauce")
        login_page.is_error_message_displayed()
        text_message = login_page.error_text_message()

        assert text_message == ("Epic sadface: Username and password do not "
                                "match any user in this service")

    def test_login_with_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_the_link()
        login_page.login("standard_user", "secret_sauce1")
        login_page.is_error_message_displayed()
        text_message = login_page.error_text_message()

        assert text_message == ("Epic sadface: Username and password do not "
                                "match any user in this service")

    def test_login_with_empty_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open_the_link()
        login_page.login("", "secret_sauce1")
        login_page.is_error_message_displayed()
        text_message = login_page.error_text_message()

        assert text_message == "Epic sadface: Username is required"

    def test_login_with_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_the_link()
        login_page.login("standard_user", "")
        login_page.is_error_message_displayed()
        text_message = login_page.error_text_message()

        assert text_message == "Epic sadface: Password is required"
