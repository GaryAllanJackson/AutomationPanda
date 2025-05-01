from common.function_library import Functions


class GamesApiPage:
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 10)

    def get_games_from_api(self):
        funct = Functions(self.driver)
        print("get_games_from_api")
        funct.get_json_from_api("http://localhost:5289/games")