import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
   # Incignito Mode
   # Create Instance of Chrome Options
    chrome_option = Options()
    chrome_option.add_argument("--Incognito")
    # chrome_option.add_argument("--disable-infobar") now day it willnot work
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com")
    time.sleep(10)