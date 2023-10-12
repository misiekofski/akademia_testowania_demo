from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ExpandingDivPage():
    def __init__(self, driver):
        self.driver = driver

    EXP_DIV = (By.CSS_SELECTOR, "div.expand")
    THIS_LINK = (By.CSS_SELECTOR, "a")


    def go_to_hidden_link(self):
        div = self.driver.find_element(*self.EXP_DIV)
        # mouse over div
        ActionChains(self.driver)\
            .move_to_element(div)\
            .perform()

        # search for link inside this div
        link_to_click = div.find_element(*self.THIS_LINK)
        link_to_click.click()
