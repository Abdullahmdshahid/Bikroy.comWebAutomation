import time
from tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage
from sample_data.all_information_data import *


class Test_07(BaseTestClass):
    def test_07(self):
        home_page = HomePage(driver=self.driver)
        home_page.click_login_button()

        time.sleep(2)
        login_page = LoginPage(driver=self.driver)
        login_page.click_with_email_button()
        login_page.login_with_email_and_password(LoginData.EMAIL, LoginData.PASSWORD, LoginData.NEW_PASSWORD)

        time.sleep(3)
        home_page.click_my_account_button()

        time.sleep(2)
        dashboard_page = DashboardPage(driver=self.driver)
        dashboard_page.click_my_profile_button()

        profile_page = ProfilePage(driver=self.driver)
        profile_page.click_create_profile_button()
        profile_page.edit_profile(ProfilePageData.NAME, ProfilePageData.PHONE, ProfilePageData.GENDER, ProfilePageData.DEATH_OF_BIRTH, ProfilePageData.CITY, ProfilePageData.SUB_LOCATION, ProfilePageData.EDUCATION, ProfilePageData.JOB, ProfilePageData.YEARS)
