from pages.automation_bookstore_page import AutomationBookstorePage


class TestAutomationBookstorePage:
    # def __init__(self):

    #java test
    # def test_automation_bookstore_page(self, setup):
    #     self.driver = setup
    #     auto_book = AutomationBookstorePage(self.driver)
    #     auto_book.search_books("java")

    def test_automation_bookstore_phrases(self, setup):
        self.driver = setup
        auto_book = AutomationBookstorePage(self.driver)
        # print("Search for books containing: automation")
        auto_book.search_books("automation")
        # print("Search for books containing: test")
        auto_book.search_books("test")
