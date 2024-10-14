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
@pytest.mark.alertpromt
def test_alert_tc3():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    alert_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@onclick='jsPrompt()']"))
    )
    alert_button.click()

    alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert_text = alert.text
    alert.send_keys("Samarth")
    alert.accept()
    print(alert_text)

    result = driver.find_element(By.ID, "result").text
    assert result == "You entered: Samarth"

    driver.quit()
