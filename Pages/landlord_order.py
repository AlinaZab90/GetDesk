import time
from conftest import *
from selenium.webdriver.common.by import By



def open_landlord_order(browser, landlord_order_link):
    browser.get(landlord_order_link)
    browser.implicitly_wait(3)
    time.sleep(2)
    return browser

def landlord_canceled_blok(browser):
    canceled_button = browser.find_element(By.XPATH, '//*[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium Button_button__1e85p Button_isDefault__FQC72 Button_isOutline__GkELK css-1hw9j7s"]')
    click(canceled_button, browser)
    message = browser.find_element(By.XPATH, '//*[@name="cancel_cause"]')
    click(message, browser)
    time.sleep(2)
    message.send_keys('Передумал')
    time.sleep(1)

#//*[contains(@class, 'Test')]
