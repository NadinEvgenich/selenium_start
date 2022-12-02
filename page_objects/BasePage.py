import logging
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com"

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.handlers.clear()
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Открываю url {url}")
    def _open(self, url):
        self.logger.info("Opening url: {}".format(url))
        return self.driver.get(f"{self.base_url}{url}")

    @allure.step("Поиск локатора {locator}")
    def _verify_element(self, locator: tuple):
        self.logger.info(f"Check of element: {locator}")
        try:
            return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(name=f"{locator}",
                          body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError("Can't find element selector: {}".format(locator))

    @allure.step("Поиск страницы {title}")
    def _verify_title(self, title):
        self.logger.info(f"Check page: {title}")
        try:
            return WebDriverWait(self.driver, 2).until(EC.title_is(title))
        except TimeoutException:
            allure.attach(name=f"{title}",
                          body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError("Can't find page: {}".format(title))

    @allure.step("Проверка ссылки {link_text}")
    def _verify_link(self, link_text):
        self.logger.info(f"Check link: {link_text}")
        try:
            return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            allure.attach(name=f"{link_text}",
                          body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError("Can't find element by link text: {}".format(link_text))

    @allure.step("Получаю элемент {locator}")
    def _get_element(self, locator: tuple):
        return self._verify_element(locator)

    @allure.step("Кликаю на элемент {element}")
    def _click_element(self, element):
        element.click()
