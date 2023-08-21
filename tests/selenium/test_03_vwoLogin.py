import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    loggers = logging.getLogger(__name__)
    loggers.info("Url loaded")
    time.sleep(5)
    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("SHAYAM@TTA.com")
    password_ele = driver.find_element(By.NAME, "password")
    password_ele.send_keys("Wingify@123")
    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")
    sign_in_button_ele.click()
    # if there is delay in page load
    time.sleep(5)
    assert "Dashboard" in driver.title
