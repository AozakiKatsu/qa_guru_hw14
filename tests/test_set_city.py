from test_kazanexpress.pages.city_page import city_page


def test_set_city():
    city_page.open()

    city_page.click_set_city()
    city_page.choose_city()

    city_page.check_selected_city()
