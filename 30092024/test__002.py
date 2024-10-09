#Selenium Mini Project #7 for Relative Locators

# https://codepen.io/AbdullahSajjad/full/LYGVRgK
# Switch Iframe - result
# Find the button click on it
# Find the input username
# Below element - error message
# Assert that error message.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from allure_commons.types import AttachmentType
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import allure

@pytest.mark.smoke
@allure.title("Verify that codepen registered page is opened ")
@allure.description("TC#1 - Below element - error message assert that error message.")
def test_MiniProject7():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()

    time.sleep(2)
# <iframe id="result" src="https://codepen.io/AbdullahSajjad/fu
    driver.switch_to.frame(driver.find_element(By.ID, "result"))

    button_elmnt = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button_elmnt.click()

    time.sleep(3)
# <input type="text" id="username" placeholder="Enter Username">
    username_elmnt = driver.find_element(By.ID, "username")
# <small>Username must be at least 3 characters</small>
    error_msg = driver.find_element(locate_with(By.TAG_NAME, "small").below(username_elmnt)).text


    assert error_msg == "Username must be at least 3 characters"

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    driver.quit()


