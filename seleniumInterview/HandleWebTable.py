from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://chercher.tech/practice/table")

websites = driver.find_elements(By.XPATH, "//*[@id='webtable']//tr/td[1]")
for website in websites:
    print(website)
    site = website.text
    if site=='selenium-webdriver.com':
        print(site)
        infos = driver.find_elements(By.XPATH, "//*[contains(text(),'"+site+"')]//following-sibling::td")
        for info in infos:
            print(info.text)
        break

