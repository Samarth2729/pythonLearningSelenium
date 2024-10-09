import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_practice():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()

    time.sleep(10)

    # Search for 'India' in the city search box
    search_city = driver.find_element(By.ID, "search_city")
    search_city.send_keys("India")
    time.sleep(5)

    # Correct the XPath to fetch the cities from the table
    list_of_cities = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")

    # Print header for output
    print("Name | AQI | Rank")

    # Using a for loop to iterate over cities
    for city in list_of_cities:
        # Find the AQI value to the right of the city
        aqi_element = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(city)).text
        # Find the rank value (assuming it's to the left of the city, modify as per actual table structure)
        rank_element = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(city)).text
        # Print the city, AQI, and rank
        print(city.text + " | " + aqi_element + " | " + rank_element)

    # Wait for a few seconds before closing the driver
    time.sleep(10)
    driver.quit()
