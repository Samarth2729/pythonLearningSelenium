from selenium import webdriver


def test_sample(): # selenium 4
    driver = webdriver.Edge()
    driver.get("http://google.com")  # Navigation command its get request
    assert driver.current_url == "http://google.com/"