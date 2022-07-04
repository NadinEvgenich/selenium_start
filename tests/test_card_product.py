from page_objects.CardPage import CardPage

path = "/MacBook"


def test_find_macbook(driver):
    driver.open(path)
    CardPage(driver).get_name()


def test_find_price(driver):
    driver.open(path)
    price = CardPage(driver).get_price()
    assert price.text == "$602.00"


def test_add_button(driver):
    driver.open(path)
    CardPage(driver).verify_get_add_button()


def test_image(driver):
    driver.open(path)
    images = CardPage(driver).get_images()
    assert len(images) == 4


def test_review(driver):
    driver.open(path)
    card_page = CardPage(driver)
    card_page.click_tab_reviews()
    button = card_page.get_continue_button()
    assert button.text == "Continue"
