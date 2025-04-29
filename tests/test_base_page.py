from pages.base_page import BasePage


class TestBasePage:
    def test_base_page(self, setup):
        self.driver = setup
        base_page = BasePage(self.driver)
        base_page.base_page()
