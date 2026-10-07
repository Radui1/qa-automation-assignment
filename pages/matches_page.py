"""
Page object for the Matches page and bet slip interactions.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BASE_URL


DEFAULT_WAIT_TIMEOUT = 10


class MatchesPage:
    """Encapsulates user interactions with matches and the bet slip."""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the Matches page."""
        self.driver.get(BASE_URL)

    def get_match_card(self, match_id):
        """Return the visible match card for the given match ID."""
        return WebDriverWait(self.driver, DEFAULT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(
                (By.ID, f"match-card-{match_id}")
            )
        )

    def select_home(self, match_id):
        """Select the home odds for the given match."""
        home_button = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.element_to_be_clickable(
                (By.ID, f"odds-{match_id}-home")
            )
        )

        home_button.click()

    def is_bet_slip_selection_visible(self):
        """Return whether a selection is visible in the bet slip."""
        selection_card = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#bet-slip .card")
            )
        )

        return selection_card.is_displayed()

    def get_bet_slip_text(self):
        """Return the visible text from the bet slip."""
        bet_slip = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "bet-slip")
            )
        )

        return bet_slip.text

    def place_stake(self, amount):
        """Enter the given stake amount in the bet slip."""
        stake_input = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.element_to_be_clickable(
                (By.ID, "bet-slip-stake-input")
            )
        )

        stake_input.clear()
        stake_input.send_keys(str(amount))

    def get_stake_value(self):
        """Return the current stake input value."""
        stake_input = self.driver.find_element(
            By.ID,
            "bet-slip-stake-input"
        )

        return stake_input.get_attribute("value")

    def get_potential_payout(self):
        """Return the potential payout displayed in the bet slip."""
        payout = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "bet-slip-potential-payout")
            )
        )

        return payout.text

    def place_bet(self):
        """Click the Place Bet button."""
        place_bet_button = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.element_to_be_clickable(
                (By.ID, "bet-slip-place-bet")
            )
        )
        place_bet_button.click()

