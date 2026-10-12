"""
End-to-end UI tests for the betting workflow.

The test uses match data retrieved through the API and verifies the critical
user journey from match selection through successful bet placement.
"""

def test_place_bet(matches_page, valid_match, funded_balance):
    """
    Verify the complete successful bet placement workflow.

    This scenario was selected because placing a bet is the application's
    primary user journey and combines match data, odds selection, bet slip
    behaviour, stake handling, payout calculation, and receipt validation.
    """
    stake = 10
    assert funded_balance >= stake

    home_odds = valid_match["odds"]["home"]
    expected_payout = round(stake * home_odds, 2)

    bet_slip = (
        matches_page
        .open()
        .wait_for_match(valid_match["id"])
        .select_home(valid_match["id"])
    )
    bet_slip.enter_stake(stake)

    assert bet_slip.has_bet_details(
        match=valid_match,
        stake=stake,
        payout=expected_payout
    )

    receipt = bet_slip.place_bet().capture_receipt()
    assert receipt.confirms_bet(
        match=valid_match,
        stake=stake,
        odds=home_odds
    )