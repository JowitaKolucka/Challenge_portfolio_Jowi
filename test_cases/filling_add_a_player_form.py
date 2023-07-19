import os
import time
from selenium.webdriver.chrome.service import Service
import unittest
from selenium import webdriver
from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestFillingAddPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_open_add_a_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        time.sleep(5)
        add_player = AddAPlayer(self.driver)
        time.sleep(6)
        add_player.type_in_email("jacek@gmail.com")
        add_player.type_in_name("Jacek")
        add_player.type_in_surname("Kopacz")
        add_player.type_in_phone_field("111222333")
        add_player.type_in_age_field("28")
        add_player.type_in_height_field("178")
        add_player.type_in_weight_field("70")
        add_player.type_in_main_position_field("Striker")
        add_player.click_on_the_submit_button()


    @classmethod
    def tearDown(self):
        self.driver.quit()