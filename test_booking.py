import time
from selenium.webdriver.common.by import By
from conftest import browser
from conftest import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


office_page_link = "https://getdesk.com/ru/office/66"
class TestBooking:
    def test_booking_basket(self, browser):
        browser.get(office_page_link)
        browser.implicitly_wait(10)
        browser.execute_script("window.scrollTo (0, 800)")
        time.sleep(2)
#Выбор дат в календаре
        calendar = browser.find_element(By.CSS_SELECTOR, '[class="input-field-calendar-title"]')
        calendar.click()
        browser.find_element(By.CSS_SELECTOR, '[class="lightpick__next-action"]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[5]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[6]').click()
        browser.find_element(By.CSS_SELECTOR, '[id="btnChoiceDate"]').click()
#Добавление помещений в корзину
        browser.find_element(By.XPATH, '//button[@data-id="117"]').click()
        browser.execute_script("window.scrollTo (0, 1200)")
        time.sleep(2)
        browser.find_element(By.XPATH, '//button[@data-id="115"]').click()
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '[id="bookingRooms"]').click()
        time.sleep(3)
#Cloudpayments
        #iframe = browser.find_element(By.TAG_NAME, 'iframe')
        iframe = browser.find_element(By.XPATH, '//iframe[@allow="payment"]')
        browser.switch_to.frame(iframe)
        time.sleep(3)
        assert browser.find_element(By.CSS_SELECTOR, '[id="card"]').is_displayed()



