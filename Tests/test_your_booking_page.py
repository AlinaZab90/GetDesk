import conftest
from Pages.your_booking_page import *
from selenium.webdriver.common.by import By



your_booking_page_link = "https://getdesk.com/bookings/120"

class TestYourBookingPage:
    def test_your_booking_page(self, browser):
        open_your_booking_page(browser, your_booking_page_link)
        assert browser.find_element(By.XPATH, '//*[@class="h3"]').text == conftest.name
        #assert  conftest.price in browser.find_element(By.XPATH, '//*[@class="BookingItemPayment_price__8Nk7Z"]').text



    def test_canceled_button(self, browser):
        open_your_booking_page(browser, your_booking_page_link)
        d = canceled_block(browser)
        time.sleep(3)
        assert browser.find_element(By.XPATH, '//*[@class="BookingItemCancel_title__MguWH"]')


