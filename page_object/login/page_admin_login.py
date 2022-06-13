from selenium.webdriver.common.by import By


class PageAdminLogin:
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ADMIN_LINK = (By.CLASS_NAME, "navbar-brand")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, "OpenCart")
