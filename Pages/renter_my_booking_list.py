from conftest import browser


def open_my_booking_list_page(browser, my_booking_link):
    browser.get(my_booking_link)
    browser.implicitly_wait(10)
    return browser


