import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import browser
from conftest import login


class TestLogin:
    def test_login(self, browser):
        login(browser)
        element = browser.find_element(By.CSS_SELECTOR, '[class="profile-btn-new-room"]')

        assert element.get_attribute("class") == "profile-btn-new-room"


#[class="profile-btn-new-room"]
# '//*[@class="left"]'