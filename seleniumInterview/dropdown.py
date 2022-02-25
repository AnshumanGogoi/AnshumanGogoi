import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/campaign/"
               "landing.php?campaign_id=16115752481&extra_1=s%7Cc%7C580541349579%7"
               "Ce%7Cfacebook%7C&placement=&creative=580541349579&keyword=facebook&partner"
               "_id=googlesem&extra_2=campaignid%3D16115752481%26adgroupid%3D130343387942%26matcht"
               "ype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adpo"
               "sition%3D%26target%3D%26targetid%3Dkwd-1001394929%26loc_physical_ms%3D1007745%26loc_interest_ms%3D%26feedite"
               "mid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMI6qv6lP2Q9gIVHplmAh0J0AV1EAAYASAAEgKwgPD_BwE")
days = driver.find_elements(By.XPATH,'//select[@id="day"]/option')
for day in days:
    date = day.text
    print(date)
    if date == "11":

        select = Select(driver.find_element(By.ID,"day"))
        #select.select_by_visible_text("31")
        select.select_by_value("11")
        break
        #select.select_by_index(3)
time.sleep(6)

    