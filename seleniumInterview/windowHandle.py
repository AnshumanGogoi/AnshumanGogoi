from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/s?k=iPhone+13&ref=nb_sb_noss_1")
#searchBox = driver.find_element_by_id("twotabsearchtextbox")
#searchBox.send_keys("iphone 13")
#search = driver.find_element_by_id("nav-search-submit-button")
#search.click()
current_window = driver.current_window_handle
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[1]/h2/a/span").click()
child_windows = driver.window_handles
print(child_windows)
for child in child_windows:
    if current_window!=child:
        driver.switch_to.window(child)
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.close()
driver.switch_to.window(current_window)
driver.implicitly_wait(5)
driver.quit()
