import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.negative
def test_katalon_appointment_negative():
    logger = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    logger.info("url loaded")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()

    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("John Doe")
    driver.find_element(By.ID, "btn-login").click()

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed!" in error_message.text


@pytest.mark.positive
def test_katalon_appointment_positive():
    logger = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    logger.info("url loaded")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()

    driver.find_element(By.ID, "txt-username").send_keys("John Doe")

    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")

    driver.find_element(By.ID, "btn-login").click()

    Select(driver.find_element(By.ID, "combo_facility")).select_by_visible_text("Tokyo CURA Healthcare Center")

    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()
    driver.find_element(By.ID, "txt_visit_date").send_keys("10/07/2023")
    driver.find_element(By.NAME, "comment").send_keys("I have a fever with 101")

    # submit
    driver.find_element(By.ID, "btn-book-appointment").click()

    # confirmation page
    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text

    driver.find_element(By.ID, "menu-toggle").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
