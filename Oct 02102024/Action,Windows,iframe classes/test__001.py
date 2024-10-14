# Action Classes

# ActionChains class provides a way to perform complex user interactions
# such as mouse movements, keyboard actions, and context menus.
# This is useful for doing more complex actions like hover over an element,
# double-click, drag and drop, send keys, etc.

from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions import interaction
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from selenium.webdriver.common.devtools.v85.indexed_db import KeyPath
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType

def test_Action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    #first_name.send_keys("thetestingacademy")

    # If we want to send keys in Capital letter than we use Action Keyboard Class
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys("thetestingacademy").key_up(Keys.SHIFT).perform()

    time.sleep(10)
    driver.quit()
    