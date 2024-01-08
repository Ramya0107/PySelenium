import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    url = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(url)
    js_exe = driver.execute_script
    add_button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    for i in range(3):
        js_exe("arguments[0].click()", add_button)
        time.sleep(3)

    delete_button_path = "//button[@class='added-manually']"
    total_del_button = len(driver.find_elements(By.XPATH, delete_button_path))
    if total_del_button > 2:
        driver.find_element(By.XPATH, f"{delete_button_path}[{total_del_button}]").click()
        time.sleep(3)
