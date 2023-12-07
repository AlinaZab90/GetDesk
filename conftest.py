import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def login(browser):
    link = "https://getdesk.com/ru/login"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("alina.zabaidulina@mail.ru")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("Gasprom1990")

    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]')

    time.sleep(3)
    button.click()
    time.sleep(3)



  #wait = WebDriverWait(browser, 5)
        #wait.until(
            #EC.text_to_be_present_in_element_attribute(
                #(By.CSS_SELECTOR, '[class="profile-btn-new-room"]'),
                #"class",
                #"profile"))