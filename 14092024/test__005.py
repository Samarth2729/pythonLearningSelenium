# 1 Open the URL - https://www.idrive360.com/enterprise/login
# 2 Enter the username, password
# 3 Verify that Trial is fnished and current URL also
# 4 Add a logic to add Allure Screen for the Trail end

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mini_project3():
    # Set up the driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Navigate to URL
    driver.get("https://www.idrive360.com/enterprise/login")

    # Enter username and password using WebDriverWait instead of time.sleep()
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_element.send_keys("augtest_040823@idrive.com")

    password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_element.send_keys("123456")

    # Wait for the sign-in button and click it
    signin_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "frm-btn"))
    )
    signin_button_element.click()

    # Wait for the new URL to load after signing in
    WebDriverWait(driver, 25).until(
        EC.url_to_be("https://www.idrive360.com/enterprise/account?upgradenow=true")
    )

    # Verify the trial is finished and the alert is displayed using visibility_of_element_located
    message_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "id-card-title"))
    )

    # Check if the element is visible
    assert message_alert.is_displayed()

    driver.quit()


