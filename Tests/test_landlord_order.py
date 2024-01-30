import time

from selenium.webdriver.common.by import By
from Pages.landlord_order import *



landlord_order_link = "https://getdesk.com/orders/184"

def test_landlord_order_open(browser):
    open_landlord_order(browser, landlord_order_link)
    time.sleep(3)