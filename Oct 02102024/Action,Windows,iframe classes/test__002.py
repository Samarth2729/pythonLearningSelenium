# Action Classes Mouse


from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions import interaction
import time
import pytest
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType

def test_Action_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    # click - Normal Driver, will find the elemnt and click on it, and release it
    # Click and hold - Click and hold it - We will not release it.

    # <a href="resultPage.html" id="click">Click for Results Page</a>
    a_tag = driver.find_element(By.ID, "click")
    a_tag.click()

    actionbuilder = ActionBuilder(driver)
    actionbuilder.pointer_action.pointer_up(MouseButton.BACK)
    actionbuilder.perform()

    time.sleep(5)
    driver.quit()



    time.sleep(10)
    driver.quit()

    