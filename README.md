# Ezra UI Automation

UI test automation for the Ezra web app using Playwright, Pytest, and Page Object Model. Focuses on authentication flow validation.

## 📊 Test Reports

Latest test report available at: **[GitHub Pages Report](https://spajjuri-pro.github.io/ezra-assignment/report.html)**

Reports are automatically generated and deployed on every commit to `main`.

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

## Quick Start

```bash
git clone https://github.com/spajjuri-pro/ezra-assignment.git
cd ezra-assignment
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

## Extending Tests

- Add new page objects under `pages/`
- Add test data under `data/`
- Add new tests under `tests/`
- Reuse existing fixtures in `conftest.py`

## GitHub Workflows

Automated testing is triggered on every push to `main`:

1. Tests run on Ubuntu with Pygame and Chromium
2. HTML report is generated automatically
3. Report is deployed to GitHub Pages at [the link above](#-test-reports)

View workflow runs: [Actions](https://github.com/spajjuri-pro/ezra-assignment/actions)
