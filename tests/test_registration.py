from page_objects.UserRegistrationForm import UserRegistrationForm
from faker import Faker

path = "/index.php?route=account/register"

f = Faker()
first_name = f.first_name()
last_name = f.last_name()
email = f.email()
phone = f.phone_number()
password = f.password()


def test_register(driver):
    driver.open(path)
    UserRegistrationForm(driver).verify_page("Register Account")


def test_find_login(driver):
    driver.open(path)
    user_reg_form = UserRegistrationForm(driver)
    user_reg_form.click_login()
    user_reg_form.verify_page("Account Login")


def test_radiobutton(driver):
    driver.open(path)
    button = UserRegistrationForm(driver).get_radiobutton()
    assert len(button) == 2


def test_checkbox(driver):
    driver.open(path)
    UserRegistrationForm(driver).verify_checkbox()


def test_registration(driver):
    driver.open(path)
    user_reg_form = UserRegistrationForm(driver)
    user_reg_form.registration(first_name, last_name, email, phone, password)
    user_reg_form.verify_page("Your Account Has Been Created!")
