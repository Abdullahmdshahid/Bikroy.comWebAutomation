from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGIN_BUTTON = (By.XPATH, '//body[@class=" bgwhite"]/div[1]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/ul[2]/li[2]/div[1]/a[1]')
    MY_ACCOUNT = (By.XPATH, '//body[@class=" bgwhite"]/div[1]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/ul[2]/li[2]/div[1]/a[1]')
    CHAT_BUTTON = (By.XPATH, '//body[@class=" bgwhite"]/div[1]/div/div[2]/div[2]/div/nav[1]/div[1]/ul[2]/li[1]/div[1]/a')
    POST_YOUR_AD_BUTTON = (By.XPATH, '//body[@class=" bgwhite"]/div[1]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/ul[2]/li[3]/a[1]')


class LoginPageLocators(object):
    CONTINUE_WITH_EMAIL_BUTTON = (By.CSS_SELECTOR, 'button[class*="email"]')
    EMAIL_TEXTBOX = (By.ID, "input_email")
    PASSWORD_TEXTBOX = (By.ID, "input_password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    LOGIN_FAILED_TEXT = (By.CSS_SELECTOR, 'div[class*="error"] span')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[class*="email-signup"]')


class CreateAccountPageLocators(object):
    NAME_TEXTBOX = (By.ID, "input_name")
    EMAIL_TEXTBOX = (By.ID, "input_email")
    PASSWORD_TEXTBOX = (By.ID, "input_password")
    CONFIRM_PASSWORD_TEXTBOX = (By.ID, "input_password-confirm")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[class*="email-signup"]')


class DashboardPageLocators(object):
    MY_MEMBERSHIP_BUTTON = (By.CSS_SELECTOR, 'li[class*="membership"] a')
    FAVORITES_BUTTON = (By.CSS_SELECTOR, 'a[href*="favorite-ads"]')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[href*="setting"]')
    MY_PROFILE_BUTTON = (By.LINK_TEXT, "My Profile")


class SettingPageLocators(object):
    NAME_TEXT_BOX = (By.ID, "profile-name")
    DROPDWON_ALL_CITIES_BOX = (By.XPATH, '//optgroup[@label="Cities"]/option')
    DROPDOWN_ALL_SUB_LOCATIONS_BOX = (By.XPATH, '//select[@id="location2"]/option')
    UPDATE_DETAILS_BUTTON = (By.XPATH, '//span[contains(text(),"Update details")]/parent::button')
    CURRENT_PASSWORD_TEXT_BOX = (By.ID, "old")
    NEW_PASSWORD_TEXT_BOX = (By.ID, "password")
    CONFIRM_NEW_PASSWORD_TEXT_BOX = (By.ID, "confirm")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//span[contains(text(),'Change password')]/parent::button")
    DELETE_ACCOUNT_BUTTON = (By.LINK_TEXT, "Delete account")
    LOG_OUT_BUTTON = (By.LINK_TEXT, "Log out")
    CHANGED_DETAILS_SUCCESSFULLY_TEXT = (By.CLASS_NAME, "ui-alert-content")
    CHANGED_PASSWORD_SUCCESSFULLY_TEXT = (By.CLASS_NAME, "ui-alert-content")


class ProfilePageLocators(object):
    CREATE_PROFILE_BUTTON = (By.LINK_TEXT, "Create Profile")
    UPLOAD_IMAGE_BUTTON = (By.ID, "image")
    NAME_TEXT_BOX = (By.ID, "fields-name-value")
    PHONE_TEXT_BOX = (By.ID, "fields-phone_number-value")
    GENDER_DROPDOWN = (By.XPATH, '//select[@id="fields-gender-value"]/option')
    DATE_OF_BIRTH = (By.ID, "fields-birth_date-value")
    LOCATION_DROPDOWN_BOX = (By.XPATH, '//optgroup[@label="Cities"]/option')
    SUBLOCATION_DROPDOWN_BOX = (By.XPATH, '//select[@id="fields-living_in"]/option')
    EDUCATION_DROPDOWN_BOX = (By.XPATH, '//select[@id="fields-education_level-value"]/option')
    CURRENT_JOB_DROPDOWN_BOX = (By.XPATH, '//select[@id="fields-current_role-value"]/option')
    YEAR_OF_EXPERIENCE_TEXT_BOX = (By.ID, 'fields-experience-value')
    CONTINUE_BUTTON = (By.NAME, 'post')

