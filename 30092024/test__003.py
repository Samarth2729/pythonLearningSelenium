import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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
