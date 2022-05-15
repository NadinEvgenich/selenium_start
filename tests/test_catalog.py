from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_desktops(driver):
    wait = WebDriverWait(driver, 1)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "collapse.navbar-collapse.navbar-ex1-collapse")))
    el = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))
    wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, "Desktops"), "Desktops"))
    assert el.text == "Desktops"


def test_find_monitor(driver):
    driver.find_element(By.LINK_TEXT, "Components").click()
    button = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, "Monitors (2)")))
    button.click()
    WebDriverWait(driver, 1).until(EC.staleness_of(button))


def test_find_show_all(driver):
    driver.find_element(By.LINK_TEXT, "Laptops & Notebooks").click()
    button1 = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Show All Laptops & Notebooks")))
    assert button1.text == "Show All Laptops & Notebooks"


def test_find_phones(driver):
    assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Phones")))


def test_find_cameras(driver):
    assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Cameras")))
