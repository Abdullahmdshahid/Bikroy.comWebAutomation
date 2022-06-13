import time

from tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from sample_data.all_information_data import LoginData


class Test_05(BaseTestClass):
    def test05(self):
        home_page = HomePage(driver=self.driver)
        home_page.click_login_button()

        login_page = LoginPage(driver=self.driver)
        login_page.click_with_email_button()
        login_page.login_with_email_and_password(LoginData.EMAIL, LoginData.PASSWORD)

        time.sleep(3)
        home_page.click_my_account_button()

        dashboard_page = DashboardPage(driver=self.driver)
        dashboard_page.click_my_membership_button()
        assert "membership" in dashboard_page.get_url(), "Membership button doesn't click"

        dashboard_page.click_favorites_button()
        assert "favorite" in dashboard_page.get_url(), "Favorite button doesn't click"

        dashboard_page.click_settings_button()
        assert "setting" in dashboard_page.get_url(), "Setting button doesn't click"

        dashboard_page.click_my_profile_button()
        assert "resume" in dashboard_page.get_url(), "Profile button doesn't click"
