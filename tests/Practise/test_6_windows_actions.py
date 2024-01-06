import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_windows_actions():
    driver = webdriver.Chrome()
    URL = "https://the-internet.herokuapp.com/windows"
    driver.get(URL)
    driver.maximize_window()

    # main_window_handle = driver.current_window_handle
    # print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            child_window = handle
            print(handle, "this is a new/child window")
        else:
            parent_window = handle
            print(handle, "this is a parent window")

    # driver.switch_to.window(main_window_handle)
    driver.switch_to.window(parent_window)

    time.sleep(10)