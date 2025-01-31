from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.Base_page import BasePage

class LoginPage(BasePage):

    username_xpath = "//input[@id='login_email']"
    password_xpath = "//input[@id='login_password']"
    login_button_xpath = "//button[normalize-space()='Login']"

    def __init__(self,driver):
        super().__init__(driver)

    def entering_username(self, username):
        self.element_sendkeys(username,self.username_xpath)
        # Pass a tuple (By.XPATH, <locator_value>)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, self.username_xpath))
        # ).send_keys(username)

    def entering_password(self, password):
        self.element_sendkeys(password, self.password_xpath)
        # Pass a tuple (By.XPATH, <locator_value>)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, self.password_xpath))
        # ).send_keys(password)

    def click_login(self):
        self.element_click(self.login_button_xpath)
        # Pass a tuple (By.XPATH, <locator_value>)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, self.login_button_xpath))
        # ).click()


