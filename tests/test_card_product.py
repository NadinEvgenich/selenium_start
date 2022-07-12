import allure
from page_objects.CardPage import CardPage

url = "http://192.168.1.68:8081/MacBook"


@allure.title('Проверка на наличие ссылки для товара в его карточке')
def test_find_macbook(driver):
    CardPage(driver)._open(url)
    CardPage(driver).get_name()


@allure.title('Проверка стоимости макбука')
def test_find_price(driver):
    CardPage(driver)._open(url)
    price = CardPage(driver).get_price()
    assert price.text == "$602.00"


@allure.title('Проверка на наличие кнопки для добавления товара в корзину')
def test_add_button(driver):
    CardPage(driver)._open(url)
    CardPage(driver).verify_get_add_button()


@allure.title('Проверка количества изображений с товаром')
def test_image(driver):
    CardPage(driver)._open(url)
    images = CardPage(driver).get_images()
    assert len(images) == 4


@allure.title('Проверка на наличие кнопки для отправки отзыва о товаре')
def test_review(driver):
    card_page = CardPage(driver)
    card_page._open(url)
    card_page.click_tab_reviews()
    button = card_page.get_continue_button()
    assert button.text == "Continue"
