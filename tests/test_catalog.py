import allure
from page_objects.elements.Catalog import Catalog
from helpers import main_url


@allure.title('Проверка на наличие ссылки с компьютерами')
def test_find_desktops(driver):
    Catalog(driver)._open(main_url)
    Catalog(driver).get_desktops()


@allure.title('Переход на страницу с мониторами')
def test_find_monitor(driver):
    catalog = Catalog(driver)
    catalog._open(main_url)
    catalog.click_components()
    catalog.click_monitors()


@allure.title('Проверка названия раздела со всеми ноутбуками в каталоге')
def test_find_show_all(driver):
    catalog = Catalog(driver)
    catalog._open(main_url)
    catalog.click_laptops()
    button1 = catalog.get_show_all()
    assert button1.text == "Show All Laptops & Notebooks"


@allure.title('Проверка на наличие раздела с телефонами в каталоге')
def test_find_phones(driver):
    Catalog(driver)._open(main_url)
    Catalog(driver).verify_get_phone()


@allure.title('Проверка на наличие раздела с камерами в каталоге')
def test_find_cameras(driver):
    Catalog(driver)._open(main_url)
    Catalog(driver).verify_get_cameras()
