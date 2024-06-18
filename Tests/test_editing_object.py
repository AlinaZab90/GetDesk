import time
from conftest import *
from Pages.editing_object import *
from selenium.webdriver.common.keys import Keys

id = "66"
link_object = f"https://getdesk.com/offices/edit/{id}"


class TestEditingObject:
    def test_from_published_to_moderation(self, browser):
        open_object(browser, link_object)
        element = browser.find_element(By.XPATH, '//*[@name="description"]')
        click(element, browser)
        element.send_keys(Keys.CONTROL + Keys.END)
        element.send_keys("Cool!")
        time.sleep(2)

        #Смена статуса на модерацию
        browser.find_element(By.XPATH, '//button[text()="Сохранить объект"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//button[text()="Сохранить"]').click()
        time.sleep(2)
        response = get_request(browser, f"https://getdesk.com/xhr/office/{id}/edit")
        assert response["status"] == "moderation"

        # Админ поднимает статус
        open_object(browser, f"https://getdesk.com/panel/office/{id}?locale=ru")
        browser.find_element(By.XPATH, '//*[@data-ts-item and text()="На модерации"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@data-selectable and text()="Опубликовано"]').click()
        a = browser.find_element(By.XPATH, f'//*[@formaction="https://getdesk.com/panel/office/{id}/save"]')
        time.sleep(1)
        a.click()
        browser.refresh()
        response = get_request(browser, f"https://getdesk.com/xhr/office/{id}/edit")
        time.sleep(2)
        assert response["status"] == "published"

    def test_from_published_to_draft(self, browser):
        open_object(browser, link_object)
        click(browser.find_element(By.XPATH, '//span[text()="3. Помещения"]'), browser)
        time.sleep(2)
#Добавление нового помещения
        click(browser.find_element(By.XPATH, '//*[@class="sf"]//*[@type="button"]'), browser)
        click(browser.find_element(By.XPATH, '//*[@class="zf"]/*[@type="button"][text()="Добавить"]'), browser)
        click(browser.find_element(By.XPATH, '//*[@class="lf"]/button[text()="Остаться"]'), browser)
        click(browser.find_element(By.XPATH, '//*[@class="vh wh"]/div[last()]'), browser)
#//*[@class="zf"]/*[@type="button"][text()="Добавить"]
#Статус черновик
        response = get_request(browser, f"https://getdesk.com/xhr/office/{id}/edit")
        assert response["status"] == "draft"
#Заполнение помещения
        browser.find_element(By.XPATH, '//*[@name="title"]').send_keys("Автотест")
        browser.find_element(By.XPATH, '//*[@name="description"]').send_keys("Заполнение описания автотестом!!")
        #Добавление фото
        img = browser.find_element(By.XPATH, '//input[@type="file"]')
        img.send_keys('C:/Users/user/Pictures/Снимок экрана 2023-12-28 142604.png')
        time.sleep(3)

        browser.find_element(By.XPATH, '//*[@name="square"]').send_keys("123")
        browser.find_element(By.XPATH, '//*[@name="price_hour"]').send_keys("77")
        browser.find_element(By.XPATH, '//*[@name="price_day"]').send_keys("3333")
        #browser.find_element(By.XPATH, '//*[@class="Checkbox_wrapper__7vR5o"][1]').click()

        #Сохранение помещения
        click(browser.find_element(By.XPATH, '//button[text()="Сохранить помещение"]'), browser)
        click(browser.find_element(By.XPATH, '//button[text()="Опубликовать"]'), browser)

        # Админ поднимает статус
        open_object(browser, f"https://getdesk.com/panel/office/{id}?locale=ru")
        browser.find_element(By.XPATH, '//*[@data-ts-item and text()="На модерации"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@data-selectable and text()="Опубликовано"]').click()
        a = browser.find_element(By.XPATH, f'//*[@formaction="https://getdesk.com/panel/office/{id}/save"]')
        time.sleep(1)
        a.click()
        browser.refresh()
        response = get_request(browser, f"https://getdesk.com/xhr/office/{id}/edit")
        time.sleep(2)
#Проверка статуса "опубликовано"
        assert response["status"] == "published"


