from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_card(driver):
    cards = driver.find_elements(By.CSS_SELECTOR, ".product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12")
    assert len(cards) == 4


def test_find_basket(driver):
    wait = WebDriverWait(driver, 1)
    button = wait.until(EC.visibility_of_element_located((By.ID, "cart-total")))
    assert button.text == "0 item(s) - $0.00"


def test_find(driver):
    assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.NAME, "search")))


def test_find_login(driver):
    driver.find_element(By.CSS_SELECTOR, ".caret").click()
    but = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
    assert but.text == "Login"


def test_picture(driver):
    assert WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title='Your Store']")))
