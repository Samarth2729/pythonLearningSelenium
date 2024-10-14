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

def test_alert_tc1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    # Locate and click the button to trigger the alert
    alert_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@onclick='jsAlert()']"))
    )
    alert_button.click()

    # Switch to the alert, wait for it to be present, then accept it
    alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()

    print(alert_text)  # Print alert text before accepting it

    # Verify the result message
    result = driver.find_element(By.ID, "result").text
    assert result == "You successfully clicked an alert"

    driver.quit()


