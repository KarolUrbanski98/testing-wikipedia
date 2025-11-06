import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WikiPage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 15)
        self._logger = logging.getLogger()

    def find(self, locator):
        return self._driver.find_element(*locator)

    def wait(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
