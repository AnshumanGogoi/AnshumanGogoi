from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    #driver.delete_cookie()
    return driver
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# @pytest.fixture(scope="session", autouse=True)
# def setup(browser):
#     if browser == "chrome":
#         print("Launch chrome")
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.maximize_window()
#         #     #driver.delete_cookie()
#         yield
#         driver.quit()
#
#     elif browser == "ff":
#         print("Launch firefox")
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         driver.maximize_window()
#         yield
#         driver.quit()
#
#     else:
#         print("Provide a valid browser")
#     # print("login")
#     # yield
#     # print("Logout")
#     # print("Close browser")
#     # webdriver.Firefox.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")
#
#

