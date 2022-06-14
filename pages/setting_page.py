from pages.base_page import BasePage
from utils.locators import SettingPageLocators


class SettingPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = SettingPageLocators

    def add_setting_profile_details(self, name, location, sublocation):
        name_text_box = self.find_element(*self.locator.NAME_TEXT_BOX)
        name_text_box.send_keys(name)

        # collecting all city names
        all_dropdown_cities_box = self.find_elements(*self.locator.DROPDWON_ALL_CITIES_BOX)

        # checking sample city match or not
        for city in all_dropdown_cities_box:
            if city.text == location:
                city.click()

        # collecting all sub location
        all_dropdown_sublocation_box = self.find_elements(*self.locator.DROPDOWN_ALL_SUB_LOCATIONS_BOX)
        # checking sample sublocation match or not
        for sublc in all_dropdown_sublocation_box:
            if sublc.text == sublocation:
                sublc.click()

        update_details_button = self.find_element(*self.locator.UPDATE_DETAILS_BUTTON)
        update_details_button.click()

    def get_changed_details_successfully_text(self):
        text = self.find_element(*self.locator.CHANGED_DETAILS_SUCCESSFULLY_TEXT).text
        return text

    def change_password(self, oldpassword, newpassword, confirmpassword):
        old_password_text_box = self.find_element(*self.locator.CURRENT_PASSWORD_TEXT_BOX)
        old_password_text_box.send_keys(oldpassword)
        new_password_text_box = self.find_element(*self.locator.NEW_PASSWORD_TEXT_BOX)
        new_password_text_box.send_keys(newpassword)
        confirm_password_text_box = self.find_element(*self.locator.CONFIRM_NEW_PASSWORD_TEXT_BOX)
        confirm_password_text_box.send_keys(confirmpassword)
        change_password_button = self.find_element(*self.locator.CHANGE_PASSWORD_BUTTON)
        change_password_button.click()

    def get_changed_password_successfully_text(self):
        text = self.find_element(*self.locator.CHANGED_PASSWORD_SUCCESSFULLY_TEXT).text
        return text

    def click_delete_account_button(self):
        button = self.find_element(*self.locator.DELETE_ACCOUNT_BUTTON)
        button.click()
