from selenium import webdriver

from pages.login_page import LoginPage


def test_given_valid_user_should_login_succesfully():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login_as("standard_user", "secret_sauce")

    assert login_page.get_products_title() == "Products"
    driver.close()


def test_given_invalid_user_should_not_login_succesfully():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login_as("standard_user", "bad_password")

    assert "Epic sadface" in login_page.get_error_message()
    driver.close()
