"""
Shared Selenium helpers for page and component objects.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_WAIT_TIMEOUT = 10
Locator = tuple[str, str]


class BasePage:
    """Provide common waiting and interaction helpers."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self) -> WebDriverWait:
        return WebDriverWait(self.driver, DEFAULT_WAIT_TIMEOUT)

    def _visible(self, locator: Locator) -> WebElement:
        return self._wait().until(
            EC.visibility_of_element_located(locator)
        )

    def _clickable(self, locator: Locator) -> WebElement:
        return self._wait().until(
            EC.element_to_be_clickable(locator)
        )

    def _click(self, locator: Locator) -> None:
        self._clickable(locator).click()

    def _fill(self, locator: Locator, value: str) -> None:
        element = self._clickable(locator)
        element.clear()
        element.send_keys(value)

    def _text(self, locator: Locator) -> str:
        return self._visible(locator).text

    def _value(self, locator: Locator) -> str:
        return self._visible(locator).get_attribute("value")
