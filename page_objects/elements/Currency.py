from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class Currency(BasePage):
    CARET_DOWN = (By.CLASS_NAME, "fa.fa-caret-down")
    BUTTON_EUR = (By.CSS_SELECTOR, "button[name='EUR']")
    BUTTON_GBP = (By.CSS_SELECTOR, "button[name='GBP']")
    CURRENCY = (By.CSS_SELECTOR, "strong")

    def click_caret_down(self):
        self._click_element(self._get_element(self.CARET_DOWN))

    def click_button_eur(self):
        self._click_element(self._get_element(self.BUTTON_EUR))

    def click_button_gbp(self):
        self._click_element(self._get_element(self.BUTTON_GBP))

    def get_currency(self):
        currency = self.driver.find_element(*self.CURRENCY)
        return currency
