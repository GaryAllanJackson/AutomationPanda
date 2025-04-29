import time

from selenium.webdriver.common.by import By

from common.function_library import Functions
from common import selectors
from common import variables

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def base_page(self):
        funct = Functions(self.driver)
        # Note:  You cannot pass the actual current_url because the click method
        # will need to get this once the click has occurred when a click causes a page transition
        funct.perform_click("link_text", selectors.ultimate_qa_link_link_text,  variables.ultimate_qa_link_url, variables.get_current_url_in_action_method, "Click Ultimate QA Link")
        print(f"At end of base_page function - Current URL: {self.driver.current_url}")
        time.sleep(3)
