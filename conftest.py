import time
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera", "safari", "MicrosoftEdge"])
    parser.addoption("--executor", default="localhost")
    parser.addoption("--driver_path")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--bversion", action="store", default="102.0")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    driver_path = request.config.getoption("--driver_path")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(f"===> Test {request.node.name} started at {time.asctime()}")

    if executor == "localhost":
        if browser == "chrome":
            chrome_service = ChromeService(driver_path)
            driver = ChromeDriver(service=chrome_service)

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
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser))

    driver.maximize_window()
    driver.implicitly_wait(5)

    def fin():
        driver.quit()
        logger.info(f"===> Test {request.node.name} finished at {time.asctime()}")

    request.addfinalizer(fin)
    return driver
