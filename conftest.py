import os.path
import time
import pytest
import logging

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera", "safari", "MicrosoftEdge"])
    parser.addoption("--executor", default="localhost")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--bversion", action="store", default="102.0")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption('--executor')
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")

    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    logger.info(f"===> Test {request.node.name} started at {time.asctime()}")
    
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
