import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    #browser.get("https://getdesk.com/")

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
    link = "https://getdesk.com/ru/login"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("...")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("...")

    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]')
    button.click()

    time.sleep(3)
    button.click()
    time.sleep(3)



def click(element, browser):
    butt = str(element.location['y'])
    browser.execute_script(f"window.scrollTo (0, {butt:s})")
    time.sleep(1)
    element.click()


def current_url(browser):
    return browser.current_url

name = "ТЦ Галактика"
price = "Общая стоимость: 226 ₽"
date = "30.07.2024 - 01.11.2025"

