import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.base_test import BaseTestClass
from sample_data.all_information_data import LoginData


class Test_03(BaseTestClass):
    def test_03(self):
        home_page = HomePage(driver=self.driver)
        home_page.click_login_button()

        time.sleep(2)
        login_page = LoginPage(driver=self.driver)
        login_page.click_with_email_button()

        login_page.login_with_email_and_password(LoginData.EMAIL, LoginData.PASSWORD, LoginData.NEW_PASSWORD)
        time.sleep(3)
        text = home_page.get_my_account_button_text()
        assert "My account" in text, "Login failed"
