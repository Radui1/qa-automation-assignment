"""
End-to-end UI tests for the betting workflow.

The test uses match data retrieved through the API and verifies the critical
user journey from match selection through successful bet placement.
"""

from pages.matches_page import MatchesPage
from pages.success_bet_modal import SuccessBetModal


def test_place_bet(driver, valid_match):
    """
    Verify the complete successful bet placement workflow.

    This scenario was selected because placing a bet is the application's
    primary user journey and combines match data, odds selection, bet slip
    behaviour, stake handling, payout calculation, and receipt validation.
    """
    matches_page = MatchesPage(driver)

    matches_page.open()

    match_card = matches_page.get_match_card(valid_match["id"])
    assert match_card.is_displayed()

    matches_page.select_home(valid_match["id"])

    assert matches_page.is_bet_slip_selection_visible()

    bet_slip_text = matches_page.get_bet_slip_text()
    assert valid_match["homeTeam"] in bet_slip_text
    assert valid_match["awayTeam"] in bet_slip_text

    stake = 10
    matches_page.place_stake(stake)

    assert matches_page.get_stake_value() == str(stake)

    home_odds = valid_match["odds"]["home"]
    expected_payout = round(stake * home_odds, 2)

    actual_payout = matches_page.get_potential_payout()
    actual_payout_value = float(
        actual_payout.replace("€", "").strip()
    )

    assert actual_payout_value == expected_payout

    matches_page.place_bet()

    success_modal = SuccessBetModal(driver)

    receipt_match = success_modal.get_match()

    assert valid_match["homeTeam"] in receipt_match
    assert valid_match["awayTeam"] in receipt_match
    assert success_modal.get_title() == "Bet Placed Successfully!"
    assert success_modal.get_stake() == f"€{stake:.2f}"
    assert success_modal.get_payout() == f"€{expected_payout:.2f}"
    assert success_modal.get_bet_id() != ""