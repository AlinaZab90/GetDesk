import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

class TestBasePase:
    @pytest.mark.parametrize('language', ["ru", "en", "fr"])
    def test_base_page(self, browser, language):
        link = f"https://getdesk.com/{language}"
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, "[id='btnFindCity']")
        wait = WebDriverWait(browser, 5)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[id='btnFindCity']"))
        )
        localization = {"ru": "Найти", "en": "Find", "fr": "Trouver"}

        assert button.is_displayed()
        assert button.text == localization[language]

