import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class Catalog(BasePage):
    COMPONENTS = (By.LINK_TEXT, "Components")
    MONITORS = (By.PARTIAL_LINK_TEXT, "Monitors")
    LAPTOPS = (By.LINK_TEXT, "Laptops & Notebooks")
    SHOW_ALL = (By.LINK_TEXT, "Show All Laptops & Notebooks")
    PHONE = (By.PARTIAL_LINK_TEXT, "Phones")
    CAMERAS = (By.LINK_TEXT, "Cameras")

    @allure.step("Нахожу ссылку на компьютеры в каталоге")
    def get_desktops(self):
        self._verify_link("Desktops")

    @allure.step("Выполняю клик по разделу с компонентами")
    def click_components(self):
        self._click_element(self._get_element(self.COMPONENTS))

    @allure.step("Выполняю клик по разделу с мониторами")
    def click_monitors(self):
        self._click_element(self._get_element(self.MONITORS))

    @allure.step("Выполняю клик по разделу с ноутбуками")
    def click_laptops(self):
        self._click_element(self._get_element(self.LAPTOPS))

    @allure.step("Получаю кнопку со всеми ноутбуками")
    def get_show_all(self):
        button = self.driver.find_element(*self.SHOW_ALL)
        return button

    @allure.step("Нахожу раздел с телефонами")
    def verify_get_phone(self):
        self._verify_element(self.PHONE)

    @allure.step("Нахожу раздел с камерами")
    def verify_get_cameras(self):
        self._verify_element(self.CAMERAS)
