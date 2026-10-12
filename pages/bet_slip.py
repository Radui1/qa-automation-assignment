"""
Component object for the bet slip.
"""

from selenium.webdriver.common.by import By

from domain.betting import BetSummary, MatchData, parse_amount
from pages.base_page import BasePage
from pages.success_bet_modal import SuccessBetModal


class BetSlip(BasePage):
    """Encapsulate higher-level interactions with the bet slip."""

    CONTAINER = (By.ID, "bet-slip")
    SELECTION_CARD = (By.CSS_SELECTOR, "#bet-slip .card")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    POTENTIAL_PAYOUT = (By.ID, "bet-slip-potential-payout")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")

    def capture_summary(self) -> BetSummary:
        """Return the user-visible bet details shown in the slip."""
        return BetSummary(
            match_text=self._text(self.CONTAINER),
            stake_amount=parse_amount(self._value(self.STAKE_INPUT)),
            payout_amount=parse_amount(self._text(self.POTENTIAL_PAYOUT))
        )

    def enter_stake(self, amount: int | float | str) -> None:
        """Enter a stake into the bet slip."""
        self._fill(self.STAKE_INPUT, str(amount))

    def has_bet_details(
        self,
        match: MatchData,
        stake: int | float | str,
        payout: int | float | str
    ) -> bool:
        """Return whether the slip reflects the selected bet details."""
        self._visible(self.SELECTION_CARD)
        return self.capture_summary().matches(match, stake, payout)

    def place_bet(self) -> SuccessBetModal:
        """Submit the current bet and return the success modal component."""
        self._click(self.PLACE_BET_BUTTON)
        return SuccessBetModal(self.driver)
