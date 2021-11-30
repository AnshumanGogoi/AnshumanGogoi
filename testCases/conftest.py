from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    #driver.delete_cookie()
    return driver
