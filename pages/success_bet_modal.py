"""
Component object for the successful bet receipt modal.
"""

from selenium.webdriver.common.by import By

from domain.betting import BetReceipt, BetSummary, parse_amount
from pages.base_page import BasePage


class SuccessBetModal(BasePage):
    """Encapsulate the successful bet receipt."""

    TITLE = (By.CSS_SELECTOR, ".modalBody .modalTitle")
    STAKE = (By.ID, "modal-success-stake")
    PAYOUT = (By.ID, "modal-success-payout")
    BET_ID = (By.ID, "modal-success-bet-id")
    MATCH = (By.ID, "modal-success-match")
    ODDS = (By.ID, "modal-success-odds")

    def capture_receipt(self) -> BetReceipt:
        """Return the visible receipt as a domain value object."""
        return BetReceipt(
            title=self._text(self.TITLE),
            summary=BetSummary(
                match_text=self._text(self.MATCH),
                stake_amount=parse_amount(self._text(self.STAKE)),
                payout_amount=parse_amount(self._text(self.PAYOUT)),
            ),
            odds=parse_amount(self._text(self.ODDS)),
            bet_id=self._text(self.BET_ID),
        )