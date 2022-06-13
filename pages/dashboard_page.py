from pages.base_page import BasePage
from utils.locators import DashboardPageLocators


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = DashboardPageLocators

    def click_my_membership_button(self):
        button = self.find_element(*self.locator.MY_MEMBERSHIP_BUTTON)
        button.click()

    def click_favorites_button(self):
        button = self.find_element(*self.locator.FAVORITES_BUTTON)
        button.click()

    def click_settings_button(self):
        button = self.find_element(*self.locator.SETTINGS_BUTTON)
        button.click()

    def click_my_profile_button(self):
        button = self.find_element(*self.locator.MY_PROFILE_BUTTON)
        button.click()
