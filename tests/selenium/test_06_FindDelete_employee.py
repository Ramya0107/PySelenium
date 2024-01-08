import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_find_delete():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("Hacker@4321")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)
    print("Employee - ", find_employee_status(driver, "atester"))


def find_rows_cols(driver):
    rows = len(driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div"))
    print(rows)

    cols = len(driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div[1]/div/div"))
    print(cols)
    return rows, cols


# //div[@role='table']/div[2]/div[26]/div/div[3]/following-sibling::div[3] --> chandan sign employee status
# //div[@role='table']/div[2]/div[26]/div/div[3]/following-sibling::div[3]/following-sibling::div[3]/div/button
def find_employee_status(driver, employee_name):
    rows, cols = find_rows_cols(driver)

    first_part = "//div[@role='table']/div[2]/div["
    second_part = "]/div/div["
    third_part = "]"
    employee_status = None
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if employee_name in data:
                employee_status_path = f"{dynamic_path}/following-sibling::div[3]"
                employee_status = driver.find_element(By.XPATH, employee_status_path).text
                print(f"{employee_name} employee status is {employee_status}")
                if employee_status.casefold() == "terminated":
                    delete_employee = driver.find_element(By.XPATH, f"{employee_status_path}/following-sibling::div["
                                                                    f"3]/div/button")
                    delete_employee.click()
                    print("Terminated employee data deleted")
    return employee_status
