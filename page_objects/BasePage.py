from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _verify_element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Can't find element selector: {}".format(locator))

    def _verify_title(self, title):
        try:
            return WebDriverWait(self.driver, 2).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError("Can't find page: {}".format(title))

    def _verify_link(self, link_text):
        try:
            return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Can't find element by link text: {}".format(link_text))

    def _get_element(self, locator: tuple):
        return self._verify_element(locator)

    def _click_element(self, element):
        element.click()
