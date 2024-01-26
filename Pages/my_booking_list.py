import time
from selenium.webdriver.common.by import By
from conftest import browser


def open_my_booking_list_page(browser, my_booking_link):
    browser.get(my_booking_link)
    browser.implicitly_wait(10)
    return browser

def current_url(browser):
    return browser.current_url