import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    time.sleep(10)