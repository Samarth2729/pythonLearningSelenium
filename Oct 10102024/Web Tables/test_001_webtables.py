# What is Web Tables ?
# A web table is a way of representing the data in rows and columns.
# "<table>" tag is used to define a table in HTML.
#   <thead>
#   <tbody

# Each row in the table is defined by using the "<tr>" tag.
# Each column in the table is defined by using the "<td>" tag or the "<th>" tag.
# The text in the "<th>" tag is bold by default.

# Example:- https://awesomeqa.com/webtable.html
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    # To find the number of rows in the table
    row_elemnts = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    row = len(row_elemnts)
    print("Number of rows in the table:", row)

    # To find the number of columns in the table
    column_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    column = len(column_elements)
    print("Number of columns in the table:", column)

    for i in range(2,row+1): # +1 because it print 2 to 6 but we want to print 2 to 7
        for j in range(1,column+1):
            dynamic_xpath = f"//table[@id='customers']/tbody/tr[{i}]/td[{j}]"
            print(dynamic_xpath)
            table_data = driver.find_element(By.XPATH, dynamic_xpath).text
            print(table_data, end=" ")
# find "Helen Bennett" and which country he belongs
            if "Helen Bennett" in table_data:
                # Fetch the country from the same row (last column)
                country_xpath = f"//table[@id='customers']/tbody/tr[{i}]/td[last()]"
                country = driver.find_element(By.XPATH, country_xpath).text
                print(f"\nHelen Bennett belongs to {country}")












