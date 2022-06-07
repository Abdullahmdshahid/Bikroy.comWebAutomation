import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
# setup the webdriver
def setup(request):

    chromeService = Service("F:\ChromeDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=chromeService)

    driver.get("https://bikroy.com/bn")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
