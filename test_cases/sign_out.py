from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import time

from utils.settings import DEFAULT_LOCATOR_TYPE, DRIVER_PATH, IMPLICITLY_WAIT
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class TestSignOut(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_out_from_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_signout_button()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()