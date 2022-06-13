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
