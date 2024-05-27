import time
from selenium.webdriver.common.by import By
from conftest import browser


def open_page(browser, office_page_link):
    browser.get(office_page_link)
    browser.implicitly_wait(10)
    browser.execute_script("window.scrollTo (0, 800)")
    time.sleep(2)


def calculator(browser):
    calendar = browser.find_element(By.CSS_SELECTOR, '[class="input-field-calendar-title"]')
    calendar.click()
    browser.find_element(By.CSS_SELECTOR, '[class="lightpick__next-action"]').click()
    browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[15]').click()
    browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[16]').click()
    browser.find_element(By.CSS_SELECTOR, '[id="btnChoiceDate"]').click()
    return browser.find_element(By.CSS_SELECTOR, '[class="office-page-calendar-note"]').text


def booking_basket(browser):
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, '//button[@data-id="117"]').click()
    browser.execute_script("window.scrollTo (0, 1200)")
    time.sleep(2)
    browser.find_element(By.XPATH, '//button[@data-id="115"]').click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '[id="bookingRooms"]').click()
    time.sleep(2)
    return browser.find_element(By.CSS_SELECTOR, '[class="to-result"]').text
#//*[@class="to-result"]/span


def iframe(browser):
    iframe = browser.find_element(By.XPATH, '//iframe[@allow="payment"]')
    browser.switch_to.frame(iframe)
    time.sleep(2)
    return browser.find_element(By.CSS_SELECTOR, '[class="text p0 cost-value"]').text
