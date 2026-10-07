"""
Shared pytest fixtures for UI and API tests.
"""

from datetime import date

import pytest
from selenium import webdriver

from api.api_client import ApiClient


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
def valid_match(api_client):
    """Return the first match whose kickoff date is today or later."""
    matches = api_client.get_matches()

    for match in matches:
        match_date = date.fromisoformat(match["kickoffDate"])

        if match_date >= date.today():
            return match

    pytest.fail("No upcoming match found")