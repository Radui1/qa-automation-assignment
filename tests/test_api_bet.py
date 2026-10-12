"""
API tests for betting business rules.
"""


def test_bet_is_rejected_when_stake_exceeds_balance(
    api_client,
    valid_match,
    funded_balance
):
    """
    Verify that a bet is rejected when the stake exceeds the available balance.

    This scenario was selected because insufficient balance is a critical
    financial business rule and must be enforced by the backend.
    """
    stake = funded_balance + 10

    rejected_bet = api_client.attempt_home_bet(valid_match, stake)

    assert rejected_bet.is_rejected()
    assert api_client.current_balance() == funded_balance