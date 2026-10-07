"""
API tests for betting business rules.
"""


def test_bet_is_rejected_when_stake_exceeds_balance(api_client, valid_match):
    """
    Verify that a bet is rejected when the stake exceeds the available balance.

    This scenario was selected because insufficient balance is a critical
    financial business rule and must be enforced by the backend.
    """
    api_client.reset_balance()

    balance_response = api_client.get_balance()
    initial_balance = balance_response["balance"]

    stake = initial_balance + 10

    response = api_client.place_bet(
        match_id=valid_match["id"],
        selection="HOME",
        stake=stake
    )

    assert response.status_code == 422

    balance_after_response = api_client.get_balance()
    balance_after = balance_after_response["balance"]

    assert balance_after == initial_balance