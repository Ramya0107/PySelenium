import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    firstName = driver.find_element(By.NAME, "firstname")

    # create object of Action Chains class
    action = ActionChains(driver)
    action.key_down(Keys.SHIFT).send_keys_to_element(firstName, "testing").key_up(Keys.SHIFT).perform()
    print("action 1 passed")
    time.sleep(3)

    # link = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    # action.context_click(link).perform()
    test_drag_drop(driver, action)
    test_mouse(driver, action)



def test_drag_drop(driver, action):
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    drag_from = driver.find_element(By.XPATH, "//div[@id='draggable']")
    drag_to = driver.find_element(By.XPATH, "//div[@id='droppable']")
    action.drag_and_drop(drag_from, drag_to).perform()
    action.move_to_element(driver.find_element(By.ID, "hover")).perform()
    print("action 2 passed")
    time.sleep(3)


def test_mouse(driver, action):
    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    textBox = driver.find_element(By.ID, "textInput")
    action.key_down(Keys.SHIFT).send_keys_to_element(textBox, "testing").key_up(Keys.SHIFT).perform()
    print("action 3 passed")
    time.sleep(3)



