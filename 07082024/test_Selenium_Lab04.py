import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    # Headless
    # - No Ui
    # - Its Fast - real browser but no ui so
    # less memory-you can run 5000TC

    # Non-Headless
    # - UI
    # - slow
    # - High Memory


    # Create Instance of Chrome Options
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com")
    time.sleep(10)