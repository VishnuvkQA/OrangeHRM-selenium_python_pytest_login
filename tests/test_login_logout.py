import pytest
from pages.login_page import LoginPage
from pages.dash_page import Dashboard
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_login_dashboard_logout(driver):

    loginpage = LoginPage(driver)
    loginpage.login("Admin","admin123")

    dashboard = Dashboard(driver)
    assert dashboard.das_displayed()
    assert "/dashboard/index" in driver.current_url

    dashboard.open_drop()
    assert dashboard.logout_visible()

    dashboard.logout()
    assert "/auth/login" in driver.current_url

@pytest.mark.parametrize("username,password,expected_result",
                          [
                              ("Admin","admin123","valid"),("admin","random", "invalid"),("worng","Pass","invalid"), ("","","required"),],)

def test_login_validation(driver,username,password,expected_result):
    login_page = LoginPage(driver)
    login_page.login(username,password)

    if expected_result == "invalid":
        error = login_page.get_error()

        assert error.strip() != ""
        assert "auth/login" in driver.current_url

    elif expected_result == "required":
        errors = driver.find_elements(By.CSS_SELECTOR, ".oxd-input-field-error-message")

        assert len(errors) >=1 
        assert "auth/login" in driver.current_url

    elif expected_result == "valid":
        dashboard = Dashboard(driver)

        assert dashboard.das_displayed()
        assert "/dashboard/index" in driver.current_url

        dashboard.logout()
        assert "/auth/login" in driver.current_url