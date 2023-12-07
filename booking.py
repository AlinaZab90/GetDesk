from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

try:
    getdesk = "https://getdesk.com/en/login"

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(getdesk)
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("alina.zabaidulina@mail.ru")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("Gasprom1990")
    browser.find_element(By.CSS_SELECTOR, '[class="btn btn-accent"]').click()

    link2 = "https://getdesk.com/"
    browser.get(link2)
    browser.implicitly_wait(10)
    a = browser.find_element(By.CSS_SELECTOR, '[id="mainSearchSity"]')
    a.click()
    a.send_keys("Kazan")

    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/div/form/div[1]/div/div[2]/div/ul[2]/li[1]').click()
    browser.find_element(By.CSS_SELECTOR, '[id="btnFindCity"]').click()

    browser.find_element(By.CSS_SELECTOR, '[data-location="66"]').click()
    #date = browser.find_element(By.PARTIAL_LINK_TEXT, "Выберите дату")



    date = browser.find_element(By.XPATH, '//*[@id="roomScrSel"]/div[1]/form/div/div/div[1]/div')
    #browser.execute_script("window.scrollBy(0,document.body.scrollHeight")
    date.click()


finally:
    time.sleep(5)
    browser.quit()

