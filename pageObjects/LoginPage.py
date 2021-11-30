from selenium import webdriver

class LoginPage:
    textbox_username_id = "email--1"
    textbox_password_id = "id_password"
    button_login_id = "submit-id-submit"
    #link_logout_linktext = ""

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()




