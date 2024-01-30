from conftest import *
from selenium.webdriver.common.by import By



def open_landlord_order(browser, landlord_order_link):
    browser.get(landlord_order_link)
    browser.implicitly_wait(3)
    return browser