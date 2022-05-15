from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.register import PageRegisterAccount
from faker import Faker

f = Faker()
first_name = f.first_name()
last_name = f.last_name()
email = f.email()
phone = f.phone_number()
password = f.password()


def test_register(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    assert WebDriverWait(driver, 1).until(EC.title_is("Register Account"))


def test_find_login(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    wait = WebDriverWait(driver, 2)
    login = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.LOGIN_LINK))
    login.click()
    assert wait.until(EC.title_is("Account Login"))


def test_radiobutton(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    button = driver.find_elements(*PageRegisterAccount.RADIOBUTTON)
    assert len(button) == 2


def test_checkbox(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator=PageRegisterAccount.CHECKBOX))


def test_registration(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    wait = WebDriverWait(driver, 4)
    firstname = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.FIRSTNAME_INPUT))
    firstname.send_keys(first_name)
    lastname = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.LASTNAME_INPUT))
    lastname.send_keys(last_name)
    e_mail = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.EMAIL_INPUT))
    e_mail.send_keys(email)
    telephone = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.TELEPHONE_INPUT))
    telephone.send_keys(phone)
    word = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.PASSWORD_INPUT))
    word1 = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.CONFIRM_INPUT))
    word.send_keys(password)
    word1.send_keys(password)
    box = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.CHECKBOX))
    box.click()
    button = wait.until(EC.visibility_of_element_located(locator=PageRegisterAccount.CONTINUE_BUTTON))
    button.click()
    assert wait.until(EC.title_is("Your Account Has Been Created!"))
