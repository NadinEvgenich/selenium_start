import os
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


logging.basicConfig(filename="selenium.log",
                    format='%(asctime)s:%(levelname)s:%(name)s - %(message)s',
                    encoding='utf-8',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.INFO
                    )


class Listener(AbstractEventListener):
    logger = logging.getLogger('ListenerLoger')


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera", "safari", "MicrosoftEdge"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", default="localhost")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--bversion", action="store", default="110.0")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption('--executor')
    logs = request.config.getoption("--logs")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    url = request.config.getoption("--url")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    if executor == "localhost":
        if browser == "chrome":
          options = ChromeOptions()
          options.headless = headless
          driver = webdriver.Chrome(options=options, ChromeDriverManager().install())  
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc
            },
            "name": "Capricornio"
        }

        driver = EventFiringWebDriver(webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url
        ), Listener())

        logger.info("Test {} started with {} {}".format(test_name, browser, version))

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.url = url

    def fin():
        driver.quit()
        logger.info("Browser {} closed".format(browser))
        logger.info("Test {} finished".format(test_name))

    request.addfinalizer(fin)
    return driver
