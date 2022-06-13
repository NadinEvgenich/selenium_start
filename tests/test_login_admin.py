from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.login import PageAdminLogin


def test_admin(driver):
    driver.get(driver.url + "/admin")
    assert WebDriverWait(driver, 1).until(EC.title_is("Administration"))


def test_find_opencart(driver):
    driver.get(driver.url + "/admin")
    op_link = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator=PageAdminLogin.OPENCART_LINK))
    assert op_link.text == "OpenCart"


def test_find_login(driver):
    driver.get(driver.url + "/admin")
    assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator=PageAdminLogin.ADMIN_LINK))


def test_forgotten(driver):
    driver.get(driver.url + "/admin")
    wait = WebDriverWait(driver, 2)
    forgotten_pas = wait.until(EC.visibility_of_element_located(locator=PageAdminLogin.FORGOTTEN_PASSWORD))
    forgotten_pas.click()
    assert wait.until(EC.title_is("Forgot Your Password?"))


def test_login(driver):
    driver.get(driver.url + "/admin")
    wait = WebDriverWait(driver, 4)
    username = wait.until(EC.visibility_of_element_located(locator=PageAdminLogin.USERNAME_INPUT))
    username.send_keys('user')
    password = wait.until(EC.visibility_of_element_located(locator=PageAdminLogin.PASSWORD_INPUT))
    password.send_keys('bitnami')
    button = wait.until(EC.visibility_of_element_located(locator=PageAdminLogin.SUBMIT_BUTTON))
    button.click()
    assert wait.until(EC.title_is("Dashboard"))
