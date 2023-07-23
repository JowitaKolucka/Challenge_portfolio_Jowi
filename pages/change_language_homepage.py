import os
import time
import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver


class ChangeLanguageOnHomepage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language_functionality(self):
        user_login = LoginPage(self.driver)
        user_login.choose_language("english")
        time.sleep(3)
        user_login.choose_language("polski")
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()

