from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath ="//*[@id = 'password']"
    sign_in_the_button_xpath ="//button/span[1]"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    login_url = ("https://scouts-test.futbolkolektyw.pl/en/login")
    expected_title = 'Scouts panel - sign in'
    header_of_box = 'Scouts Panel'
    polish_language_xpath = "//div[3]/ul/li[1]"
    english_language_xpath = "//div[3]/ul/li[2]"
    language_list_xpath = "//form/div/div[2]/div"
    polish_url = ("https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true")



    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_the_button_xpath)

    def choose_language(self, language):
        self.click_on_the_element(self.language_list_xpath)
        time.sleep(2)
        if language == "english":
            self.click_on_the_element(self.english_language_xpath)
        else:
            self.click_on_the_element(self.polish_language_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
