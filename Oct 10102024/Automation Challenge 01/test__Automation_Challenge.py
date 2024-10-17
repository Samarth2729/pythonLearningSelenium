import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Calculate the Total Amount of Money Spent via Selenium Script
# Open the https://demo.applitools.com
# Enter the Username as Admin and Password as Password@123
# Verify that you are on the app.html page afterward.
# Calculate the total amount spent this month.
# Create a util which will parse and check for spent vs earned.
# Verify total is 1996.22

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_applitools_demo():
    driver = webdriver.Chrome()
    driver.get("https://demo.applitools.com")

    # Print the page title for verification
    print("Page title:", driver.title)

    username_input_textbox = driver.find_element(By.XPATH, "//input[@id='username']")
    username_input_textbox.send_keys("Admin")


    password_input_textbox = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input_textbox.send_keys("Password@123")


    sign_in_btn = driver.find_element(By.XPATH, "//a[@id='log-in']")
    sign_in_btn.click()


    time.sleep(5)

    # Verify if on the correct page
    assert "app.html" in driver.current_url, "Not on the app.html page!"

    rows = driver.find_elements(By.XPATH, './/tbody/tr')

    total_amount = 0.0

    for row in rows:
        amount_text = row.find_element(By.XPATH, './td[5]').text
        print(f"Raw amount text: {amount_text}")

        # Remove currency symbol, commas, and spaces, then convert to float
        amount_text = amount_text.replace('USD', '').replace(',', '').replace(' ', '')
        amount = float(amount_text)
        print(f"Converted amount: {amount}")

        total_amount += amount

    print(f"Total amount calculated: {total_amount}")

    # Final assertion with detailed output
    expected_total = 1996.22
    assert total_amount == expected_total, f"Expected total {expected_total}, but got {total_amount}"

    print("Test completed successfully.")

    # Close the driver
    driver.quit()


