import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from conftest import browser
from conftest import login


class TestBooking:
    def test_search(self, browser):
        login(browser)

        base_page_link = "https://getdesk.com/"
        browser.get(base_page_link)

        browser.implicitly_wait(10)
        a = browser.find_element(By.CSS_SELECTOR, '[id="mainSearchSity"]')
        a.click()
        a.send_keys("Moskow")

        browser.find_element(By.XPATH,
                             '//*[@id="content"]/div/div[1]/div/div/form/div[1]/div/div[2]/div/ul[2]/li[1]').click()

        browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()

        #browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').click()
        def test_instant_booking():
            instant_booking = browser.find_element(By.CSS_SELECTOR, "[class='switch-label']")
            assert instant_booking.is_displayed()

        def test_result():
            result = browser.find_element(By.CSS_SELECTOR, "[id='currentLocation']")
            assert result.is_displayed()
        # instant_booking.click()
