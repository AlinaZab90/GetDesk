import time
from selenium.webdriver.common.by import By
from Pages.landlord_order import *
from conftest import *



landlord_order_link = "https://getdesk.com/orders/184"


class TestLandlordOrder:
    def test_landlord_order_open(self, browser):
        open_landlord_order(browser, landlord_order_link)
        assert browser.find_element(By.XPATH, '//div[@class="date"]').is_displayed()
        assert browser.find_element(By.XPATH, '//div[text()="Оплачено"]').text == "Оплачено"
        assert browser.find_element(By.XPATH, '//*[text()="Эльтаун"]').text == 'Эльтаун'
        assert browser.find_element(By.XPATH, '//*[@class="wr-info-list"]').is_displayed()

    def test_landlord_canceled(self, browser):
        open_landlord_order(browser, landlord_order_link)
        landlord_canceled_blok(browser)
        time.sleep(2)
        assert browser.find_element(By.XPATH, '//*[not(@disabled) and text()="Отправить заявку на отмену"]')
