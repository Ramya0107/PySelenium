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
def test_svg_maps(driver):
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    action = ActionChains(driver)
    time.sleep(3)
    state_label = driver.find_elements(By.XPATH, "//*[local-name()='svg']/*[local-name()='g']/*[local-name()='g']/*["
                                               "local-name()='g']/*[local-name()='path']")
    print("total states", len(state_label))
    for state in state_label:
        state_name = state.get_attribute("aria-label")
        print(state_name)
        time.sleep(1)
        if state_name == "Tamil Nadu  ":
            action.move_to_element(state).click().perform()
            time.sleep(3)

