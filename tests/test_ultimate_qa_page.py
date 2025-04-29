from pages.base_page import BasePage
from pages.ultimate_qa_page import UltimateQaPage




class TestUltimateQaPage:
    def test_ultimate_qa_page(self, setup):
        self.driver = setup
        base_page = BasePage(self.driver)
        base_page.base_page()
        ultimate = UltimateQaPage(self.driver)
        ultimate.list_elements()
        ultimate.learn_to_automate()
