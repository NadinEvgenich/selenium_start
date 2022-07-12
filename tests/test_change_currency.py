import allure
from page_objects.elements.Currency import Currency

url = "http://192.168.1.68:8081"


@allure.title('Переключение валюты на евро')
def test_change_currency_eur(driver):
    currency = Currency(driver)
    currency._open(url)
    currency.click_caret_down()
    currency.click_button_eur()
    cur = currency.get_currency()
    assert cur.text == "€"


@allure.title('Переключение валюты на фунты')
def test_change_currency_gbp(driver):
    currency = Currency(driver)
    currency._open(url)
    currency.click_caret_down()
    currency.click_button_gbp()
    cur1 = currency.get_currency()
    assert cur1.text == "£"
