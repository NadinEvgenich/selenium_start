from page_objects.AdminPageLogin import AdminPageLogin
from page_objects.AdminPage import AdminPage

path = "/admin"

name = "Canon EOS R10"
text = "A camera so versatile it can tackle virtually anything. It’s the ideal travel companion."
tag = "Canon EOS R10"
model = "R10"
price = "979.99"
quantity = "500"


def test_create_product(driver):
    driver.open(path)
    admin_page = AdminPage(driver)
    AdminPageLogin(driver).login("user", "bitnami")
    admin_page.go_to_product()
    admin_page.create_product(name, text, tag, model, price, quantity)
    admin_page.verify_product(name)


def test_delete_product(driver):
    driver.open(path)
    admin_page = AdminPage(driver)
    AdminPageLogin(driver).login("user", "bitnami")
    admin_page.go_to_product()
    admin_page.verify_product(name)
    admin_page.delete_product()
    admin_page.verify_product(name)
