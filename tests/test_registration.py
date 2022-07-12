import allure
from page_objects.UserRegistrationForm import UserRegistrationForm
from faker import Faker

url = "http://192.168.1.68:8081/index.php?route=account/register"

f = Faker()
first_name = f.first_name()
last_name = f.last_name()
email = f.email()
phone = f.phone_number()
password = f.password()


@allure.title('Проверка, что данная страница является регистрацией нового пользователя')
def test_register(driver):
    UserRegistrationForm(driver)._open(url)
    UserRegistrationForm(driver).verify_page("Register Account")


@allure.title('Появление формы для авторизации пользователя')
def test_find_login(driver):
    user_reg_form = UserRegistrationForm(driver)
    user_reg_form._open(url)
    user_reg_form.click_login()
    user_reg_form.verify_page("Account Login")


@allure.title('Проверка количества радиобатонов')
def test_radiobutton(driver):
    UserRegistrationForm(driver)._open(url)
    button = UserRegistrationForm(driver).get_radiobutton()
    assert len(button) == 2


@allure.title('Проверка на наличие чекбокса')
def test_checkbox(driver):
    UserRegistrationForm(driver)._open(url)
    UserRegistrationForm(driver).verify_checkbox()


@allure.title('Проверка регисчтрации нового пользователя')
def test_registration(driver):
    user_reg_form = UserRegistrationForm(driver)
    user_reg_form._open(url)
    user_reg_form.registration(first_name, last_name, email, phone, password)
    user_reg_form.verify_page("Your Account Has Been Created!")
