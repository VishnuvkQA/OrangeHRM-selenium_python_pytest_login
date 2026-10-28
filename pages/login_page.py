from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.loginbtn = (By.CSS_SELECTOR, ".orangehrm-login-button")
        self.error_msg = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    # Functions
    def enter_username(self, username):
        self.wait.until(
            ec.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            ec.visibility_of_element_located(self.password)
        ).send_keys(password)

    def click_btn(self):
        self.wait.until(
            ec.element_to_be_clickable(self.loginbtn)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_btn()

    def get_error(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.error_msg)
        ).text