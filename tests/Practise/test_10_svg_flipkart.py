import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_svg(driver):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys("Computer")
    svg_icon = driver.find_element(By.XPATH, "//*[local-name()='svg']")
    action = ActionChains(driver)
    action.move_to_element(svg_icon).click().perform()
    time.sleep(3)
