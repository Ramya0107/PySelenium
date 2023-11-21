import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# import org.openqa.selenium.WebElement

def test_checkbox_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # click the checkbox which is not selected
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for c in checkboxes:
        if not c.is_selected():
            c.click()

    # uncomment below to click the 1st checkbox element
    # checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
    # checkbox.click()
    # time.sleep(10)
