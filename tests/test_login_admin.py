import allure
from page_objects.AdminPageLogin import AdminPageLogin
from helpers import admin_url


@allure.title('Проверка, что данная страница является авторизацией в админку')
def test_admin(driver):
    AdminPageLogin(driver)._open(admin_url)
    AdminPageLogin(driver).verify_page("Administration")


@allure.title('Проверка на наличие ссылки главной страницы')
def test_find_opencart(driver):
    AdminPageLogin(driver)._open(admin_url)
    AdminPageLogin(driver).get_opencart_link()


@allure.title('Проверка на наличие ссылки для логина')
def test_find_login(driver):
    AdminPageLogin(driver)._open(admin_url)
    AdminPageLogin(driver).verify_login_link()


@allure.title('Появление формы для восстановления пароля')
def test_forgotten(driver):
    admin_page_login = AdminPageLogin(driver)
    admin_page_login._open(admin_url)
    admin_page_login.click_forgotten_password()
    admin_page_login.verify_page("Forgot Your Password?")


@allure.title('Проверка авторизации в админку')
def test_login(driver):
    admin_page_login = AdminPageLogin(driver)
    admin_page_login._open(admin_url)
    admin_page_login.login("user", "bitnami")
    admin_page_login.verify_page("Dashboard")
