from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webTable_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    table = driver.find_elements(By.XPATH, "//table[@id='customers']")

