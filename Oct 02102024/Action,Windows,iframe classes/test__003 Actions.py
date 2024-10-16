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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType

def test_Action_mousedraggable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    # <div id="draggable" class="ui-widget-content ui-draggable
    # ui-draggable-handle" style="position: relative;">Draggable</div>
    drag_elemnt = driver.find_element(By.ID, "draggable" )

    action = ActionChains(driver)
    action.click_and_hold(on_element=drag_elemnt).perform()

    time.sleep(10)



    