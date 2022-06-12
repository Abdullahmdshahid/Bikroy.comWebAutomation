from pages.base_page import BasePage

class ChatPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
