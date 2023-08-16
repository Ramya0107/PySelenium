# call the selenium
# use the selenium commands - navigate to url
# If you are using selenium < 4, we use to set the driver path
# If you are using selenium > 4, driver path is not needed, they will handle automatically


# selenium code(python, java) -> API HTTP request -> ChromeDriver /GeckoDriver -> Chrome / Firefox

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    print(browser.session_id)
    yield browser  # browser will be available only when this is been executing
    # return browser # value will be stored


def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert "Login - VWO" == driver.title
