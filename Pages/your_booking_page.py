from conftest import *
from selenium.webdriver.common.by import By



def open_your_booking_page(browser, your_booking_page_link):
    browser.get(your_booking_page_link)
    browser.implicitly_wait(3)
    return browser



def canceled_block(browser):
    canceled_button = browser.find_element(By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium Button_button__1e85p Button_isDefault__FQC72 Button_isWhite__5rAx9 BookingItemCancellation_button__HBwA8 css-1hw9j7s"]')
    click(canceled_button, browser)
    return canceled_button


