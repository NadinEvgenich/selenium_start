from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class Catalog(BasePage):
    COMPONENTS = (By.LINK_TEXT, "Components")
    MONITORS = (By.LINK_TEXT, "Monitors (2)")
    LAPTOPS = (By.LINK_TEXT, "Laptops & Notebooks")
    SHOW_ALL = (By.LINK_TEXT, "Show All Laptops & Notebooks")
    PHONE = (By.PARTIAL_LINK_TEXT, "Phones")
    CAMERAS = (By.LINK_TEXT, "Cameras")

    def get_desktops(self):
        self._verify_link("Desktops")

    def click_components(self):
        self._click_element(self._get_element(self.COMPONENTS))

    def click_monitors(self):
        self._click_element(self._get_element(self.MONITORS))

    def click_laptops(self):
        self._click_element(self._get_element(self.LAPTOPS))

    def get_show_all(self):
        button = self.driver.find_element(*self.SHOW_ALL)
        return button

    def verify_get_phone(self):
        self._verify_element(self.PHONE)

    def verify_get_cameras(self):
        self._verify_element(self.CAMERAS)
