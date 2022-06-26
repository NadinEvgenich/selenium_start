from page_objects.MainPage import MainPage


def test_find_card(driver):
    cards = MainPage(driver).find_card()
    assert len(cards) == 4


def test_find_basket(driver):
    button = MainPage(driver).find_basket()
    assert button.text == "0 item(s) - $0.00"


def test_find(driver):
    MainPage(driver).verify_find()


def test_find_login(driver):
    main_page = MainPage(driver)
    main_page.click_caret()
    main_page.find_login()


def test_picture(driver):
    MainPage(driver).verify_picture()
