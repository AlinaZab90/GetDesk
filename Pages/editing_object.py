from conftest import *


def open_object(browser, link_object):
    browser.get(link_object)
    browser.implicitly_wait(3)
    time.sleep(2)
    return browser
