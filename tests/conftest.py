from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chromeService = Service("F:\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=chromeService)

driver.get("https://bikroy.com/bn")
driver.maximize_window()
