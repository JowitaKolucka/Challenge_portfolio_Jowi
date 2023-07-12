from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_field = "//*[@name='myTeam']"
    enemy_team_field = "//*[@name='enemyTeam']"
    my_team_score_field = "//*[@name='myTeamScore']"
    enemy_team_score_field = "//*[@name='enemyTeamScore']"
    date_select_field = "//*[@name='date']"
    match_at_home_picker = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]/input"
    match_out_home_picker = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
    t_shirt_color_field = "//*[@name='tshirt']"
    rating_field = "//*[@name='rating']"
    numer_field = "//*[@name='number']"
    pass