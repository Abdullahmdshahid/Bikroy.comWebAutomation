from pages.base_page import BasePage
from utils.locators import *


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = LoginPageLocators

    def click_with_email_button(self):
        super().wait_element(*self.locator.CONTINUE_WITH_EMAIL_BUTTON)
        button = self.driver.find_element(*self.locator.CONTINUE_WITH_EMAIL_BUTTON)
        button.click()

    def login_with_email_and_password(self, email, password):
        email_text_box = self.find_element(*self.locator.EMAIL_TEXTBOX)
        email_text_box.send_keys(email)
        password_text_box = self.find_element(*self.locator.PASSWORD_TEXTBOX)
        password_text_box.send_keys(password)
        login_button = self.find_element(*self.locator.LOGIN_BUTTON)
        login_button.click()

    def get_login_failed_text(self):
        super().wait_element(*self.locator.LOGIN_FAILED_TEXT)
        text = self.find_element(*self.locator.LOGIN_FAILED_TEXT).text
        return text


