from pages.base_page import BasePage
from utils.locators import *


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = CreateAccountPageLocators

    def create_new_account(self, name, email, password, confirmpassword):
        name_text_box = self.find_element(*self.locator.NAME_TEXTBOX)
        name_text_box.send_keys(name)
        email_text_box = self.find_element(*self.locator.EMAIL_TEXTBOX)
        email_text_box.send_keys(email)
        password_text_box = self.find_element(*self.locator.PASSWORD_TEXTBOX)
        password_text_box.send_keys(password)
        confirm_password_text_box = self.find_element(*self.locator.CONFIRM_PASSWORD_TEXTBOX)
        confirm_password_text_box.send_keys(confirmpassword)
        sign_up_button = self.find_element(*self.locator.SIGN_UP_BUTTON)
        sign_up_button.click()

