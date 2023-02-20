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
 
    logger = logging.getLogger('driver')
    test_name = request.node.name
    if "\\" in test_name:
        test_name = test_name.split("\\")[0]
    log_path = f"logs/{test_name}_{datetime.now().strftime('%d-%m-%Y_%H.%M.%S')}.log"
    logger.addHandler(logging.FileHandler(log_path))
    logger.setLevel(level=log_level)
    logger.info(f"{logger.name} ===> Test {test_name} started at {datetime.now()}")


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
    driver.test_name = test_name
    driver.log_path = log_path

    logger.info("Browser:{}".format(browser))

    driver.maximize_window()
    driver.implicitly_wait(5)

    def fin():
        driver.quit()
        logger.info(f"===> Test {test_name} finished at {datetime.now()}")

    request.addfinalizer(fin)
    return driver
