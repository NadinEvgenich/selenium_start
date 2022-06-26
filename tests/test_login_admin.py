from page_objects.AdminPageLogin import AdminPageLogin

path = "/admin"


def test_admin(driver):
    driver.open(path)
    AdminPageLogin(driver).verify_page("Administration")


def test_find_opencart(driver):
    driver.open(path)
    AdminPageLogin(driver).get_opencart_link()


def test_find_login(driver):
    driver.open(path)
    AdminPageLogin(driver).verify_login_link()


def test_forgotten(driver):
    driver.open(path)
    admin_page_login = AdminPageLogin(driver)
    admin_page_login.click_forgotten_password()
    admin_page_login.verify_page("Forgot Your Password?")


def test_login(driver):
    driver.open(path)
    admin_page_login = AdminPageLogin(driver)
    admin_page_login.login("user", "bitnami")
    admin_page_login.verify_page("Dashboard")
