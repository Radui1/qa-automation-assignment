# QA Automation Assignment

Small automation framework built for the QA Engineer home assignment.

The project contains:
- One end-to-end UI test for the critical bet placement journey
- One API test for a critical betting business rule
- Shared pytest fixtures
- Page/component objects for UI interactions
- API client utilities
- Environment-based configuration

## Tech Stack

- Python 3
- Selenium WebDriver
- Pytest
- Requests
- python-dotenv
- Google Chrome

## Project Structure

```text
selenium_python/
├── api/
│   ├── __init__.py
│   └── api_client.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── pages/
│   ├── __init__.py
│   ├── matches_page.py
│   └── success_bet_modal.py
│
├── tests/
│   ├── __init__.py
│   ├── test_place_bet.py
│   └── test_api_bet.py
│
├── conftest.py
├── .env
├── .gitignore
├── requirements.txt
├── test_plan.md
├── execution_results.md
├── strategy.md
└── README.md