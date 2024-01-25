import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import browser
from conftest import login


class TestLogin:
    def test_login(self, browser_not_authorized):
        browser_not_authorized.get("https://getdesk.com/en/registration")
        browser_not_authorized.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys("Test")
        browser_not_authorized.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("Test55")
        browser_not_authorized.find_element(By.CSS_SELECTOR, '[name="password-repeat"]').send_keys("Test55")
        browser_not_authorized.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        time.sleep(3)
        assert browser_not_authorized.find_element(By.CSS_SELECTOR, '[class="errors"]').is_displayed()


