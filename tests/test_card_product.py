from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_macbook(driver):
    driver.get(driver.url + "/MacBook")
    wait = WebDriverWait(driver, 1)
    pic = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "MacBook")))
    wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, "MacBook"), "MacBook"))
    assert pic.text == "MacBook"


def test_find_price(driver):
    driver.get(driver.url + "/MacBook")
    price = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li>h2")))
    assert price.text == "$602.00"


def test_add_button(driver):
    driver.get(driver.url + "/MacBook")
    assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "button-cart")))


def test_image(driver):
    driver.get(driver.url + "/MacBook")
    images = driver.find_elements(By.CSS_SELECTOR, ".image-additional")
    assert len(images) == 4


def test_review(driver):
    driver.get(driver.url + "/MacBook")
    driver.find_element(By.CSS_SELECTOR, "a[href='#tab-review']").click()
    button = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.ID, "button-review")))
    assert button.text == "Continue"
