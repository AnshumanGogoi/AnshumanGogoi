
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/s?k=iphone+13&crid=1XFBGSBZB7CJ4&sprefix=%2Caps%2C285&ref=nb_sb_ss_recent_1_0_recent")
#searchBox = driver.find_element_by_id("twotabsearchtextbox")
#searchBox.send_keys("iphone 13")
#search = driver.find_element_by_id("nav-search-submit-button")
#search.click()

prices = driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
iphonePrice = []
for price in prices:
    #print(price.text)
    displatedPrice = int(price.text.replace(",",''))
    iphonePrice.append(displatedPrice)
print(iphonePrice)
print(sorted(iphonePrice))
max_price = iphonePrice[0]
second_max = iphonePrice[0]
for i in range(len(iphonePrice)):
    if max_price < iphonePrice[i]:
        max_price = iphonePrice[i]
for i in range (len(iphonePrice)):
    if second_max < iphonePrice[i]:
        if iphonePrice[i] != max_price:
            second_max = iphonePrice[i]
print(max_price)
print(second_max)
set_prices = set(iphonePrice)
print(set_prices)
print(sorted(set_prices))
executableLinks = []
links = driver.find_elements_by_xpath("//a[@class='a-link-normal s-link-style a-text-normal']")
for link in links:
    url = link.get_attribute('href')
    executableLinks.append(url)
for executableLink in executableLinks:
    driver.get(executableLink)
