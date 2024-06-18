import time
from selenium.webdriver.common.by import By
from conftest import browser
from selenium.common.exceptions import NoSuchElementException

base_page_link = "https://getdesk.com/"
search_link = "https://getdesk.com/ru/search?booking_type=with_confirmation&zoom=11&ne_lat=72.03839295057298&ne_lng=102.61193105419922&sw_lat=71.88936343282951&sw_lng=102.26929494580078"


class TestSearch:

    def test_search(self, browser):
        # login(browser)
        browser.get(base_page_link)
        browser.implicitly_wait(10)
        a = browser.find_element(By.CSS_SELECTOR, '[id="mainSearchCity"]')
        a.click()
        a.send_keys("Chatanga")

        browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()
        instant_booking = browser.find_element(By.CSS_SELECTOR, "[class='switch-label']")
        assert instant_booking.is_displayed()

    def test_search_result(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="50"]').is_displayed()

    def test_booking_type_direct(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="50"]').is_displayed()
        browser.find_element(By.CSS_SELECTOR, '[class="switch-toggle"]').click()
        time.sleep(5)
        try:
            browser.find_element(By.CSS_SELECTOR, '[data-location="50"]')
            loc50 = True
        except NoSuchElementException:
            loc50 = False
        assert loc50 == False
