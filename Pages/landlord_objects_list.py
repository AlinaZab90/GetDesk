import time
from conftest import *
from selenium.webdriver.common.by import By


def open_landlord_objects_list(browser, landlord_objects_list_link):
    browser.get(landlord_objects_list_link)
    browser.implicitly_wait(3)
    time.sleep(2)
    return browser



