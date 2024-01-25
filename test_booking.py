import time
from selenium.webdriver.common.by import By
from conftest import browser
from conftest import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.booking_page import *

office_page_link = "https://getdesk.com/ru/office/66"
class TestBooking:
    def test_open_booking_page(self, browser):
        open_page(browser, office_page_link)
        assert browser.find_element(By.XPATH, '//*[@class="office-page-space-head"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="office-page-space-item__instant"]').is_displayed()


#Выбор дат в календаре
    def test_calendar(self, browser):
        open_page(browser, office_page_link)
        message = calculator(browser)
        assert message == "Время бронирования рассчитывается по местному времени объекта"

#Добавление помещений в корзину
    def test_booking_basket(self, browser):
        open_page(browser, office_page_link)
        calculator(browser)
        summ = booking_basket(browser)
        assert summ == 'Итого\n5 650 ₽'


#Cloudpayments
    def test_iframe(self, browser):
        open_page(browser, office_page_link)
        calculator(browser)
        booking_basket(browser)
        f = iframe(browser)
        assert f.find_element(By.CSS_SELECTOR, '[id="card"]').is_displayed()



