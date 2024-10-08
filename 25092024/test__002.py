import time
import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
def test_amcharts_svg_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)

    # //*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']
    state_list = driver.find_elements(By.XPATH,
                                      "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    # we use for loop.
    for state in state_list:
        if "Madhya Pradesh" in state.get_attribute("aria-label"):  # aria-label we can from path as a unique identity
            state.click()
        break

    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), "svg_elements", allure.attachment_type.PNG)


