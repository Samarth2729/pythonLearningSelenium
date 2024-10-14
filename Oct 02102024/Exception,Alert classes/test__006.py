import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
@pytest.mark.checkbox
def test_checkbox():
    # Instantiate ChromeOptions and set the page load strategy
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=options)

    # Navigate to the checkbox page
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Maximize the window (optional, for visibility)
    driver.maximize_window()

    # Interact with the checkboxes (example: clicking the first checkbox)
    checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
    checkbox1.click()
    time.sleep(1)

