from selenium import webdriver

from pages.bae_page import BasicAjaxPage


def test_user_can_select_desktop_and_c():
    driver = webdriver.Chrome()
    driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")

    ajax_page = BasicAjaxPage(driver)
    ajax_page.select_category_and_language("Desktop", "C")
