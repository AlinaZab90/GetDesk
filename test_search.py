import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import browser
from conftest import login
from selenium.common.exceptions import NoSuchElementException

base_page_link = "https://getdesk.com/"
search_link = "https://getdesk.com/ru/search?booking_type=with_confirmation&zoom=11&ne_lat=55.892904072950344&ne_lng=37.986028637695306&sw_lat=55.61779259893132&sw_lng=37.24857136230468"


class TestBooking:

    def test_search(self, browser):
        # login(browser)
        browser.get(base_page_link)
        browser.implicitly_wait(10)
        a = browser.find_element(By.CSS_SELECTOR, '[id="mainSearchSity"]')
        a.click()
        a.send_keys("Moskow")

        browser.find_element(By.XPATH,
                             '//*[@id="content"]/div/div[1]/div/div/form/div[1]/div/div[2]/div/ul[2]/li[1]').click()
        browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()
        instant_booking = browser.find_element(By.CSS_SELECTOR, "[class='switch-label']")
        assert instant_booking.is_displayed()

    def test_search_result(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').is_displayed()

    def test_booking_type_direct(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '[class="switch-toggle"]').click()
        time.sleep(5)
        try:
            browser.find_element(By.CSS_SELECTOR, '[data-location="50"]')
            loc50 = True
        except NoSuchElementException:
            loc50 = False
        assert loc50 == False
