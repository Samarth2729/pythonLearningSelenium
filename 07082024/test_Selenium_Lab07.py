import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.close()
    # Close will close the current window or tab
    # session id != null
    #  It will not close other tabs

    time.sleep(10)

    driver.quit()
    # Close All the tabs
    # session id = null

