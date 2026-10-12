from typing import Any

import requests

from domain.betting import BetAttemptResult, MatchData, Selection, is_upcoming_match, normalize_amount
from config.settings import BASE_API_URL, USER_ID


class ApiClient:
    def __init__(self):
        self.base_url = BASE_API_URL
        self.session = requests.Session()
        self.session.headers.update({"x-user-id": USER_ID})

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    @staticmethod
    def _json(response: requests.Response) -> Any:
        response.raise_for_status()
        return response.json()

    def get_matches(self) -> list[MatchData]:
        response = self.session.get(self._url("/api/matches"))
        return self._json(response)

    def find_first_upcoming_match(self) -> MatchData:
        """Return the first match whose kickoff date is today or later."""
        for match in self.get_matches():
            if is_upcoming_match(match):
                return match

        raise LookupError("No upcoming match found")

    def current_balance(self):
        """Return the current balance for the test user."""
        response = self.session.get(self._url("/api/balance"))
        payload = self._json(response)
        return normalize_amount(payload["balance"])

    def reset_balance(self):
        """Reset the balance for the test user and return it."""
        response = self.session.post(self._url("/api/reset-balance"))
        self._json(response)
        return self.current_balance()

    def attempt_bet(self, match_id, selection, stake):
        """Attempt to place a bet through the API."""
        payload = {
            "matchId": match_id,
            "selection": selection.value,
            "stake": float(normalize_amount(stake))
        }

        response = self.session.post(
            self._url("/api/place-bet"),
            json=payload
        )
        result_payload = response.json() if response.content else None
        return BetAttemptResult(
            status_code=response.status_code,
            payload=result_payload
        )

    def attempt_home_bet(self, match, stake):
        """Attempt a home selection bet for the provided match."""
        return self.attempt_bet(
            match_id=match["id"],
            selection=Selection.HOME,
            stake=stake
        )