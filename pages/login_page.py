from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    LOGIN_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "span.title")
    ERROR_MESSAGE_BOX = (By.XPATH, "//h3[@data-test='error']")

    def login_as(self, user, password):
        login_input = self.driver.find_element(*self.LOGIN_INPUT)
        login_input.send_keys(user)

        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def get_products_title(self):
        products_title = self.driver.find_element(*self.PRODUCTS_TITLE)
        return products_title.text

    def get_error_message(self):
        error_message_box = self.driver.find_element(*self.ERROR_MESSAGE_BOX)
        return error_message_box.text