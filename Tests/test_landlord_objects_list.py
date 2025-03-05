from Pages.landlord_objects_list import *
from conftest import *

landlord_objects_list_link = "https://getdesk.com/offices"


class TestLandlordObjects:

    def test_open_landlord_object_list(self, browser):
        open_landlord_objects_list(browser, landlord_objects_list_link)
        assert browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")]').is_displayed()
        assert browser.find_element(By.XPATH, '//*[contains(@class, "Item_title") and text()="Эльтаун"]').text == "Эльтаун"
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
        listing_status = browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/div[contains(@class, "Item_public")]').text
        browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")]/button[1]').click()
        listing_button = browser.find_element(By.XPATH, '//*[@class="Item_popover__zMEZw"]/li[2]')

        if listing_status == 'Не опубликовано':
            assert listing_button.text == "Опубликовать"
            listing_button.click()
            time.sleep(2)
            listing_status = browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/div[contains(@class, "Item_public")]').text
            assert listing_status == 'Опубликовано'
        else:
            assert listing_button.text == "Снять с публикации"
            listing_button.click()
            time.sleep(2)
            listing_status = browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")][2]/div[contains(@class, "Item_public")]').text
            assert listing_status == 'Не опубликовано'

    def test_menu_edit(self, browser):
        #login(browser)
        browser.get("http://getdesk:4c9hpVjbr9WWbcJ3rb@luna.getdesk.com/")
        browser.get('http://luna.getdesk.com/offices')
        browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@class="Item_popover__zMEZw"]/li[1]').click()
        assert browser.find_element(By.XPATH, '//*[contains(@class, "About_block")]').is_displayed()

    def test_menu_calendar(self, browser):
        browser.get("http://getdesk:4c9hpVjbr9WWbcJ3rb@luna.getdesk.com/")
        browser.get('http://luna.getdesk.com/offices')
        browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@class="Item_popover__zMEZw"]/li[3]').click()
        time.sleep(2)
        assert browser.find_element(By.XPATH, '//div[contains(@class, "Toolbar_month")]').is_displayed()

    def test_menu_object(self, browser):
        browser.get("http://getdesk:4c9hpVjbr9WWbcJ3rb@luna.getdesk.com/")
        browser.get('http://luna.getdesk.com/offices')
        browser.find_element(By.XPATH, '//*[contains(@class, "Item_wrapper")]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@class="Item_popover__zMEZw"]/li[4]').click()
        time.sleep(2)
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        assert browser.find_element(By.XPATH, '//div[@id="my-gallery"]').is_displayed()

