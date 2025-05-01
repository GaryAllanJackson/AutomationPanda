import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AutomationBookstorePage:
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)

    def search_books(self, phrase):
        if self.driver.current_url != "https://automationbookstore.dev/":
            self.driver.find_element(By.LINK_TEXT, "Automation Bookstore").click()
            time.sleep(3)
        print(f"====[ Search for books containing: {phrase} ]===========")
        self.driver.find_element(By.ID, "searchBar").send_keys(phrase)
        time.sleep(2)
        # elements = self.driver.find_elements(By.CSS_SELECTOR, "ul.productList li")
        elements = self.driver.find_elements(By.XPATH, "(//ul[@id='productList'])/li")
        for element in elements:
            title = element.find_element(By.TAG_NAME, "h2").text
            author = element.find_element(By.TAG_NAME, "p").text
            price =  element.find_element(By.CSS_SELECTOR, "p.ui-li-aside").text
            if len(title) > 0:
                print(f"Title:{title}\tAuthor:{author}\tPrice:{price}")
        print("==================================================")
        self.driver.refresh()

