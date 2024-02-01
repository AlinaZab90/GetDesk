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
