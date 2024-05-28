from conftest import browser
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
        assert summ == 'Итого\n5000 ₽'


#Cloudpayments
    def test_iframe(self, browser):
        open_page(browser, office_page_link)
        calculator(browser)
        summ_gd = booking_basket(browser)
        cp_summ = (iframe(browser))
        assert cp_summ == summ_gd

