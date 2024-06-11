import conftest
from Pages.renter_your_booking_page import *
from selenium.webdriver.common.by import By



your_booking_page_link = "https://getdesk.com/bookings/67"

class TestYourBookingPage:
    def test_your_booking_page(self, browser):
        open_your_booking_page_renter(browser, your_booking_page_link)
        assert browser.find_element(By.XPATH, '//*[@class="h3"]').text == conftest.name
        #assert  conftest.price in browser.find_element(By.XPATH, '//*[@class="BookingItemPayment_price__8Nk7Z"]').text



    def test_canceled_button(self, browser):
        open_your_booking_page_renter(browser, your_booking_page_link)
        d = canceled_block_renter(browser)
        time.sleep(3)
        button = browser.find_element(By.XPATH, '//*[@class="Pd"]/button')
        assert button.is_displayed()
        button.click()
        time.sleep(2)
        assert browser.find_element(By.XPATH, '//*[@name="cancel_cause"]').is_displayed()


