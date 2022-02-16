import requests
import urllib3
import pytest
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.flipkart.com')
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()
links = driver.find_elements(By.CSS_SELECTOR, "a")
broken_links = 0
valid_links = 0

for link in links:
    try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
        if (request.status_code == 404):
            broken_links = (broken_links + 1)
        else:
            valid_links = (valid_links + 1)
    except requests.exceptions.MissingSchema:
        print("status code :" + str(request.status_code))
    #     print("Encountered MissingSchema Exception")
    # except requests.exceptions.InvalidSchema:
    #     print("Encountered InvalidSchema Exception")
    # except:
    #     print("Encountered Some other execption")
