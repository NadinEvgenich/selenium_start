from page_objects.elements.Catalog import Catalog


def test_find_desktops(driver):
    Catalog(driver).get_desktops()


def test_find_monitor(driver):
    catalog = Catalog(driver)
    catalog.click_components()
    catalog.click_monitors()


def test_find_show_all(driver):
    catalog = Catalog(driver)
    catalog.click_laptops()
    button1 = catalog.get_show_all()
    assert button1.text == "Show All Laptops & Notebooks"


def test_find_phones(driver):
    Catalog(driver).verify_get_phone()


def test_find_cameras(driver):
    Catalog(driver).verify_get_cameras()
