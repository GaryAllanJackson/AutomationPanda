import time

import pyautogui
import requests

# import pyscreeze

from common.function_library import Functions


class UltimateQaPage:
    def __init__(self, driver):
        self.driver = driver
        self.funct = Functions(self.driver)

    def ultimate_qa_page(self):
        pass

    def list_elements(self):
        # funct = Functions(self.driver)
        elements = self.funct.get_elements("css_selector", ".et_pb_text_inner li > a")
        for ele in elements:
            print(self.funct.get_element_text_alt(ele))

    def learn_to_automate(self):
        self.funct.perform_click("link_text", "Learn how to automate an application that evolves over time", "https://ultimateqa.com/sample-application-lifecycle-sprint-1/", "current_url", "Click Learn to automate link")
        print(self.driver.current_url)
        print(self.funct.get_element_text("tagname", "h1"))
        # element = self.funct.get_element("name", "firstname")
        self.funct.perform_send_key("name", "firstname", "Gary", "Gary", "get_text", "Send Text to Input")
        self.funct.perform_click("id", "submitForm", "https://ultimateqa.com/?firstname=Gary", "current_url", "Submitting form with url check requirement")
        self.funct.log_contains_action("URL Check",  "Gary", self.driver.current_url,"Check URL contains name" )
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshots/full_screenshot_with_url.png")
        except Exception as e:
            print(e)
            self.driver.save_screenshot("screenshots/ultimate_screenshot.png")
        # self.funct.navigate("https://localhost:5289/games", "Getting JSON from Local API")
        time.sleep(10)
        # print(f"Navigated to {self.driver.current_url}")
        # print(requests.get(self.driver.current_url).json())
        # time.sleep(5)