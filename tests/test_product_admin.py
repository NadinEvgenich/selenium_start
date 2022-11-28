import allure
from page_objects.AdminPageLogin import AdminPageLogin
from page_objects.AdminPage import AdminPage

name = "Canon EOS R10"
text = "A camera so versatile it can tackle virtually anything. It’s the ideal travel companion."
tag = "Canon EOS R10"
model = "R10"
price = "979.99"
quantity = "500"


@allure.title('Тест на создание продукта в админке')
def test_create_product(driver):
    admin_page = AdminPage(driver)
    admin_page._open('/admin')
    AdminPageLogin(driver).login("user", "bitnami")
    admin_page.go_to_page_products()
    admin_page.create_product(name, text, tag, model, price, quantity)
    admin_page.verify_product(name)


@allure.title('Тест на удаление товара из каталога в админке')
def test_delete_product(driver):
    admin_page = AdminPage(driver)
    admin_page._open('/admin')
    AdminPageLogin(driver).login("user", "bitnami")
    admin_page.go_to_page_products()
    admin_page.delete_product()
