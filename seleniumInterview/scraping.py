import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv

driver = webdriver.Chrome('C:/chromedriver')
driver.maximize_window()
driver.get('https://www.landsend.com')
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 10)

try:
    driver.switch_to_active_element()
    driver.find_element_by_id('closeButton').click()
except:
    pass

with open('landsend.com.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(
        ["URL", "SUK_NAME", "PRODUCT REFERENCE ID", "PRICE", "PRICE TEXT", "SIZE", "COLOR", "STOCK", "PRODUCT DETAILS",
         "FEATURES"])

    time.sleep(2)
    new = driver.find_element_by_xpath('//ul[@class="tab-navigation-desktop sticky-header"]/li[1]')
    actionChains = ActionChains(driver)
    actionChains.move_to_element(new).perform()
    categories_href = []
    items_href = []

    categories = driver.find_elements_by_xpath(".//*[@id='nav']/ul[1]/li[1]/div/div/div[1]/div[1]/ul/li/a")
    for category in categories[0:1]:
        href = category.get_attribute('href')
        categories_href.append(href)

    for cat_href in categories_href:
        driver.get(cat_href)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(15)
        items = driver.find_elements_by_xpath('//a[@class="pdp-link pdp-link-img ng-scope"]')

        for item in items:
            href = item.get_attribute('href')
            items_href.append(href)

    for item_href in items_href:
        driver.get(item_href)

        try:
            sku_name = driver.find_element_by_xpath('//h1[@class="product-title ng-binding"]').text.encode('ascii',
                                                                                                           'ignore')

            colors = driver.find_elements_by_xpath('//ul[@class="feature-selectors swatches ng-scope"]/li')
            count = 1

            for color in colors:
                color = driver.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//ul[@class="feature-selectors swatches ng-scope"]/li[' + str(count) + ']')))
                actionChains = ActionChains(driver)
                actionChains.move_to_element(color).click().perform()
                element = driver.find_element_by_xpath('//span[@class="color-selection-label ng-binding"]')
                driver.execute_script("arguments[0].scrollIntoView();", element)
                driver.implicitly_wait(5)
                age_ranges = driver.find_elements_by_xpath('//ul[@class="feature-selectors ng-scope"]/li')
                age_range_count = 1

                for age_range in age_ranges:
                    button = driver.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '//ul[@class="feature-selectors ng-scope"]/li[' + str(age_range_count) + ']')))
                    actionChains = ActionChains(driver)
                    actionChains.move_to_element(button).click().perform()
                    sizes = driver.find_elements_by_xpath('//ul[@class="feature-selectors"]/li')
                    size_count = 1

                    for size in sizes:
                        size = driver.wait.until(EC.element_to_be_clickable(
                            (By.XPATH, '//ul[@class="feature-selectors"]/li[' + str(size_count) + ']')))
                        actionChains = ActionChains(driver)
                        actionChains.move_to_element(size).click().perform()
                        time.sleep(1)

                        url = driver.current_url

                        color_of_the_product = driver.find_element_by_xpath(
                            '//span[@class="color-selection-label ng-binding"]') \
                            .text.encode('ascii', 'ignore').replace("Color:", '')
                        age_range1 = driver.find_element_by_xpath(
                            '//span[@class="selected-feature-name ng-binding ng-scope"]') \
                            .text.encode('ascii', 'ignore')
                        size1 = driver.find_element_by_xpath('//span[@class="ng-binding"][2]') \
                            .text.encode('ascii',
                                         'ignore')
                        size = age_range1 + "," + size1
                        price_text = driver.find_element_by_xpath('//span[@class="ng-binding ng-scope"]').text \
                            .encode('ascii', 'ignore')
                        price = price_text.replace("INR", '').replace("$", '')
                        product_details = driver.find_element_by_xpath('//p[@class="ng-binding ng-scope"]') \
                            .text.encode('ascii', 'ignore')
                        stock = driver.find_element_by_xpath('//div[@class="availability ng-binding"]') \
                            .text.encode('ascii', 'ignore')
                        id = driver.find_element_by_xpath(
                            '//div[@class="col-sm-12 col-md-7 product-number hidden-xs"]/span[2]') \
                            .text.replace("Item #", '')
                        features = driver.find_elements_by_xpath('//ul[@class="feature-list"]/li')
                        features_count = 1
                        features_list = []

                        for feature in features:
                            feature = driver.find_element_by_xpath(
                                '//ul[@class="feature-list"]/li[' + str(features_count) + ']') \
                                .text.encode('ascii', 'ignore').replace("u'", "")
                            features_list.append(feature)
                            features_count = features_count + 1

                        print
                        sku_name
                        print
                        url
                        print
                        color_of_the_product
                        print
                        size
                        print
                        price
                        print
                        price_text
                        print
                        stock
                        print
                        id
                        size_count = size_count + 1

                        writer.writerow(
                            [url, sku_name, id, price, price_text, size, color_of_the_product, stock, product_details,
                             features_list])

                    age_range_count = age_range_count + 1
                    time.sleep(1)

                element1 = driver.find_element_by_xpath('//h1[@class="product-title ng-binding"]')
                driver.execute_script("arguments[0].scrollIntoView();", element1)
                count = count + 1
                time.sleep(1)
        except:
            pass
