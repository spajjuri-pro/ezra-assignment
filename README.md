# Ezra UI Automation

UI test automation for the Ezra web app using:
- Playwright (browser automation)
- Pytest (test runner)
- Page Object Model (maintainable test structure)

This repository currently focuses on authentication flow checks (login page rendering, signup navigation, and invalid email validation).

## How to get this repository

Option 1: Clone with Git (recommended)

```bash
git clone https://github.com/spajjuri-pro/ezra-assignment.git
cd ezra-assignment
```

Option 2: Download ZIP from GitHub

1. Open the repository page on GitHub.
2. Select **Code**.
3. Select **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted folder in VS Code.

## Who this is for

Use this repo if you want to:
- run automated UI checks against Ezra environments
- validate core auth behavior quickly
- extend test coverage using the existing POM framework

## Project structure

```text
.
├── conftest.py                    # Pytest fixtures and CLI options
├── pytest.ini                     # Pytest configuration and markers
├── requirements.txt               # Python dependencies
├── data/
│   └── test_data.py               # Test data/constants
├── pages/
│   ├── base_page.py               # Shared page actions
│   └── ezra_auth_page.py          # Auth page object
├── tests/
│   └── test_authentication_ezra.py
└── artifacts/                     # Generated test reports
```

## Prerequisites

- Python 3.10+
- pip
- macOS/Linux shell (commands below use bash)

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

## Run tests

Run all tests:

```bash
pytest
```

Run against a specific environment:

```bash
pytest --env staging
pytest --env qa
pytest --env prod
```

Run with a custom base URL (overrides --env):

```bash
pytest --base-url "https://custom-host.example.com/"
```

Run by marker:

```bash
pytest -m smoke
pytest -m regression
```

## HTML report

Generate a self-contained HTML report:

```bash
mkdir -p artifacts
pytest -v --html=artifacts/report.html --self-contained-html
```

Open the generated report:

```bash
open artifacts/report.html
```

## Common issues

- Browser not installed:
   - Run `python -m playwright install`
- Virtual environment not active:
   - Re-run `source .venv/bin/activate`
- Dependency errors:
   - Re-run `pip install -r requirements.txt`

## Extending this suite

- Add new page objects under `pages/`
- Add test data under `data/`
- Add new tests under `tests/`
- Reuse existing fixtures in `conftest.py`

## Scalability and future implementations

- Expand coverage to booking flows, including scan selection and pricing checks.
- Add medical questionnaire and downstream checkout validations.
- Add payment and confirmation coverage for end-to-end critical user paths.
- Introduce environment-specific secrets and credential management.
- Add CI pipelines (smoke on pull requests, regression on schedule).
- Enable richer observability with traces, videos, and improved reporting artifacts.
- Add retry strategy and stable test data factories to reduce flakiness.

## Notes

- Default test target is configured via CLI options in `conftest.py`.
- Browser settings are configured in the test framework setup.
