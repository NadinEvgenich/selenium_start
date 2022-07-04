import os
import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.68:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Загрузки/Drivers"))


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=drivers + "/chromedriver")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=drivers + "/geckodriver")
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=drivers + "/operadriver")
    elif browser_name == "yandex":
        browser = webdriver.Chrome(executable_path=drivers + "/yandexdriver")
    else:
        raise ValueError("Browser not supported!")

    request.addfinalizer(browser.close)

    def open(path=""):
        return browser.get(url + path)

    browser.maximize_window()
    browser.implicitly_wait(5)

    browser.open = open
    browser.open()

    return browser
