import time
from conftest import *
from Pages.editing_object import *
from selenium.webdriver.common.keys import Keys


link_object = "https://getdesk.com/offices/edit/66"


class TestEditingObject:
    def test_from_published_to_moderation(self, browser):
        open_object(browser, link_object)
        element = browser.find_element(By.XPATH, '//*[@name="description"]')
        click(element, browser)
        element.send_keys(Keys.CONTROL+Keys.END)
        element.send_keys("Cool!")
        time.sleep(2)

#Смена статуса на модерацию
        browser.find_element(By.XPATH, '//button[text()="Сохранить объект"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//button[text()="Сохранить"]').click()
        time.sleep(2)
        response = get_request(browser, "https://getdesk.com/xhr/office/66/edit")
        assert response["status"] == "moderation"

#Админ поднимает статус
        open_object(browser, "https://getdesk.com/panel/office/66?locale=ru")
        browser.find_element(By.XPATH, '//*[@data-ts-item and text()="На модерации"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@data-selectable and text()="Опубликовано"]').click()
        a = browser.find_element(By.XPATH, '//*[@formaction="https://getdesk.com/panel/office/66/save"]')
        time.sleep(1)
        a.click()
        browser.refresh()
        response = get_request(browser, "https://getdesk.com/xhr/office/66/edit")
        time.sleep(2)
        assert response["status"] == "published"






