from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPageLogin(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ADMIN_LINK = (By.CLASS_NAME, "navbar-brand")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

    def verify_page(self, title):
        self._verify_title(title)

    def get_opencart_link(self):
        self._verify_link("OpenCart")

    def verify_login_link(self):
        self._verify_element(self.ADMIN_LINK)

    def click_forgotten_password(self):
        self._click_element(self._get_element(self.FORGOTTEN_PASSWORD))

    def login(self, username, password):
        self._get_element(self.USERNAME_INPUT).send_keys(username)
        self._get_element(self.PASSWORD_INPUT).send_keys(password)
        self._click_element(self._get_element(self.SUBMIT_BUTTON))
