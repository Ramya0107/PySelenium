import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

# assertions after actions, scroll outer iframe and inner iframe
def test_assert():
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    textbox = driver.find_element(By.ID, "clickable")
    action.key_down(Keys.SHIFT).send_keys_to_element(textbox, "testing").perform()
    status = driver.find_element(By.ID, "click-status")
    assert status.text == "focused"
    time.sleep(3)

    textbox.clear()
    action.double_click().perform()
    assert status.text == "double-clicked"
    time.sleep(3)

    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    iframe_tag = driver.find_element(By.TAG_NAME, "iframe")

    # To scroll till iframe
    # action.scroll_to_element(iframe_tag).perform()
    # time.sleep(3)

    scrolliframe = ScrollOrigin.from_element(iframe_tag)

    # To scroll inside the iframe
    action.scroll_from_origin(scrolliframe, 0, 200).perform()
    time.sleep(3)
