from Pages.landlord_objects_list import *
from conftest import *

landlord_objects_list_link = "https://getdesk.com/offices"


class TestLandlordObjects:

    def test_open_landlord_object_list(self, browser):
        open_landlord_objects_list(browser, landlord_objects_list_link)
        assert browser.find_element(By.XPATH, '//*[@class="ads-account-item"]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[@class="title" and text()="Эльтаун"]').text == "Эльтаун"
        assert browser.find_element(By.XPATH, '//*[@style]').is_displayed()

    def test_offices_status(self, browser):
        open_landlord_objects_list(browser, landlord_objects_list_link)
        url = "https://getdesk.com/xhr/office"
        response = get_request(browser, url)
        assert json_element(response, 66)["status"] == "published"


# response = webdriver.request('POST', 'url here', data={"param1": "value1"})
    def test_status_moderation(self, browser):
        browser.get("http://getdesk:4c9hpVjbr9WWbcJ3rb@luna.getdesk.com/")
        #browser.get('http://getdesk:4c9hpVjbr9WWbcJ3rb@luna.getdesk.com/ru/login')
        #browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("alina.zabaidulina@mail.ru")
        #browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("Gasprom1990")
        #time.sleep(3)
        #browser.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]').click()
        #time.sleep(2)
        url = 'http://luna.getdesk.com/offices'
        browser.get(url)
        time.sleep(2)
        assert (browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/div[contains(@class, "Item_admin")]')).text == 'Проверено'
        assert (browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/div[contains(@class, "Item_public")]')).text == 'Не опубликовано'
        browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/button[1]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//li[text()="Опубликовать"]').click()
        time.sleep(3)
        assert (browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/div[contains(@class, "Item_public")]')).text == 'Опубликовано'

