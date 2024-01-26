from selenium.webdriver.common.by import By
from conftest import browser
from Pages.my_booking_list import *



my_booking_link = "https://getdesk.com/bookings/current"
class TestPageMyBookingList:
    def test_booking_list(self, browser):
        open_my_booking_list_page(browser, my_booking_link)
        assert browser.find_element(By.CSS_SELECTOR, '[class="styled-tabs"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="title"]').text == "ТЦ Галактика"
        assert browser.find_element(By.XPATH, '//*[@class="image"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="price"]').text == "Общая стоимость: 226 ₽"
        assert browser.find_element(By.XPATH, '//*[@class="date"]').text == "30.07.2024 - 01.11.2025"

    def test_tab_completed(self, browser):
        open_my_booking_list_page(browser, my_booking_link)
        browser.find_element(By.LINK_TEXT, 'Завершенные').click()
        url = current_url(browser)
        assert url == "https://getdesk.com/bookings/completed"


    def test_tab_canceled(self, browser):
        open_my_booking_list_page(browser, my_booking_link)
        browser.find_element(By.LINK_TEXT, 'Отмененные').click()
        url = current_url(browser)
        assert url == "https://getdesk.com/bookings/removed"

