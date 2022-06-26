import os
from selenium.webdriver.common.by import By
from .BasePage import BasePage
from selenium.webdriver.support.select import Select


class AdminPage(BasePage):
    CATALOG = (By.LINK_TEXT, "Catalog")
    PRODUCTS = (By.LINK_TEXT, "Products")
    ADD_NEW = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    PRODUCT_NAME = (By.ID, "input-name1")
    DESCRIPTION = (By.CLASS_NAME, "note-editable")
    META_TAGS = (By.ID, "input-meta-title1")
    TAB_DATA = (By.LINK_TEXT, "Data")
    MODEL = (By.ID, "input-model")
    PRICE = (By.ID, "input-price")
    QUANTITY = (By.ID, "input-quantity")
    SELECT_TAX_CLASS = (By.ID, "input-tax-class")
    SAVE = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    ALERT = (By.CLASS_NAME, "alert.alert-success.alert-dismissible")
    CLOSE_ALERT = (By.CSS_SELECTOR, '[data-dismiss="alert"]')
    FILTER_PRODUCT_NAME = (By.ID, "input-name")
    BTN_FILTER = (By.ID, "button-filter")
    TABLE = (By.XPATH, "//tr")
    CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    DELETE = (By.CLASS_NAME, "btn-danger")

    def go_to_product(self):
        self._click_element(self._get_element(self.CATALOG))
        self._click_element(self._get_element(self.PRODUCTS))

    def create_product(self, name, text, tag, model, price, quantity):
        self._click_element(self._get_element(self.ADD_NEW))
        self._get_element(self.PRODUCT_NAME).send_keys(name)
        self._get_element(self.DESCRIPTION).send_keys(text)
        self._get_element(self.META_TAGS).send_keys(tag)
        self._click_element(self._get_element(self.TAB_DATA))
        self._get_element(self.MODEL).send_keys(model)
        self._get_element(self.PRICE).send_keys(price)
        self._get_element(self.QUANTITY).send_keys(quantity)
        select = Select(self.driver.find_element(*self.SELECT_TAX_CLASS))
        select.select_by_visible_text("Taxable Goods")
        self._click_element(self._get_element(self.SAVE))
        self._verify_element(self.ALERT)
        self._click_element(self._get_element(self.CLOSE_ALERT))

    def verify_product(self, name):
        self._get_element(self.FILTER_PRODUCT_NAME).send_keys(name)
        self._click_element(self._get_element(self.BTN_FILTER))
        el = self.driver.find_elements(*self.TABLE)
        if len(el) < 2:
            raise AssertionError("Product not created!")
        if len(el) > 2:
            raise AssertionError("Product not deleted!")

    def delete_product(self):
        self._click_element(self.driver.find_elements(*self.CHECKBOX)[1])
        self._click_element(self._get_element(self.DELETE))
        alert = self.driver.switch_to.alert
        alert.accept()
