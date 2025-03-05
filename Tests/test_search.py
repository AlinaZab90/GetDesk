import time
from selenium.webdriver.common.by import By
from conftest import *
from selenium.common.exceptions import NoSuchElementException
import base64

base_page_link = "https://getdesk.com/"
search_link = "https://getdesk.com/ru/search?booking_type=with_confirmation&zoom=11&ne_lat=72.03839295057298&ne_lng=102.61193105419922&sw_lat=71.88936343282951&sw_lng=102.26929494580078"


class TestSearch:

    def test_search(self, browser):
#Переход в поиск
        browser.get(base_page_link)
        browser.implicitly_wait(10)
        a = browser.find_element(By.CSS_SELECTOR, '[id="mainSearchCity"]')
        a.click()
        a.send_keys("Chatanga")
        browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()
        instant_booking = browser.find_element(By.CSS_SELECTOR, "[class='switch-label']")
        assert instant_booking.is_displayed()

    def test_search_result(self, browser):
#Отображение объектов
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="50"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-location="49"]').is_displayed()


    def test_filter_date(self, browser):
#Выбор дневного диапазона
        browser.get('https://getdesk.com/ru/search?booking_type=with_confirmation&zoom=11&ne_lat=72.03955752527436&ne_lng=102.68437215527344&sw_lat=71.88818944451735&sw_lng=102.19685384472656')
        browser.find_element(By.XPATH, '//*[@id="filterDate"]').click()
        browser.find_element(By.XPATH, '//*[@class="lightpick__next-action"]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[15]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[16]').click()
        browser.find_element(By.XPATH, '//*[@data-set="setOfficeDateTime"]').click()
        time.sleep(2)

#Есть только цена за час. При выборе дней - не отображатеся в поиске
        assert element_exist(browser, '//*[@data-location="49"]') == False
        assert browser.find_element(By.XPATH, '//*[@data-location="50"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@data-location="66"]').is_displayed()


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


    def test_amenitys(self, browser):
#Выбор удобства
        browser.get(search_link)
        browser.find_element(By.XPATH, '//*[@id="filterCheck"]').click()
        click(browser.find_element(By.XPATH, '//*[@for="amenity32"]'), browser)
        click(browser.find_element(By.XPATH, '//*[@data-set="setOfficeAmenities"]'), browser)
        time.sleep(3)
        assert element_exist(browser, '//*[@data-location="50"]') == False
        assert element_exist(browser, '//*[@data-location="66"]') == False
        assert browser.find_element(By.XPATH, '//*[@data-location="49"]').is_displayed()





    def test_booking_type_direct(self, browser):
        browser.get(search_link)
        browser.implicitly_wait(10)
        assert browser.find_element(By.XPATH, '//*[@data-location="49"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@data-location="50"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@data-location="66"]').is_displayed()
        browser.find_element(By.XPATH, '//*[@class="switch-button"]').click()
        time.sleep(3)
        assert element_exist(browser, '//*[@data-location="49"]') == False
        assert element_exist(browser, '//*[@data-location="50"]') == False
        browser.find_element(By.XPATH, '//*[@data-location="66"]').is_displayed()


    def test_all_filters(self, browser):
        browser.get(search_link)
        assert browser.find_element(By.XPATH, '//*[@data-location="49"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@data-location="50"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@data-location="66"]').is_displayed()
