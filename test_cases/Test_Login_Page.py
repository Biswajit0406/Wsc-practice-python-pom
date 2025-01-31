import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.Login_Page import LoginPage
from utilities.read_config import Read_Config
import pytest
from utilities.custom_logger import Log_maker
from utilities.excel_reader import ExcelUtils
from Base.Base_page import BasePage

testdata = ExcelUtils.load_excel_data("C:/Users/KIIT/Desktop/Credential.xlsx","Sheet1")

class Test_Loginpage:

    url = Read_Config.get_url()
    # username = Read_Config.get_username()
    # password = Read_Config.get_password()
    logger = Log_maker.log_gen()

    @pytest.mark.parametrize("username,password",testdata)
    def test_login(self,setup,username,password):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.entering_username(username)
        self.lp.entering_password(password)
        self.lp.click_login()
        self.logger.info("******************Login successfull*********************")
        self.driver.save_screenshot("C:/Users/KIIT/PycharmProjects/pythonProject1/screenshots/screenshot2.png")
        time.sleep(5)
        self.driver.close()






