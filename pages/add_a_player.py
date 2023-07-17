import self

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_xpath = "//*[text()='Add player]"
    email_field_xpath = "//*[@name = 'email']"
    name_field_xpath = "//*[@name = 'name']"
    surname_field_xpath = "//*[@name = 'surname']"
    phone_field_xpath = "//*[@name = 'phone']"
    weight_field_xpath = "//*[@name = 'weight']"
    height_field_xpath = "//*[@name = 'height']"
    age_field_xpath = "//*[@name = 'age']"
    main_position_field_xpath = "//*[@name = 'mainPosition']"
    submit_button_xpath = "//button[@type='submit']"
    add_player_title = "Add player"
    player_form_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    player_title_xpath = "/html/head/title"


    def check_title_of_page(self):
        self.click_on_the_element(self.add_player_xpath)
        time.sleep(5)
        assert self.get_page_title(self.player_title_xpath) == self.add_player_title