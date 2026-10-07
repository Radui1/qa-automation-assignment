# Test Plan

## TC-01 Successful Single Bet Placement
**Priority:** Critical

**Risk Rationale:**  
Bet placement is the application's primary business flow. A failure here directly prevents users from using the core product functionality.

**Steps:**
1. Open the application with a valid user ID.
2. Select an upcoming football match.
3. Select the HOME outcome.
4. Verify the selected match appears in the bet slip.
5. Enter a valid stake of €10.00.
6. Verify the potential payout equals stake × odds.
7. Click Place Bet.
8. Verify the success receipt.

**Expected Result:**
- The selected match and odds are shown correctly in the bet slip.
- The stake is accepted.
- Potential payout is calculated correctly.
- The bet is placed successfully.
- The receipt contains the correct match, selection, stake, odds, payout, bet ID, and timestamp.


## TC-02 Reject Bet When Stake Exceeds Available Balance
**Priority:** Critical

**Risk Rationale:**  
Allowing a user to bet more than the available balance is a critical financial integrity risk and can result in invalid negative balances.

**Steps:**
1. Reset the user balance.
2. Retrieve the current balance.
3. Select a valid upcoming match.
4. Attempt to place a bet with a stake greater than the available balance.

**Expected Result:**
- The bet is rejected.
- The API returns the expected validation error.
- The balance remains unchanged.
- No bet is created.


## TC-03 Stake Boundary and Validation
**Priority:** High

**Risk Rationale:**  
Incorrect stake validation may allow invalid financial values or block valid user input.

**Steps:**
1. Select a valid match.
2. Enter a stake below the minimum.
3. Enter the minimum valid stake.
4. Enter the maximum valid stake.
5. Enter a stake above the maximum.
6. Enter a value with more than two decimal places.

**Expected Result:**
- Invalid stake values are rejected with clear feedback.
- Valid boundary values are accepted.
- Stake precision rules are enforced correctly.


## TC-04 Single Selection Replacement
**Priority:** High

**Risk Rationale:**  
The product supports only one active bet selection. Incorrect replacement behaviour could result in the wrong match being submitted.

**Steps:**
1. Select an outcome for one match.
2. Verify it appears in the bet slip.
3. Select an outcome for a different match.

**Expected Result:**
- The previous selection is replaced.
- Only the latest selected match remains active in the bet slip.
- Stake and payout information correspond to the active selection.


## TC-05 Odds Filter
**Priority:** Medium

**Risk Rationale:**  
Incorrect filtering may hide valid matches or display matches outside the user's selected criteria.

**Steps:**
1. Open the matches page.
2. Enter a minimum odds value.
3. Enter a maximum odds value.
4. Apply the filter.
5. Review the displayed matches.

**Expected Result:**
- Only matches with odds inside the inclusive selected range are displayed.
- Matches outside the range are excluded.
- Invalid ranges provide clear user feedback.


## TC-06 Date Filter
**Priority:** Medium

**Risk Rationale:**  
Users rely on date filtering to find relevant upcoming events. Incorrect inclusive boundaries may result in missing or unrelated matches.

**Steps:**
1. Open the matches page.
2. Select a single date and apply the filter.
3. Verify matches displayed for that date.
4. Select a date range.
5. Verify matches at both range boundaries.

**Expected Result:**
- Only matches within the selected date or inclusive date range are displayed.
- Boundary dates are included.
- Invalid date ranges show clear feedback.