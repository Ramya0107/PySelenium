from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button1 = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    button1.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("button1 result" + driver.find_element(By.XPATH, "//p[@id='result']").text)

    button2 = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
    button2.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.dismiss()
    print("button2 result" + driver.find_element(By.XPATH, "//p[@id='result']").text)

    button3 = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
    button3.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Bruno")
    alert.accept()
    print("button3 result" + driver.find_element(By.XPATH, "//p[@id='result']").text)