#Даты и тип помещения = отображается стоимость
        browser.find_element(By.XPATH, '//*[@id="filterDate"]').click()
        browser.find_element(By.XPATH, '//*[@class="lightpick__next-action"]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[15]').click()
        browser.find_element(By.XPATH, '//div[@class="lightpick__days"]/div[16]').click()
        browser.find_element(By.XPATH, '//*[@data-set="setOfficeDateTime"]').click()

        browser.find_element(By.XPATH, '//*[@id="filterQuanti"]').click()
        browser.find_element(By.XPATH, '//input[@id="meeting_rooms"]/parent::*/span[@class="quantity-plus"]').click()
        browser.find_element(By.XPATH, '//*[@data-set="setOfficeParams"]').click()
        time.sleep(3)
        assert browser.find_element(By.XPATH, '//*[@class="search-page_item-price-label"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="search-page_item-price-cost"]').is_displayed()
        summ = browser.find_element(By.XPATH, '//*[@class="search-page_item-price-cost"]').text
        assert summ.replace(' ', '') == '2000₽'


    def test_ya_s(self, browser):
        link = 'https://yandex.ru/maps/?display-text=%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3&ll=94.631778%2C54.550365&mode=search&sctx=ZAAAAAgBEAAaKAoSCUZe1sQC8VRAEV6EKcqll0tAEhIJ7BaBsb6wX0ARAFKbOLkbSUAiBgABAgMEBSgKOABA4QFIAWoCcnWdAc3MzD2gAQCoAQC9AQBdoonCAdMGlruGkd8EnsnVzIUFzpryrIEDx%2FvWmAetq9m%2BdouWuPsEh6%2BIuJ4C%2FJasjeUEj6CYutQEifuFkd8Ducya6AWAzIW8ugOsn6qJ0gSmp6rGswOnsYT%2B%2BAPM56j2%2BQG7%2Ftv%2F2gTtqOrczATQn5K8xQTZjZXSswSHvP7MuwGLmeqLgQW%2B9aKgOvzp5aBCnYfhtAa82Y65mQSv5fyVcOGwnOaVBOnXjr8GqvOFuoQBvY721wSc9PaRjgKsltzfO%2BmEs613u62YqJcD0LXSzwSLpNjd5QSPsc2jpQSM8%2BLSsATkva%2BatgPEseDJkAOykZyhkgTskq%2Fe%2BwOa7pLhkgTZ3I6TBavwopgFrraG%2Bgap4vzSxAb%2Bq%2FfvhAHVmKaFBdKZpYOIBJCt6aDWBo66hfC7A5Xrt9DKBIjP8sTdBMT0ierKBuSQqtuABqHj%2Fq%2BCAZfo4Iv%2FBPvq7eaCA5rkpObaBJaAtIwE%2Fby0sdEDh4X8nQTerYq5hwXOzJaKcfWJj%2FMEqaXZ9PMC3sPNuGnzn6z%2FOI28qdSFBbCNia8E5KOs3JQBjb2KodcCmaKpqf8Bysa%2Fut0EtPiRi5YG9KK%2FtsoF4YDSvdUEmvT0vQTfnbi4igHEhuKzpgTmt%2F6SrwSZr%2BS7Rc7oyYfxA%2FmokvnkA9umvuQKpsCR6fkFtOLkzwaE2vCOugaj3uCu4gWY%2FLz5iwLM0d%2BxogPf6LyH1AON1eHIiwSz3vfj8QTv662NBfWMo5vLAqWyguiJAtO3l7HSBKHMnuQD9oil9gOoxKXczAG7u9mgZImjt5zlBNaHy%2FpkrpvO6kKJxuD%2FA8DFj679Arvuyrn1BIL9kewNnfrbs1T26%2BacnAO9ktHB%2BwSKn7LHsQS8q9b9iAPL%2FOCVrATPjs%2Br6QL6gty%2B%2FQSsnNvunwLPpJ%2BX%2FgPvz9%2Bc3wKR092QkASns%2BLuogO1or%2Fi9QKEgqTr2QX2idO29wLOtY%2FVBJeyxY%2B2A5%2Bv66uqBLXPyOU9w8LcwAWJxYGaBNvm7oG6BOHJ7d4GwZyCi74DkL2grNMD142hn40Er%2FmxuQaNj%2F3HBOT%2Bj9yjBLfSkucDjZPX77gDhbjRrwSwzPj9N46W49pxmMDHjYoDsozEhcsG6Imb8I0D7cCXugaCAh0oKGNhdGVnb3J5X2lkOig2MDkzNDc2NjA4MSkpKYoCCzYwOTM0NzY2MDgxkgIAmgIMZGVza3RvcC1tYXBzqgL5ATIyMTM1MDI4MTk3NCw4ODY1NTk2MjQxOCw4MTExMDAwOTgyNSwyNDMzNzU0NzY5MzAsNzQ4NzEzODE5MDAsMTQ4Njg5Njc1Nzc3LDExNzk1NzQ4NjE1MSw1MzI1Mjg0NjIxMywyMjkyMDI3NjQxNDIsNzY2NDk3NzEzMzgsMjQ1MTg4Mjc4NSwzMzAyMzg1NzUxOCwxNDc1Mzg3MjI3MjQsMTI1MDAzMjQxNDc1LDE3NzE5MjE4Njk2NSwxNDI2NDI0OTIyODAsNDUxMzU4MDI5MTUsMTU2ODk4MDU0NzYyLDE4ODE5NjM2NTMyNSw4ODUyNzQ4ODgxOA%3D%3D&sll=94.631778%2C54.550365&sspn=162.689170%2C65.863233&text=%7B%22text%22%3A%22%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22category_id%22%2C%22attr_values%22%3A%5B%2260934766081%22%5D%7D%5D%7D&z=3.27'
        browser.get(link)
        scroll_container = browser.find_element(By.XPATH, '//div[contains(@class, "scroll__container")]')

        browser.execute_script("arguments[0].scrollTop += 2000;", scroll_container)
        time.sleep(3)
        browser.execute_script("arguments[0].scrollTop += 2000;", scroll_container)
        time.sleep(2)
        browser.execute_script("arguments[0].scrollTop += 2000;", scroll_container)
        time.sleep(2)


