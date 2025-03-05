import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *



class TestBasePase:
    @pytest.mark.parametrize('language', ["en", "fr", "ru"])
    @allure.feature("Base Page Tests")
    @allure.story("Localization check")
    @allure.title("Check localization for '{language}'")
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

    def test_popular_slider(self, browser):
        browser.get('https://getdesk.com/')
        click(browser.find_element(By.XPATH, '//*[@id="mainPopularSlider"]/a'), browser)
        assert browser.find_element(By.XPATH, '//*[@class="office-page-title"]').is_displayed()

    def test_direct_slider(self, browser):
        browser.get('https://getdesk.com/')
        click(browser.find_element(By.XPATH, '//*[@id="mainDirectSlider"]/a'), browser)
        assert browser.find_element(By.XPATH, '//*[@class="office-page-title"]').is_displayed()


    def test_video_block_button(self, browser):
        browser.get('https://getdesk.com/')
        browser.execute_script("arguments[0].scrollIntoView();", browser.find_element(By.XPATH, '//*[contains(@class, "main-video-content")]'))
        time.sleep(2)
        browser.find_element(By.XPATH, '//section[@class="main-video"]//*[contains(@class,"main-video-content") and contains(@class,"fadeRight")]/a').click()
        assert browser.find_element(By.XPATH, '//*[@class="search-page_item"]').is_displayed()


    def test_promo_content(self, browser):
        browser.get('https://getdesk.com/')
        click(browser.find_element(By.XPATH, '//section[@class="main-promo"]//*[contains(@class,"main-promo-content") and contains(@class,"fadeRight")]/a'), browser)
        assert browser.find_element(By.XPATH, '//*[@class="business-tag"]')

