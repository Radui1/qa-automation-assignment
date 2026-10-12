"""
Component object for the successful bet receipt modal.
"""

from selenium.webdriver.common.by import By

from domain.betting import BetReceipt, BetSummary, parse_amount
from pages.base_page import BasePage


class SuccessBetModal(BasePage):
    """Encapsulates data displayed in the successful bet modal."""

    TITLE = (By.CSS_SELECTOR, ".modalBody .modalTitle")
    STAKE = (By.ID, "modal-success-stake")
    PAYOUT = (By.ID, "modal-success-payout")
    BET_ID = (By.ID, "modal-success-bet-id")
    MATCH = (By.ID, "modal-success-match")
    ODDS = (By.ID, "modal-success-odds")

    def get_title(self):
        """Return the title displayed in the success modal."""
        return self._text(self.TITLE)

    def get_stake(self):
        """Return the stake displayed in the receipt."""
        return self._text(self.STAKE)

    def get_payout(self):
        """Return the potential payout displayed in the receipt."""
        return self._text(self.PAYOUT)

    def get_bet_id(self):
        """Return the bet ID displayed in the receipt."""
        return self._text(self.BET_ID)

    def get_match(self):
        """Return the match information displayed in the receipt."""
        return self._text(self.MATCH)

    def get_odds(self):
        """Return the odds displayed in the receipt."""
        return self._text(self.ODDS)

    def capture_receipt(self) -> BetReceipt:
        """Return the visible receipt details as a value object."""
        return BetReceipt(
            title=self.get_title(),
            summary=BetSummary(
                match_text=self.get_match(),
                stake_amount=parse_amount(self.get_stake()),
                payout_amount=parse_amount(self.get_payout())
            ),
            odds=parse_amount(self.get_odds()),
            bet_id=self.get_bet_id()
        )
