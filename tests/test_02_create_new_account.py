from tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from sample_data.all_information_data import SignUpData


class Test_02(BaseTestClass):
    def test_02(self):
        home_page = HomePage(driver=self.driver)
        home_page.click_login_button()

        login_page = LoginPage(driver=self.driver)
        login_page.click_with_email_button()
        login_page.click_sign_up_button()

        create_account_page = CreateAccountPage(driver=self.driver)
        create_account_page.create_new_account(SignUpData.NAME, SignUpData.EMAIL, SignUpData.PASSWORD, SignUpData.PASSWORD)

        assert "success" in create_account_page.get_url(), "Already have an account using this email"
