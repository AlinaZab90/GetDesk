import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


