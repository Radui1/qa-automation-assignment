"""
Page object for the Matches page and bet slip interactions.
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.bet_slip import BetSlip
from config.settings import BASE_URL


class MatchesPage(BasePage):
    """Encapsulates user interactions with matches and the bet slip."""

    @staticmethod
    def _match_card_locator(match_id):
        return (By.ID, f"match-card-{match_id}")

    @staticmethod
    def _home_odds_locator(match_id):
        return (By.ID, f"odds-{match_id}-home")

    def open(self):
        """Open the Matches page."""
        self.driver.get(BASE_URL)
        return self

    def wait_for_match(self, match_id):
        """Wait for the requested match card to be visible."""
        self._visible(self._match_card_locator(match_id))
        return self

    def select_home(self, match_id):
        """Select the home odds for the given match and return the bet slip."""
        self._click(self._home_odds_locator(match_id))
        return BetSlip(self.driver)
