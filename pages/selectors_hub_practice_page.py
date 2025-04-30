import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.function_library import Functions


class SelectorsHubPracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def selectors_hub_practice_page(self):
        # WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.LINK_TEXT, "SelectorsHub Practice Page"))).click()
        self.wait.until(element_to_be_clickable((By.LINK_TEXT, "SelectorsHub Practice Page"))).click()
        print(self.driver.find_element(By.TAG_NAME,"h2").text)
        time.sleep(5)

    def useful_links_for_learning(self):
        dd = self.driver.find_element(By.CSS_SELECTOR, "div.dropdown > button")
        actions = ActionChains(self.driver)
        actions.move_to_element(dd).perform()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Join Training").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.current_url)
        # This closes the child window
        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.current_url)
        self.choose_car()
        self.get_users_table_information()


    def choose_car(self):
        car_type = self.driver.find_element(By.ID, "cars")
        select = Select(car_type)
        select.select_by_value("audi")
        time.sleep(5)

    def get_users_table_information(self):
        table = self.driver.find_element(By.ID, "resultTable")
        table_rows = table.find_elements(By.TAG_NAME, "tr")
        table_headers = ""
        for tr in table_rows:
            if table_headers == "":
                table_headers = tr.find_elements(By.TAG_NAME, "th")
                for th in table_headers:
                    print(th.text)
            table_cells = tr.find_elements(By.TAG_NAME, "td")
            for td in table_cells:
                print(td.text)
        funct = Functions(self.driver)
        funct.get_json_from_api("http://localhost:5289/games")



    # def switch_to_window(self):
    #     main_window = self.driver.current_window_handle
    #     WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
    #     for window_handle in self.driver.window_handles:
    #         if window_handle != main_window:
    #             self.driver.switch_to(window_handle)
    #             print(window_handle)
    #             break




