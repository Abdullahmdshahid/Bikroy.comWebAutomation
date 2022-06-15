import os
import time
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = ProfilePageLocators

    def click_create_profile_button(self):
        button = self.find_element(*self.locator.CREATE_PROFILE_BUTTON)
        button.click()

    def edit_profile(self, name, phone, gender, birthdate, location, sublocation, education, job, years):
        input_image = self.find_element(*self.locator.UPLOAD_IMAGE_BUTTON)
        input_image.send_keys(os.getcwd() + r"\sample_data\profile_pic_demo.png")
        time.sleep(3)
        name_text_box = self.find_element(*self.locator.NAME_TEXT_BOX)
        name_text_box.clear()
        name_text_box.send_keys(name)
        phone_text_box = self.find_element(*self.locator.PHONE_TEXT_BOX)
        phone_text_box.clear()
        phone_text_box.send_keys(phone)
        # collect all gender
        genders_dropdown_box = self.find_elements(*self.locator.GENDER_DROPDOWN)
        # checking gender match with sample
        for gender_box in genders_dropdown_box:
            if gender_box.text == gender:
                gender_box.click()

        date_of_birth_box = self.find_element(*self.locator.DATE_OF_BIRTH)
        date_of_birth_box.clear()
        date_of_birth_box.send_keys(birthdate)
        date_of_birth_box.send_keys(Keys.ENTER)

        # collecting all city names
        all_dropdown_cities_box = self.find_elements(*self.locator.LOCATION_DROPDOWN_BOX)

        # checking sample city match or not
        for city in all_dropdown_cities_box:
            if city.text == location:
                city.click()

        # collecting all sub location
        all_dropdown_sublocation_box = self.find_elements(*self.locator.SUBLOCATION_DROPDOWN_BOX)
        # checking sample sublocation match or not
        for sublc in all_dropdown_sublocation_box:
            if sublc.text == sublocation:
                sublc.click()

        # collecting all education
        educations_dropdown_box = self.find_elements(*self.locator.EDUCATION_DROPDOWN_BOX)
        # checking sample data match with education or not
        for education_box in educations_dropdown_box:
            if education_box.text == education:
                education_box.click()

        # collecting all job
        jobs_dropdown_box = self.find_elements(*self.locator.CURRENT_JOB_DROPDOWN_BOX)
        # checking sample data match or not
        for job_box in jobs_dropdown_box:
            if job_box.text == job:
                job_box.click()

        years_of_experience_text_box = self.find_element(*self.locator.YEAR_OF_EXPERIENCE_TEXT_BOX)
        years_of_experience_text_box.clear()
        years_of_experience_text_box.send_keys(years)

        submit_button = self.find_element(*self.locator.CONTINUE_BUTTON)
        submit_button.click()
