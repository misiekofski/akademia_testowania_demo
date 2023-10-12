from time import sleep

from selenium import webdriver

from pages.exp_div_page import ExpandingDivPage


def test_user_can_edit_table_data():
    driver = webdriver.Chrome()
    driver.get("https://testpages.herokuapp.com/styled/expandingdiv.html")

    exp_div_page = ExpandingDivPage(driver)
    exp_div_page.go_to_hidden_link()

    sleep(2)