import time
from selenium.webdriver.common.by import By
from conftest import browser


class Test_Page_My_Booking:
    def test_booking_list(self, browser):
        browser.get("https://getdesk.com/bookings/current")
        assert browser.find_element(By.CSS_SELECTOR, '[class="styled-tabs"]').is_displayed()
