from selenium import webdriver
import time

from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)
browser.close()
################ Another Way ###############
element = driver.find_element_by_id("my-id")
actions = ActionChains(driver)
actions.move_to_element(element).perform()