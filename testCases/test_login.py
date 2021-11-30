import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
#from utilities.customLogger import LogGen
import allure


class Test_001_Login:
    #baseURL = "https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F"
    #username = "gogoi.anshuman21@gmail.com"
    #password = "sunny@08642"
    baseURL = ReadConfig.getApplicationURL()
    #print(baseURL)
    username = ReadConfig.getUsername()
    #print(username)
    password = ReadConfig.getPassword()
    #Logen Utility
    #logger=LogGen.loggen()


    def test_homePageTitle(self,setup):
        #fixture
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.logger.info("***************Test_001_Login*******************")
        #self.logger.info("***************Verifying Home Page*******************")
        self.driver = setup
        #self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print("*****************Title************")
        print(act_title)

        if act_title == "Login | Udemy":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot("/Users/anshumangogoi/PycharmProjects/TestingFrameWork/Screenshots/"+"test_homePageTitle.png")
            self.driver.quit()
            assert False

    def test_login(self,setup):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        #self.driver.maximize_window()
        self.driver.get(self.baseURL)
        # object creation of LoginPage.py
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.save_screenshot("/Users/anshumangogoi/PycharmProjects/TestingFrameWork/Screenshots/"+"test_login.png")
        print("#########################Title#############")
        print(act_title)
        self.driver.quit()
