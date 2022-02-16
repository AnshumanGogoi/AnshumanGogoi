from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("your.site.with.dragndrop.functionality.com")
source_element = driver.find_element_by_name('your element to drag')
dest_element = driver.find_element_by_name('element to drag to')
action = ActionChains(driver)
action.drag_and_drop(source_element, dest_element).perform()
