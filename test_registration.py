import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en", "fr"])
class TestRegistration:
    def test_registration(self, browser, language):
        link = f"http://dev.getdesk.com/profile?locale={language}"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
