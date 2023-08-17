from selenium import webdriver

# chrome -> chrome options
# Chrome options -> chrome with the extension, window size, proxy, JS disabled


def test_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    extension_path = "D:/Backup_sep/Ramya_Official/pythonProject1/AdBlock.crx"
    chrome_options.add_extension(extension_path)

    # 1. Headless mode: Run chrome in headless mode(without GUI)
    chrome_options.add_argument("--headless=new")

    # with UI - slow and consume lot of resource, you can see the test -100-
    # without UI - headless - fast, it will consume less resources, you can't see the test - > 10,000 -

    driver = webdriver.Chrome(chrome_options)
    # driver.maximize_window()
    driver.get("https://app.vwo.com")