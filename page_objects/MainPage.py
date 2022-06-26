from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    CARDS = (By.CSS_SELECTOR, ".product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12")
    BASKET = (By.ID, "cart-total")
    CARET = (By.CSS_SELECTOR, ".caret")
    FIND = (By.NAME, "search")
    LOGO = (By.CSS_SELECTOR, "img[title='Your Store']")

    def find_card(self):
        cards = self.driver.find_elements(*self.CARDS)
        return cards

    def find_basket(self):
        button = self.driver.find_element(*self.BASKET)
        return button

    def click_caret(self):
        self._click_element(self._get_element(self.CARET))

    def find_login(self):
        self._verify_link("Login")

    def verify_find(self):
        self._verify_element(self.FIND)

    def verify_picture(self):
        self._verify_element(self.LOGO)
