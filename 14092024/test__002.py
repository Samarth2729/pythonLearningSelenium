import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
from selenium.webdriver.common.by import By

@pytest.mark.poitive
@allure.title("Verify that URL changes when we click on the make appointment button")
@allure.description("Verify the URL Changes")

def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # - Find the Element the Anchor tag
    # - We need to find the unique attribute which can find the web element
    # - <a id="btn-make-appointment"
    # href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")

    # Click on it
    make_appointment_element.click()

    # Verify that Url Changes

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.quit()
