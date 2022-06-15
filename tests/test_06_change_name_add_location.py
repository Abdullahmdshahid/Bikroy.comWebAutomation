import time
from tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.setting_page import SettingPage
from sample_data.all_information_data import *


class Test_06(BaseTestClass):
    def test_06(self):
        home_page = HomePage(driver=self.driver)
        home_page.click_login_button()

        login_page = LoginPage(driver=self.driver)
        login_page.click_with_email_button()
        login_page.login_with_email_and_password(LoginData.EMAIL, LoginData.PASSWORD)

        time.sleep(3)
        home_page.click_my_account_button()

        dashboard_page = DashboardPage(driver=self.driver)

        dashboard_page.click_settings_button()
        assert "setting" in dashboard_page.get_url(), "Setting button doesn't click"

        setting_page = SettingPage(driver=self.driver)
        setting_page.add_setting_profile_details(SettingPageData.NAME, SettingPageData.CITY, SettingPageData.SUB_LOCATION)
        assert "successfully" in setting_page.get_changed_details_successfully_text()

        setting_page.change_password(SettingPageData.CURRENT_PASSWORD, SettingPageData.NEW_PASSWORD, SettingPageData.NEW_PASSWORD)
        assert "password was changed" in setting_page.get_changed_password_successfully_text()
