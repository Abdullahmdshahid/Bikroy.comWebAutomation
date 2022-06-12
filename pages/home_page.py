from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = HomePageLocators

    def click_login_button(self):
        button = self.find_element(*self.locator.LOGIN_BUTTON)
        button.click()

    def click_my_account_button(self):
        super().wait_element(*self.locator.MY_ACCOUNT)
        button = self.find_element(*self.locator.MY_ACCOUNT)
        button.click()

    def click_chat_button(self):
        button = self.find_element(*self.locator.CHAT_BUTTON)
        button.click()

    def click_post_your_ad_button(self):
        button = self.find_element(*self.locator.POST_YOUR_AD_BUTTON)
        button.click()

    def get_my_account_button_text(self):
        text = self.find_element(*self.locator.MY_ACCOUNT).text
        return text
