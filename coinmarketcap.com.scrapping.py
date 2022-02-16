import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# get method to launch the URL
#driver.get("https://coinmarketcap.com")

# CSV file creation

with open('coinmarketcap[13].com.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(
        ["name", "price", "daily_interest_percentage", "weekly_interest_percentage", "market_cap", "daily_volume"])
    for i in range(13, 95):
        url = "https://coinmarketcap.com" + "/?page=" + str(i)
        print("Current url:"+url)
        print("**************Scraping is going on. Please wait****************")
        driver.get(url)
        height = driver.execute_script("return document.body.scrollHeight")
        for scrol in range(100, height, 100):
            driver.execute_script(f"window.scrollTo(0,{scrol})")
            time.sleep(0.1)

        details_xpath = "*//div[@class='css-1had40c']"
        crypto_details_xpath = "//table[@class='h7vnx2-2 czTsgW cmc-table  ']/tbody/tr"
        crypto_details = driver.find_elements(By.XPATH, crypto_details_xpath)
        columns_count = driver.find_elements(By.XPATH, "//table[@class='h7vnx2-2 czTsgW cmc-table  ']//tr[1]/td")
        rows = len(crypto_details)
        columns = len(columns_count)
        #print(rows)
        #print(columns)
        for i in range(1, rows + 1):
            name = driver.find_element(By.XPATH, crypto_details_xpath + "[" + str(i) +
                                       "]/td[3]//p[@class='sc-1eb5slv-0 iworPT']").text
            #print(name)
            price = driver.find_element(By.XPATH, crypto_details_xpath + "[" + str(i) + "]/td[4]/div//span").text
            #print(price)
            try:
                price_down_daily = driver.find_element(By.XPATH, crypto_details_xpath +
                                                       "[" + str(i) + "]/td[5]//span[@class='icon-Caret-down']")

                daily_interest_percentage_raw = driver.find_element(By.XPATH,
                                                                    crypto_details_xpath + "[" + str(
                                                                        i) + "]/td[5]//span").text
                daily_interest_percentage = "-" + daily_interest_percentage_raw
                #print("price down 24%: " + daily_interest_percentage)
            except:
                price_up_daily = driver.find_element(By.XPATH, crypto_details_xpath +
                                                     "[" + str(i) + "]/td[5]//span[@class='icon-Caret-up']")
                daily_interest_percentage_raw = driver.find_element(By.XPATH, crypto_details_xpath +
                                                                "[" + str(i) + "]/td[5]//span").text
                daily_interest_percentage = "+" + daily_interest_percentage_raw
                #print("price up 24%: " + daily_interest_percentage)
            finally:
                daily_interest_percentage = "N/A"

            try:
                price_down_weekly = driver.find_element(By.XPATH, crypto_details_xpath +
                                                        "[" + str(i) + "]/td[6]//span[@class='icon-Caret-down']")
                weekly_interest_percentage_raw = driver.find_element(By.XPATH, crypto_details_xpath +
                                                                     "[" + str(i) + "]/td[6]//span").text
                weekly_interest_percentage = "-" + weekly_interest_percentage_raw
                #print("Price down in 7 days:" + weekly_interest_percentage)
            except:
                price_up_weekly = driver.find_element(By.XPATH, crypto_details_xpath +
                                              "[" + str(i) + "]/td[6]//span[@class='icon-Caret-up']")
                weekly_interest_percentage_raw = driver.find_element(By.XPATH, crypto_details_xpath +
                                                             "[" + str(i) + "]/td[6]//span").text
                weekly_interest_percentage = "+" + weekly_interest_percentage_raw
                #print("Price up in 7 days:" + weekly_interest_percentage)
            market_cap = driver.find_element(By.XPATH, crypto_details_xpath +
                                     "[" + str(i) + "]/td[7]//span[@class='sc-1ow4cwt-1 ieFnWP']").text
            #print("Market Capital:" + market_cap)
            try:
                daily_volume = driver.find_element(By.XPATH, crypto_details_xpath +
                                       "[" + str(
                             i) + "]/td[8]//p[@class='sc-1eb5slv-0 hykWbK font_weight_500']").text
                #print("daily_volume:" + daily_volume)
            except:
                daily_volume = "N/A"
            writer.writerow(
                        [name, price, daily_interest_percentage, weekly_interest_percentage, market_cap, daily_volume])
