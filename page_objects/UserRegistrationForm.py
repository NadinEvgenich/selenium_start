from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserRegistrationForm(BasePage):
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_INPUT = (By.ID, "input-confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    LOGIN_LINK = (By.LINK_TEXT, "login page")
    RADIOBUTTON = (By.CSS_SELECTOR, "input[name='newsletter']")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    def verify_page(self, title):
        self._verify_title(title)

    def click_login(self):
        self._click_element(self._get_element(self.LOGIN_LINK))

    def get_radiobutton(self):
        radiobutton = self.driver.find_elements(*self.RADIOBUTTON)
        return radiobutton

    def verify_checkbox(self):
        self._verify_element(self.CHECKBOX)

    def registration(self, first_name, last_name, email, phone, password):
        self._get_element(self.FIRSTNAME_INPUT).send_keys(first_name)
        self._get_element(self.LASTNAME_INPUT).send_keys(last_name)
        self._get_element(self.EMAIL_INPUT).send_keys(email)
        self._get_element(self.TELEPHONE_INPUT).send_keys(phone)
        self._get_element(self.PASSWORD_INPUT).send_keys(password)
        self._get_element(self.CONFIRM_INPUT).send_keys(password)
        self._click_element(self._get_element(self.CHECKBOX))
        self._click_element(self._get_element(self.CONTINUE_BUTTON))
