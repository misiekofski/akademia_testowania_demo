from selenium import webdriver

from pages.dynamic_table_page import DynamicTablePage


def test_user_can_edit_table_data():
    driver = webdriver.Chrome()
    driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

    table_page = DynamicTablePage(driver)
    table_page.refresh_table_with_data('[{"imię": "Bob", "wiek" : 20}, {"imię": "George", "wiek" : 42}, {"imię": "Jan", "wiek" : 7} ]')

    # sprawdź czy mamy cztery wiersze w tabeli (pierwszy to nagłówki)
    assert table_page.get_table_rows() == 4

