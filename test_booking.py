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
        a.send_keys("Kazan")

        browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/div/form/div[1]/div/div[2]/div/ul[2]/li[1]').click()
        browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()
        browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').click()



