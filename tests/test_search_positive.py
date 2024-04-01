from test_kazanexpress.pages.search_page import search_page


def test_search_positive():
    search_page.open()

    search_page.fill_search_input()

    search_page.check_search_results()
