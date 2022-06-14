import time
from tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.chat_page import ChatPage
from sample_data.all_information_data import LoginData


class Test_04(BaseTestClass):
    def test_04(self):
        home_page = HomePage(driver=self.driver)
        home_page.click_login_button()

        login_page = LoginPage(driver=self.driver)
        login_page.click_with_email_button()
        login_page.login_with_email_and_password(LoginData.EMAIL, LoginData.PASSWORD)

        time.sleep(3)
        home_page.click_chat_button()
        chat_page = ChatPage(driver=self.driver)
        assert "chat" in chat_page.get_url(), "Chat button doesn't click"
