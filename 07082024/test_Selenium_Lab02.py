import time

from selenium import webdriver

def test_open_vwologin():
    driver = webdriver.Chrome()
    # this code call http request - POST
    # Post Request / Create the Session
    # Session means - its 16 digit of unique id
    #driver = webdrive.Edge()
    #driver = webdrive.Firefox()
    # code->http request->chrome drive->chrome session(id)

    driver.get("https://app.vwo.com")
    print(driver.session_id) # ae7fbef827727e7ca0c94b5681f1814f
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)



