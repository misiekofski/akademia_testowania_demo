from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasicAjaxPage():
    def __init__(self, driver):
        self.driver = driver

    CATEGORY_DROPDOWN = (By.ID, "combo1")
    LANGUAGE_DROPDOWN = (By.ID, "combo2")
    CODE_BUTTON = (By.CSS_SELECTOR, "input.styled-click-button")
    AJAX_SPINNER = (By.ID, "ajaxBusy")

    def select_category_and_language(self, category, language):
        category_dropdown = self.driver.find_element(*self.CATEGORY_DROPDOWN)
        select_category = Select(category_dropdown)
        select_category.select_by_visible_text(category)

        # wait for spinner to stop
        wait = WebDriverWait(self.driver, timeout=5)
        spinner = self.driver.find_element(*self.AJAX_SPINNER)
        wait.until(lambda d: not spinner.is_displayed())

        # pick language
        language_dropdown = self.driver.find_element(*self.LANGUAGE_DROPDOWN)
        select_language = Select(language_dropdown)
        select_language.select_by_visible_text(language)

        # click button
        button = self.driver.find_element(*self.CODE_BUTTON)
        button.click()

