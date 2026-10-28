from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class Dashboard:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.dash_heading = (
            By.XPATH, "//h6[normalize-space()='Dashboard']"
        )
        self.dropdown = (
            By.CSS_SELECTOR, ".oxd-userdropdown-tab"
        )
        self.logout_link = (By.LINK_TEXT, "Logout")

    def das_displayed(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.dash_heading)
        ).is_displayed()

    def open_drop(self):
        self.wait.until(
            ec.element_to_be_clickable(self.dropdown)
        ).click()

    def logout_visible(self):
        return self.wait.until(ec.visibility_of_element_located((self.logout_link))).is_displayed()

    def open_logout(self):
        self.wait.until(
            ec.element_to_be_clickable(self.logout_link)
        ).click()

    def logout(self):
        self.open_drop()
        time.sleep(2)
        self.open_logout()
        time.sleep(2)