from pages.selectors_hub_practice_page import SelectorsHubPracticePage


class TestSelectorsHubPracticePage:
    def test_selectors_hub_practice_page(self, setup):
        self.driver = setup
        shp = SelectorsHubPracticePage(self.driver)
        shp.selectors_hub_practice_page()
        shp.useful_links_for_learning()
