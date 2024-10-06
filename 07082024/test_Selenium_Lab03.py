import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    # Option classes - What is this ?
    # customized the behaviour of the browser during automation testing
    # Chrome -> headless or UI -> hEADLESS MODE is no UI
    # diable gpe,add extensions,maximize,set window,100 other option that u can
    # Before starting the browser

    # Create Instance of Chrome Options
    chrome_option = Options()
    chrome_option.add_argument("--window-size=920*680")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com")
    time.sleep(10)
