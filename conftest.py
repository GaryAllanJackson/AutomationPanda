import pytest
from selenium import webdriver
from common.function_library import Functions
from common import variables


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    funct = Functions(driver)
    funct.navigate(variables.base_url, "Navigating to base URL")
    yield driver
    # driver.quit()
    close_driver(driver)


def close_driver(driver):
    driver.quit()
    funct = Functions(driver)
    funct.log_equal_action("Close Driver", "n/a", "n/a",  "Closing Driver")
    print("\nDriver closed")
