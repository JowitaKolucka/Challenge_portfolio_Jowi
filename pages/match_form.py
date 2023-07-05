from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    enemy_team_score_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    date_select_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    match_at_home_picker = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]/input"
    match_out_home_picker = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
    t_shirt_color_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    rating_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    numer_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    pass