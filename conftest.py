"""Shared pytest fixtures for UI and API tests."""

import pytest
from selenium import webdriver

from api.api_client import ApiClient
from pages.matches_page import MatchesPage


@pytest.fixture
def driver():
    """Provide a Chrome WebDriver instance and close it after the test."""
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def api_client():
    """Provide an API client for backend interactions."""
    return ApiClient()


@pytest.fixture
def matches_page(driver):
    """Provide the Matches page object for UI interactions."""
    return MatchesPage(driver)


@pytest.fixture
def funded_balance(api_client):
    """Reset the test user's balance and return the available amount."""
    return api_client.reset_balance()


@pytest.fixture
def valid_match(api_client):
    """Return the first match whose kickoff date is today or later."""
    try:
        return api_client.find_first_upcoming_match()
    except LookupError as exc:
        pytest.fail(str(exc))