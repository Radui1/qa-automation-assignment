"""
Component object for the successful bet receipt modal.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DEFAULT_WAIT_TIMEOUT = 10


class SuccessBetModal:
    """Encapsulates data displayed in the successful bet modal."""

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        """Return the title displayed in the success modal."""
        title = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".modalBody .modalTitle")
            )
        )

        return title.text

    def get_stake(self):
        """Return the stake displayed in the receipt."""
        stake = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "modal-success-stake")
            )
        )

        return stake.text

    def get_payout(self):
        """Return the potential payout displayed in the receipt."""
        payout = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "modal-success-payout")
            )
        )

        return payout.text

    def get_bet_id(self):
        """Return the bet ID displayed in the receipt."""
        bet_id = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "modal-success-bet-id")
            )
        )

        return bet_id.text

    def get_match(self):
        """Return the match information displayed in the receipt."""
        match = WebDriverWait(
            self.driver,
            DEFAULT_WAIT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "modal-success-match")
            )
        )

        return match.text
