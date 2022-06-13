from selenium.webdriver.common.by import By


class PageRegisterAccount:
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
