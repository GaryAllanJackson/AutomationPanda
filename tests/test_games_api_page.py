from pages.games_api_page import GamesApiPage


class TestGamesApiPage:
    def test_games_api_page(self, setup):
        self.driver = setup
        game = GamesApiPage(self.driver)
        game.get_games_from_api()
