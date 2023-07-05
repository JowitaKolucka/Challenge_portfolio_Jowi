from pages.base_page import BasePage


class Dashboard(BasePage):
    add_player_xpath= "//*[text()= 'Dodaj gracza']"
    dev_team_contact_xpath='//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    logout_button_xpath="//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    english_button_xpath="//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    gracze_button_xpath="//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    last_player_xpath="//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    recently_updated_player_xpath="//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    recently_updated_match_xpath="//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]"
    recently_updated_report = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"
    last_created_match_xptah="//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[2]"


pass