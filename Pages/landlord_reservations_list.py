from conftest import *
from selenium.webdriver.common.by import By





def open_landlord_reservations_list(browser, landlord_reservations_list):
    browser.get(landlord_reservations_list)
    browser.implicitly_wait(3)
    return browser



