import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_shadow_dom(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//img[@class='sgpb-popup-close-button-6']").click()
    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")
    driver.execute_script("arguments[0].scrollIntoView(true);", div)

    pizza = driver.execute_script(
        "return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector("
        "'input#pizza');")
    pizza.send_keys("Farmhouse")
    # href = driver.execute_script(
    #     "return document.querySelector('div.jackPart').shadowRoot.querySelector('a#href')")

    time.sleep(4)
