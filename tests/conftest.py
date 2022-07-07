import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope="class")
# setup the webdriver
def setup(request):

    chromeService = Service(os.getcwd() + r"\ChromeDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=chromeService)

    driver.get("https://bikroy.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
