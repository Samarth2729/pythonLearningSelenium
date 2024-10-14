import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import (ElementNotVisibleException,NoSuchElementException,TimeoutException,
                                        ElementNotSelectableException,StaleElementReferenceException)

# How Handle Exceptions
# NoSuchElementException
# ElementNotVisibleException
# ElementNotSelectableException
# StaleElementReferenceException

# How to handle exceptions in selenium
def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()

    # Learning how to handle exceptions by using try and except block
    try:
        driver.find_element(By.NAME, "sam").send_keys("Python")
    except NoSuchElementException:
        print("Element not found")
    time.sleep(5)


# Stale element exception
def test_stale():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    try:
        text_area = driver.find_element(By.NAME, "q")
        # text area will be refereshed
        driver.refresh()
         # DOM element refereshed
        # webdriver will not be able to find the element
        text_area.send_keys("Python")

        time.sleep(5)

    except StaleElementReferenceException:
        print("Element is stale")
        text_area = driver.find_element(By.NAME, "q")
        text_area.send_keys("Python")

        time.sleep(5)

def test_exceptions():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()

    # Learning how to handle exceptions by using try and except block
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "sam")))
        print("End of the Program")

    except TimeoutException as see:
        print("see")
        print("Time out excepetion occured!, 10 seconds pass")
    time.sleep(5)

    