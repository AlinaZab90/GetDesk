import time
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


login_link = "https://getdesk.com/en/login"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument(r"--user-data-dir=C:\Users\user\PycharmProjects\GetDesk\Google_Chrome")
    options.add_argument(r'--profile-directory=Profile 3')
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument('--enable-sync')

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    # browser.get("https://getdesk.com/")

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser_not_authorized():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()


def login(browser):
    link = "https://getdesk.com/xhr/index/auth"
    browser.get(link)
    status = json.loads(browser.find_element(By.TAG_NAME, 'pre').text)['message']
    if status:
        return

    browser.get("https://getdesk.com/ru/login")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("...")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("...")
    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]')
    button.click()


def click(element, browser):
    butt = str(element.location['y'])
    browser.execute_script(f"window.scrollTo (0, {butt:s})")
    time.sleep(3)
    element.click()
    time.sleep(2)


def get_request(browser, url):
    js = f'''
                   const req = new XMLHttpRequest();
           req.open("GET", "{url}", false);
           req.send();
           return req.response'''

    json_message = browser.execute_script(js)
    return json.loads(json_message)


def json_element(response, key):
    for i in response:
        if i["id"] != key:
            continue
        return i


name = "Эльтаун"
price = "Общая стоимость: 5 085 ₽"
date = "14.08.2023 - 16.08.2024"

# js =
'''const req = new XMLHttpRequest();
req.open("GET", "https://getdesk.com/xhr/office", false);
req.send();
return req.response'''
