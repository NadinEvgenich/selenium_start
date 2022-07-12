import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CardPage(BasePage):
    PRICE = (By.CSS_SELECTOR, "li>h2")
    IMAGE = (By.CSS_SELECTOR, ".image-additional")
    TAB = (By.CSS_SELECTOR, "a[href='#tab-review']")
    CONTINUE = (By.ID, "button-review")
    ADD_BUTTON = (By.CSS_SELECTOR, "#button-cart")

    @allure.step("Нахожу ссылку на товар")
    def get_name(self):
        self._verify_link("MacBook")

    @allure.step("Получаю стоимость товара")
    def get_price(self):
        price = self.driver.find_element(*self.PRICE)
        return price

    @allure.step("Нахожу кнопку для добавления товара в корзину")
    def verify_get_add_button(self):
        self._verify_element(self.ADD_BUTTON)

    @allure.step("Получаю изображения")
    def get_images(self):
        images = self.driver.find_elements(*self.IMAGE)
        return images

    @allure.step("Выполняю клик по табу для отзыва")
    def click_tab_reviews(self):
        self._click_element(self._get_element(self.TAB))

    @allure.step("Получаю кнопку для отправки отзыва о товаре")
    def get_continue_button(self):
        button = self.driver.find_element(*self.CONTINUE)
        return button
