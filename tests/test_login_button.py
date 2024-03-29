import allure
from selene import browser, have

from test_kazanexpress.pages.login_page import LoginPage


def test_login_button():
    login_page = LoginPage()

    login_page.open()
    login_page.click_login_button()
    login_page.should_pop_up_visible()





