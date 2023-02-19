import os.path
import time
import pytest
import logging

from selenium import webdriver


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
    parser.addoption("--executor", default="localhost")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", default=True)
    parser.addoption("--bversion", action="store", default="102.0")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption('--executor')
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    test_name = request.node.name


    if executor == "localhost":
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Загрузки/Drivers/chromedriver"))

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

        driver = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url
        ), Listener())
  

    logger.info("Test {} started with {} {}".format(test_name, browser, version))

    driver.maximize_window()
    driver.implicitly_wait(5)

    def fin():
        driver.quit()
         logger.info("Browser {} closed".format(browser))
         logger.info("Test {} finished".format(test_name))

    request.addfinalizer(fin)
    return driver
