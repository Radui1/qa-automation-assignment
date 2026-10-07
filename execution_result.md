# Execution Results and Defect Reports

## Executed Scenarios

The highest-priority scenarios were executed against the application, together with additional exploratory checks around bet placement, balance handling, payout calculation, match availability, and API responses.

The following defects were identified.

---

## BUG-01 - Success receipt displays incorrect potential payout

**Severity:** High

**Reproduction Steps:**
1. Open the application with a valid user.
2. Select an upcoming match.
3. Select the HOME outcome.
4. Enter a stake of €10.00.
5. Verify the potential payout shown in the bet slip.
6. Place the bet.
7. Compare the payout displayed in the success receipt with the payout shown before placement.

**Expected Result:**
The potential payout in the success receipt should match the value calculated before placement using:

`stake × odds`

Example:

`€10.00 × 1.95 = €19.50`

The success receipt should therefore display `€19.50`.

**Actual Result:**
The bet slip correctly displays `€19.50`, but the success receipt displays `€20.00`.

**Business Impact:**
The user receives inconsistent financial information after placing a bet. This can reduce trust in payout calculations and may misrepresent the expected return.

**Evidence:**
Observed during automated UI execution. The automated assertion fails because the receipt payout differs from the expected payout.

---

## BUG-02 - API returns incorrect currency

**Severity:** High

**Reproduction Steps:**
1. Send a request to a betting API endpoint using a valid user context.
2. Inspect the returned response payload.
3. Check the value of the `currency` field.

**Expected Result:**
The currency should be returned as `EUR`.

**Actual Result:**
The API returns `USD`.

**Business Impact:**
Incorrect currency information can result in misleading financial data and inconsistent behaviour between the UI and backend.

**Evidence:**
Observed directly in API responses during exploratory testing.

---

## BUG-03 - Balance is not correctly enforced or refreshed after bet placement

**Severity:** Critical

**Reproduction Steps:**
1. Open the application with a valid user.
2. Note the current balance displayed in the UI.
3. Place a valid bet.
4. Close the success receipt.
5. Observe the balance displayed in the UI without refreshing the page.
6. Place additional bets until the total stake exceeds the actual available balance.
7. Check the resulting balance through the UI and/or API.

**Expected Result:**
- The UI balance should update immediately after each successful bet.
- The backend should reject any bet whose stake exceeds the user's current available balance.
- The user's balance should never become negative.

**Actual Result:**
- The UI continues to display the previous balance after a successful bet until the page is refreshed.
- Additional bets can still be placed based on the stale balance shown in the UI.
- The backend accepts bets even when the available balance is insufficient.
- The user's balance can become negative.

**Business Impact:**
This is a critical financial integrity issue. Users can place bets using funds they do not actually have, while the UI presents an incorrect available balance.

**Evidence:**
Observed during repeated manual bet placement and confirmed through API balance responses showing a negative balance.

## BUG-04 - Past matches are available although only upcoming matches should be offered

**Severity:** High

**Reproduction Steps:**
1. Open the application or retrieve the available matches through the API.
2. Review the kickoff dates of returned matches.
3. Compare the kickoff dates with the current date.

**Expected Result:**
Only upcoming matches should be available for betting.

**Actual Result:**
Matches with kickoff dates in the past are returned and/or displayed.

**Business Impact:**
Users may be presented with events that are no longer valid for pre-match betting, creating invalid betting opportunities and inconsistent product behaviour.

**Evidence:**
Observed in the match data returned by the application/API.

---

## BUG-05 - Home and away team order is reversed in the success receipt

**Severity:** High

**Reproduction Steps:**
1. Select a match where the API identifies:
   - Home team: Dortmund
   - Away team: Frankfurt
2. Place a bet on the match.
3. Open the success receipt.
4. Compare the displayed match order with the original match information.

**Expected Result:**
The success receipt should preserve the match order:

`Dortmund vs Frankfurt`

**Actual Result:**
The success receipt displays:

`Frankfurt vs Dortmund`

**Business Impact:**
The receipt can misrepresent the event on which the user placed the bet. This is especially risky because home and away outcomes have different meanings and odds.

**Evidence:**
Observed in the success receipt after placing the bet.

---
## BUG-06 - Odds filter accepts an invalid range where minimum exceeds maximum

**Severity:** Medium

**Reproduction Steps:**
1. Open the Odds Range filter.
2. Set MIN to `6.00`.
3. Set MAX to `2.00`.
4. Click Apply.

**Expected Result:**
The filter should reject the invalid range and display clear validation feedback indicating that the minimum odds cannot exceed the maximum odds.

**Actual Result:**
The application allows the invalid range to be applied without clear validation feedback.

**Business Impact:**
Users can configure an invalid filter state, which may produce confusing or incorrect match results and reduces confidence in filtering behaviour.

**Evidence:**
Odds filter configured with MIN `6.00` and MAX `2.00`.

## Additional Observation - Stake minimum specification inconsistency

This is not recorded as an application defect because the specification itself contains conflicting requirements.

One section defines the minimum stake as:

`€1.00`

while the validation rules define the minimum stake as:

`€1.01`

This should be clarified before finalising automated boundary coverage.