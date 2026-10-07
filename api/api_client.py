import requests

from config.settings import BASE_API_URL, USER_ID

class ApiClient:
    def __init__(self):
        self.base_url = BASE_API_URL
        self.headers = {
            "x-user-id": USER_ID
        }

    def get_matches(self):
        response = requests.get(
            f"{self.base_url}/api/matches",
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()

    def get_balance(self):
        """Return the current balance for the test user."""
        response = requests.get(
            f"{self.base_url}/api/balance",
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()

    def reset_balance(self):
        """Reset the balance for the test user."""
        response = requests.post(
            f"{self.base_url}/api/reset-balance",
            headers=self.headers
        )

        response.raise_for_status()
        return response.json()

    def place_bet(self, match_id, selection, stake):
        """Place a bet through the API."""
        payload = {
            "matchId": match_id,
            "selection": selection,
            "stake": stake
        }

        return requests.post(
            f"{self.base_url}/api/place-bet",
            headers=self.headers,
            json=payload
        )