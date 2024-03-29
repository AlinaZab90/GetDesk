import conftest
from selenium.webdriver.common.by import By
from Pages.renter_my_booking_list import *



my_booking_link = "https://getdesk.com/bookings/current"
class TestPageMyBookingList:
    def test_booking_list(self, browser):
        open_my_booking_list_page(browser, my_booking_link)
        assert browser.find_element(By.CSS_SELECTOR, '[class="styled-tabs"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="title"]').text == conftest.name
        assert browser.find_element(By.XPATH, '//*[@class="image"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="price"]').text == conftest.price
        assert browser.find_element(By.XPATH, '//*[@class="date"]').text == conftest.date

    def test_tab_completed(self, browser):
        open_my_booking_list_page(browser, my_booking_link)
        browser.find_element(By.LINK_TEXT, 'Завершенные').click()
        assert browser.current_url == "https://getdesk.com/bookings/completed"


    def test_tab_canceled(self, browser):
        open_my_booking_list_page(browser, my_booking_link)
        browser.find_element(By.LINK_TEXT, 'Отмененные').click()
        assert browser.current_url == "https://getdesk.com/bookings/removed"

