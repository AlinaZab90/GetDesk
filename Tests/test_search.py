import time
from selenium.webdriver.common.by import By
from conftest import *
from selenium.common.exceptions import NoSuchElementException
import base64

base_page_link = "https://getdesk.com/"
search_link = "https://getdesk.com/ru/search?booking_type=with_confirmation&zoom=11&ne_lat=72.03839295057298&ne_lng=102.61193105419922&sw_lat=71.88936343282951&sw_lng=102.26929494580078"


class TestSearch:

    def test_search(self, browser):
        browser.get(base_page_link)
        browser.implicitly_wait(10)
        a = browser.find_element(By.CSS_SELECTOR, '[id="mainSearchCity"]')
        a.click()
        a.send_keys("Chatanga")
        browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()
        instant_booking = browser.find_element(By.CSS_SELECTOR, "[class='switch-label']")
        assert instant_booking.is_displayed()


    def test_filter_date(self, browser):
#Выбор дневного диапазона
        browser.get('https://getdesk.com/ru/search?booking_type=with_confirmation&zoom=11&ne_lat=72.03955752527436&ne_lng=102.68437215527344&sw_lat=71.88818944451735&sw_lng=102.19685384472656')
        browser.find_element(By.XPATH, '//*[@id="filterDate"]').click()
        browser.find_element(By.XPATH, '//*[@class="lightpick__next-action"]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[15]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[16]').click()
        browser.find_element(By.XPATH, '//*[@data-set="setOfficeDateTime"]').click()
        time.sleep(2)

#Выбраны только часовые бронирования. При выборе дней - не отображатеся в поиске
        assert element_exist(browser, '//*[@data-location="49"]') == False


    def test_filter_hour(self, browser):
#Выбор часового диапазона
        date_start = "2026-03-16T05:00:00"
        date_end = "2026-03-16T23:00:00"
        date_start_bytes = date_start.encode("utf-8")
        date_end_bytes = date_end.encode("utf-8")
        date_start_base64 = base64.b64encode(date_start_bytes).decode("utf-8")
        date_end_base64 = base64.b64encode(date_end_bytes).decode("utf-8")
        url = f"https://getdesk.com/ru/search?dt_st={date_start_base64}&dt_ed={date_end_base64}&booking_type=with_confirmation&zoom=11&ne_lat=72.03770396155987&ne_lng=102.77191945751953&sw_lat=71.8863207808514&sw_lng=102.10930654248047"
        browser.get(url)
        assert element_exist(browser, '//*[@data-location="50"]') == False
        assert element_exist(browser, '//*[@data-location="66"]') == False
        assert browser.find_element(By.XPATH, '//*[@data-location="49"]').is_displayed()


    def test_type_of_spases(self, browser):
#Выбор типов помещения
        browser.get(search_link)
        browser.find_element(By.XPATH, '//*[@id="filterQuanti"]').click()
        browser.find_element(By.XPATH, '//input[@id="meeting_rooms"]/parent::*/span[@class="quantity-plus"]').click()
        browser.find_element(By.XPATH, '//*[@data-set="setOfficeParams"]').click()
        time.sleep(7)
        assert element_exist(browser, '//*[@data-location="50"]') == False
        assert element_exist(browser, '//*[@data-location="49"]') == False
        assert browser.find_element(By.XPATH, '//*[@data-location="66"]').is_displayed()



    def test_search_result(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="50"]').is_displayed()


    def test_booking_type_direct(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="50"]').is_displayed()
        browser.find_element(By.CSS_SELECTOR, '[class="switch-toggle"]').click()
        time.sleep(5)
        assert element_exist(browser, '//*[@data-location="50"]') == False

