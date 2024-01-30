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
        browser.find_element(By.XPATH, '//div[text()="Предстоящие"]').click()
        time.sleep(2)
        url = current_url(browser)
        assert url == "https://getdesk.com/orders?page=1&status=paid&sortBy=default&order=asc"
        assert browser.find_element(By.XPATH, '//*[@class="number id"]').text == "184"

