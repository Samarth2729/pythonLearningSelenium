# Selenium Project#4 - Mini Project
# open the url - https://katalon-demo-cura.herokuapp.com/
# click on the make appoinment button
# verify that url changes - assert
# time.sleep(3)
# enter the username, password
# next page verify the current url
# make appoinment text on the web page.
# Upload them github.com


import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

def test_mini_project_4():
    # Set up the driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Navigate to URL
    driver.get("https://katalon-demo-cura.herokuapp.com")

    # Use WebDriverWait instead of sleep for Make Appointment button
    appointment_bttn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
    )
    appointment_bttn.click()

    # Verify URL changes to login page
    WebDriverWait(driver, 15).until(
        EC.url_contains("profile.php#login")
    )

    # Wait for the username field and enter username
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txt-username"))
    )
    email_element.send_keys("John Doe")

    # Wait for the password field and enter password
    password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txt-password"))
    )
    password_element.send_keys("ThisIsNotAPassword")

    # Find the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-login"))
    )
    login_button.click()

    # Verify URL changes to the appointment page
    WebDriverWait(driver, 15).until(
        EC.url_to_be("https://katalon-demo-cura.herokuapp.com/#appointment")
    )

    # Wait for the "Make Appointment" header to be visible
    h2_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Make Appointment']"))
    )
    allure.attach(driver.get_screenshot_as_png(), "h2_element", allure.attachment_type.PNG)
    # Assert the text is "Make Appointment"
    assert h2_element.text == "Make Appointment"




