from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtable_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    # table = driver.find_elements(By.XPATH, "//table[@id='customers']")

    # Finding num of rows
    rows = len(driver.find_elements(By.XPATH, "//table[contains(@id,'custo')]/tbody/tr"))
    print(rows)

    # Finding num of columns
    columns = len(driver.find_elements(By.XPATH, "//table[contains(@id,'custo')]/tbody/tr[2]/td"))
    print(columns)

    first_part = "//table[contains(@id,'custo')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    # getting the text present in each cell
    for i in range(2, rows+1):
        for j in range(1, columns+1):
            data_xpath = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, data_xpath).text
            # print(data, end=" ")
            if "Roland Mendel" in data:
                country_xpath = f"{data_xpath}/following-sibling::td"
                country = driver.find_element(By.XPATH, country_xpath).text
                print(f"Roland Mendel is in {country}")
                break

    # Dynamic table
    driver.get("https://awesomeqa.com/webtable1.html")
    table = driver.find_element(By.XPATH, "//table[@class='tsc_table_s13']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        col_table = row.find_elements(By.TAG_NAME, "td")
        for e in col_table:
            if "UAE" in e.text:
                print("Yes")
