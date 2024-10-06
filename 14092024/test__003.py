import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
from selenium.webdriver.common.by import By

@pytest.mark.poitive
@allure.title("VWO Invalid Login Page - Test Mini Project 2")
@allure.description("Verify that with invalid Email and Password,Error message came")

def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"

    # Find the Element email and password and enter Invalid details
    # <input type="email" class="text-input W(100%)"
    # name="username" id="login-username" data-qa="hocewoqisi">
    # - We need to find the unique attribute which can find the web element
    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("admin@admin.com")

    time.sleep(2)  # Reducing the wait time from 100 to 2 seconds

    # <input type="password" class="text-input W(100%)"
    # name="password" id="login-password" data-qa="jobodapuxe">

    password_web_element = driver.find_element(By.ID, "login-password")
    password_web_element.send_keys("admin@123")


    # Find the element Submit button
    # <button type="submit" id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)" data-qa="sibequkica">
    #
    # <span class="icon loader hidden" data-qa="zuyezasugu"></span>
    # <span data-qa="ezazsuguuy">Sign in</span>
    # </button>

    submit_button_element = driver.find_element(By.ID, "js-login-btn")  # Fixing locator here
    submit_button_element.click()

    time.sleep(3)

    # Error Message
    # <div class="notification-box-description" id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password, IP address or location did not match</div>

    error_message_element = driver.find_element(By.ID, "js-notification-box-msg")  # Fixing locator here
    assert error_message_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)

    driver.quit()
