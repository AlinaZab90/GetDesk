import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    yield browser
    print("\nquit browser..")
    browser.quit()


def login(browser):
    link = "https://getdesk.com/ru/login"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("...")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("...")

    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]')

    time.sleep(3)
    button.click()
    time.sleep(3)

#https://ru.stackoverflow.com/questions/894287/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-cookie-%D0%B2-selenium-%D0%9A%D0%B0%D0%BA-%D1%80%D0%B5%D1%88%D0%B8%D1%82%D1%8C-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-%D0%BF%D1%80%D0%B8-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B8


  #wait = WebDriverWait(browser, 5)
        #wait.until(
            #EC.text_to_be_present_in_element_attribute(
                #(By.CSS_SELECTOR, '[class="profile-btn-new-room"]'),
                #"class",
                #"profile"))