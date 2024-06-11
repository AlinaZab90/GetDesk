from conftest import *
from selenium.webdriver.common.by import By



def open_your_booking_page_renter(browser, your_booking_page_link):
    browser.get(your_booking_page_link)
    browser.implicitly_wait(3)
    return browser



def canceled_block_renter(browser):
    time.sleep(3)
    canceled_button = browser.find_element(By.XPATH, '//*[@class="xb"]/button')
    click(canceled_button, browser)
    return canceled_button


