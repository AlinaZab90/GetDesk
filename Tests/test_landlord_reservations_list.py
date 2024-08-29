import time
import conftest
from Pages.landlord_reservations_list import *
from selenium.webdriver.common.by import By

landlord_reservations_list = "https://getdesk.com/orders"


class TestLandlordReservationsList:
    def test_open_landlord_reservations_list(self, browser):
        open_landlord_reservations_list(browser, landlord_reservations_list)
        assert browser.find_element(By.XPATH, '//*[@class="wrapper-fast-filters-scroll"]').is_displayed()

    def test_landlord_tab(self, browser):
        open_landlord_reservations_list(browser, landlord_reservations_list)
        time.sleep(2)
        browser.find_element(By.XPATH, '//div[text()="Отмененные"]').click()
        time.sleep(2)

        assert browser.current_url == "https://getdesk.com/orders?page=1&status=canceled&sortBy=default&order=asc"
        #assert browser.find_element(By.XPATH, '//*[@class="number order-id"]').text == "163"
        assert browser.find_element(By.XPATH, '//*[@class="number order-transaction"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="section-item"]//div[@class="name"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="addres"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="date-time"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="order-price"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="renter"]//div[@class="name-wrapp"]').text == 'Алина\nЗабайдулина'


