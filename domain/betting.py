"""
Shared bet-related value objects used by the UI and API layers.
"""

import re
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from typing import Any, Mapping


MatchData = Mapping[str, Any]
TWOPLACES = Decimal("0.01")
SUCCESS_TITLE = "Bet Placed Successfully!"
BET_VALIDATION_ERROR_STATUS = 422


class Selection(str, Enum):
    """Supported bet selections."""

    HOME = "HOME"
    DRAW = "DRAW"
    AWAY = "AWAY"


def normalize_amount(value: Decimal | int | float | str) -> Decimal:
    """Return a two-decimal amount for stable UI and API assertions."""
    return Decimal(str(value)).quantize(
        TWOPLACES,
        rounding=ROUND_HALF_UP
    )


def parse_amount(value: str) -> Decimal:
    """Extract a numeric amount from UI text."""
    numeric_value = re.sub(r"[^0-9.\-]", "", value)
    return normalize_amount(numeric_value)


def is_upcoming_match(match: MatchData) -> bool:
    """Return whether the match starts today or later."""
    kickoff_date = date.fromisoformat(str(match["kickoffDate"]))
    return kickoff_date >= date.today()


@dataclass(frozen=True)
class BetSummary:
    """User-visible bet information shared by the bet slip and receipt."""

    match_text: str
    stake_amount: Decimal
    payout_amount: Decimal

    def includes_match(self, match: MatchData) -> bool:
        return (
            str(match["homeTeam"]) in self.match_text
            and str(match["awayTeam"]) in self.match_text
        )

    def shows_stake(self, stake: Decimal | int | float | str) -> bool:
        return self.stake_amount == normalize_amount(stake)

    def shows_payout(self, payout: Decimal | int | float | str) -> bool:
        return self.payout_amount == normalize_amount(payout)

    def matches(
        self,
        match: MatchData,
        stake: Decimal | int | float | str,
        payout: Decimal | int | float | str
    ) -> bool:
        return (
            self.includes_match(match)
            and self.shows_stake(stake)
            and self.shows_payout(payout)
        )


@dataclass(frozen=True)
class BetReceipt:
    """Successful bet receipt details captured from the confirmation modal."""

    title: str
    summary: BetSummary
    odds: Decimal
    bet_id: str

    def has_bet_id(self) -> bool:
        return bool(self.bet_id.strip())

    def shows_odds(self, odds: Decimal | int | float | str) -> bool:
        return self.odds == normalize_amount(odds)

    def confirms_bet(
        self,
        match: MatchData,
        stake: Decimal | int | float | str,
        odds: Decimal | int | float | str
    ) -> bool:
        return (
            self.title == SUCCESS_TITLE
            and self.summary.includes_match(match)
            and self.summary.shows_stake(stake)
            and self.summary.payout_amount > Decimal("0.00")
            and self.shows_odds(odds)
            and self.has_bet_id()
        )


@dataclass(frozen=True)
class BetAttemptResult:
    """Outcome of a bet placement attempt through the API."""

    status_code: int
    payload: MatchData | None = None

    def is_rejected(self) -> bool:
        return self.status_code == BET_VALIDATION_ERROR_STATUS
