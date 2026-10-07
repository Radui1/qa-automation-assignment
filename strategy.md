# Automation Strategy and Recommendations

## Why These Two Tests Were Selected

The assignment asks for only two automated tests, so I selected scenarios that cover the highest business risk and provide the most value across different test layers.

### 1. End-to-End UI Bet Placement

The UI test covers the application's primary user journey:

- Select an upcoming match
- Select an outcome
- Verify the bet slip
- Enter a valid stake
- Validate the potential payout
- Place the bet
- Validate the success receipt

This scenario was selected because it exercises the main customer flow across several important components and verifies that data remains consistent from selection through final receipt.

It also validates integration between match data, the betting UI, stake handling, payout calculation, and the final receipt.

### 2. API Insufficient Balance Validation

The API test verifies that a bet cannot be placed when the requested stake exceeds the user's available balance.

This scenario was selected because it represents a critical financial business rule that should be enforced by the backend independently of UI validation.

The test verifies both:

- The expected validation response
- That the user's balance remains unchanged after the rejected request

This provides stronger coverage than checking only the HTTP response code and helps detect unintended backend side effects.

## What Was Intentionally Left Manual

Several scenarios were intentionally kept as manual tests because the assignment limits automation to two high-value scenarios.

### Stake Boundary Validation

Minimum stake, maximum stake, decimal precision, empty values, and invalid values are important validation cases.

These would be good candidates for parameterized API or UI automation in a larger suite, but automating all stake combinations would add volume without providing more value than the selected business-rule test within the scope of this assignment.

### Date and Odds Filtering

Date and odds filters were kept manual because they contain several combinations and boundary conditions that can be explored efficiently during focused manual testing.

If the application were to scale, these would be good candidates for lower-level API or component tests rather than relying mainly on UI automation.

### Single Selection Replacement

The behaviour where selecting a new match replaces the previous active selection was kept manual.

It is an important interaction rule, but its business impact is lower than successful bet placement and insufficient balance validation.

### Error Modal and Retry Behaviour

Failure handling, Rebet, Close, and modal state transitions were left manual for this assignment.

Automating these flows reliably would require a deterministic way to force the backend into an error state. Without controlled failure setup, the test could become flaky or dependent on unpredictable backend behaviour.

In a larger test environment, I would use controlled test data, mocks, or dedicated test hooks to trigger these failure scenarios consistently.

## Recommendations for Scaling

### 1. Introduce CI/CD Automation

The automated suite should run as part of the delivery pipeline.

A practical approach would be:

- Run API and fast validation tests on every pull request
- Run the critical UI smoke flow on every deployment to a test environment
- Run a broader regression suite on scheduled or release-triggered pipelines
- Publish test results and failure evidence automatically

This would provide faster feedback while avoiding unnecessary execution of slower UI tests.

### 2. Expand Lower-Level Test Coverage

Business rules should primarily be covered through API or component-level tests where possible.

Examples include:

- Stake minimum and maximum
- Decimal precision
- Invalid selections
- Invalid or missing match IDs
- Insufficient balance
- Currency validation
- Payout calculation

UI automation should remain focused on critical user journeys and integration behaviour rather than duplicating every validation rule through the browser.

### 3. Improve Test Data and State Management

The current tests use API calls to retrieve valid match data and reset the user balance.

If the project grows, test data management should become more deterministic.

Recommended improvements include:

- Dedicated test users
- Controlled balance setup
- Predictable test matches
- Environment cleanup after tests
- Clearly defined test data ownership and lifecycle

This would reduce dependency on changing production-like data and improve test repeatability.

## Specification Clarifications

The specification should be clarified before expanding automated boundary coverage.

One identified inconsistency is the minimum stake requirement:

- The business rules define the minimum stake as €1.00
- The validation section defines the minimum stake as €1.01

A single source of truth should be agreed before automating this boundary.

Additional clarification should also ensure that UI and API behaviour remain aligned for:

- Currency
- Balance enforcement
- Match availability
- Receipt data consistency
- Home and away team ordering

## Summary

The automation strategy intentionally prioritizes risk over test quantity.

The UI test protects the primary customer journey, while the API test protects a critical financial rule at the backend layer.

If the project were to scale, I would increase lower-level API and component coverage, keep UI automation focused on critical workflows, introduce automated execution in CI/CD, and strengthen test data management.