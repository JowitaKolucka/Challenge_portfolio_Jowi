from pages.base_page import BasePage
import time


class Dashboard(BasePage):
    add_player_xpath= "//*[text()= 'Add player']"
    dev_team_contact_xpath="//*[text()='Dev team contact']"
    sign_out_button_xpath="//ul[2]/div[2]/div[2]/span"
    polski_button_xpath="//*[text()= 'Polski']"
    players_button_xpath="//*[text()= 'Players']"
    last_player_xpath="//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_xpath="//div[3]/div/div/a[2]/button/span[1]"
    last_updated_match_xpath="//div[3]/div/div/a[4]/button/span[1]"
    last_updated_report = "//div[3]/div/div/a[5]/button/span[1]"
    last_created_match_xpath="//div[3]/div/div/a[3]/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    def title_of_page(self):
        time.sleep(6)
        assert self.get_page_title(self.dashboard_url) == self.expected_title


pass