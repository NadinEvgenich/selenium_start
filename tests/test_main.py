import allure
from page_objects.MainPage import MainPage


@allure.title('Проверка количества карточек с товаром на главной странице')
def test_find_card(driver):
    MainPage(driver)._open('/')
    cards = MainPage(driver).find_card()
    assert len(cards) == 4


@allure.title('Проверка, что в корзину ничего не добавлено')
def test_find_basket(driver):
    MainPage(driver)._open('/')
    button = MainPage(driver).find_basket()
    assert button.text == "0 item(s) - $0.00"


@allure.title('Проверка на наличие поисковика по сайту')
def test_find(driver):
    MainPage(driver)._open('/')
    MainPage(driver).verify_find()


@allure.title('Проверка на наличие раздела для авторизации')
def test_find_login(driver):
    main_page = MainPage(driver)
    main_page._open('/')
    main_page.click_caret()
    main_page.find_login()


@allure.title('Проверка на наличие логотипа на главной странице')
def test_picture(driver):
    MainPage(driver)._open('/')
    MainPage(driver).verify_picture()
