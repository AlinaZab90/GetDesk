import time
from selenium.webdriver.common.by import By
from conftest import browser
from conftest import browser_not_authorized
from conftest import login_link




class TestLogin:
    def test_authorized_test_browser(self, browser):
        browser.get("https://getdesk.com/")
        browser.find_element(By.CSS_SELECTOR, '[class="user-btn"]').click()
        time.sleep(2)
        auth = browser.find_element(By.XPATH, '//a[text()="Профиль"]').text
        assert auth == "Профиль"

    def test_google_authorized(self, browser_not_authorized):
        browser_not_authorized.get(login_link)
        browser_not_authorized.implicitly_wait(10)
        browser_not_authorized.find_element(By.XPATH, '//*[text()="Login with Google"]').click()
        assert browser_not_authorized.find_element(By.CSS_SELECTOR, '[id="identifierId"]').is_displayed()

    def test_invalid_data(self, browser_not_authorized):
        browser_not_authorized.get(login_link)
        browser_not_authorized.implicitly_wait(10)
        browser_not_authorized.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("test@mail.ru")
        browser_not_authorized.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("Testtest12345")
        time.sleep(5)
        browser_not_authorized.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]').click()
        time.sleep(5)
        error = browser_not_authorized.find_element(By.XPATH, '//*[text()="Incorrect login or password"]').text
        assert error == "Incorrect login or password"

