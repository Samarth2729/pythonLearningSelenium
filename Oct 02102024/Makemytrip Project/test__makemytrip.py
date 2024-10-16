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
def test_Action_makemytrip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/flights")
    driver.maximize_window()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    ).click()

    # <input data-cy="fromCity" id="fromCity" type="text"
    # class="fsw_inputField lineHeight36 latoBlack font30" readonly="" value="Delhi">

    fromcity = driver.find_element(By.ID, "fromCity")

    actions = ActionChains(driver)
    actions.move_to_element(fromcity).click().send_keys("Mumbai").perform()
    time.sleep(2)  # Allow time for the dropdown options to load

    # Use keyboard actions to select the first option
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    time.sleep(10)  # Wait for demo purposes

    driver.quit()



    