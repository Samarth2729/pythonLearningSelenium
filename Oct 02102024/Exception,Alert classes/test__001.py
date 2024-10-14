# How to handle Static  Dropdown element.

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

@pytest.mark.positive
def test_dropdown_elmnt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()

    # find dropdown element
    dropdown_elmnt = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown_elmnt)
    select.select_by_visible_text("Option 2")
    time.sleep(2)
    driver.quit()
    



