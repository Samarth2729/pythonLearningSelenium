from selenium import webdriver


def test_sample():
    driver = webdriver.Edge()
    driver.get("http://google.com")  # Navigation command its get request
