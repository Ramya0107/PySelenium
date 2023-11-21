import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_hrm_login():
    driver = webdriver.Chrome()
    logger = logging.getLogger(__name__)
    driver.maximize_window()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    time.sleep(5)
    logger.info("url loaded")
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Hacker@4321")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Add").click()

    wait = WebDriverWait(driver, timeout=30)

