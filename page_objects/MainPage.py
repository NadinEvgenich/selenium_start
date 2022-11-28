import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    CARDS = (By.CSS_SELECTOR, ".product-thumb")
    BASKET = (By.CSS_SELECTOR, ".fas.fa-shopping-cart")
    CARET = (By.CSS_SELECTOR, ".fas.fa-caret-down")
    FIND = (By.NAME, "search")
    LOGO = (By.CSS_SELECTOR, "img[title='Your Store']")

    @allure.step("Получаю карточки с товарами")
    def find_card(self):
        cards = self.driver.find_elements(*self.CARDS)
        return cards

    @allure.step("Получаю кнопку корзины")
    def find_basket(self):
        button = self.driver.find_element(*self.BASKET)
        return button

    @allure.step("Выполняю клик по значку выпадающего списка")
    def click_caret(self):
        self._click_element(self._get_element(self.CARET))

    @allure.step("Нахожу ссылку для авторизации")
    def find_login(self):
        self._verify_link("Login")

    @allure.step("Нахожу инпут для поиска")
    def verify_find(self):
        self._verify_element(self.FIND)

    @allure.step("Нахожу логотип")
    def verify_picture(self):
        self._verify_element(self.LOGO)
