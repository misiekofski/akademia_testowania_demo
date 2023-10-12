from selenium.webdriver.common.by import By


class DynamicTablePage():
    def __init__(self, driver):
        self.driver = driver

    SUMMARY_EXPANDER = (By.XPATH, "//summary")
    JSONDATA_TEXTAREA = (By.ID, "jsondata")
    REFRESHTABLE_BUTTON = (By.ID, "refreshtable")
    DYNAMIC_TABLE = (By.ID, "dynamictable")
    DYNAMIC_TABLE_ROWS = (By.XPATH, ".//tr")

    def refresh_table_with_data(self, table_data):
        self.driver.find_element(*self.SUMMARY_EXPANDER).click()

        jsondata_text = self.driver.find_element(*self.JSONDATA_TEXTAREA)
        jsondata_text.click()
        jsondata_text.clear()
        jsondata_text.send_keys(table_data)

        self.driver.find_element(*self.REFRESHTABLE_BUTTON).click()

    def get_table_rows(self):
        table = self.driver.find_element(*self.DYNAMIC_TABLE)
        # search for all elements inside table
        rows = table.find_elements(*self.DYNAMIC_TABLE_ROWS)
        # how much rows did we find in table
        return len(rows)
