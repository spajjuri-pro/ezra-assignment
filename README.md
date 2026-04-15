# Ezra Healthcare UI Automation (Playwright + Pytest + POM)

This project automates critical healthcare web scenarios for Ezra web environments:
- Default environment: `staging` (`https://myezra-staging.ezra.com/`)
- Framework: `Playwright` + `Pytest`
- Architecture: `Page Object Model (POM)`

## Automated critical test cases (from your attached Excel)

Implemented 3 high-priority scenarios from the critical list:

1. **Login screen rendering** (Critical Test Case #2)
   - Validates `Please sign in to your account`, `Email`, `Password`, and `Submit` visibility.
   - Chosen because it is the first gating workflow for all member actions.

2. **Signup path and required fields** (Critical Test Case #1)
   - Validates navigation from login to `Sign up` and presence of:
     - `Legal First Name`
     - `Legal Last Name`
     - `Email`
   - Chosen because member registration failures block onboarding.

3. **Invalid email validation** (Critical Test Case #3)
   - Validates invalid email (`john.doe`) triggers a validation error.
   - Chosen because data quality and form validation are high business-risk and low-flakiness to automate.

## Trade-offs and assumptions

- **Assumption:** staging content and labels are stable (`Please sign in to your account`, `Sign up`, field labels).
- **Assumption:** these tests can run without private test credentials.
- **Trade-off:** selected stable authentication validations first instead of booking + payment to avoid credential and external payment dependency.
- **Trade-off:** focused on 3 critical tests now for reliability and maintainability; framework is ready to expand to scan booking, questionnaire, and payment tests.

## Framework structure

```text
.
├── conftest.py
├── data
│   └── test_data.py
├── pages
│   ├── base_page.py
│   └── ezra_auth_page.py
├── tests
│   └── test_authentication_ezra.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Execute tests

```bash
pytest
```

Default browser is configured as **Google Chrome** (`chromium` + `--browser-channel chrome`).

Choose environment:

```bash
pytest --env staging
pytest --env qa
pytest --env prod
```

Override with a custom URL (takes precedence over `--env`):

```bash
pytest --env staging --base-url "https://custom-host.example.com/"
```

Smoke only:

```bash
pytest -m smoke
```

Regression only:

```bash
pytest -m regression
```

## Test reports

Generate an HTML report:

```bash
mkdir -p artifacts
pytest --env staging -v --html=artifacts/report.html --self-contained-html
```

## Scalability and future implementation

- Add authenticated booking flow coverage for:
  - scan selection and pricing checks (Critical #5/#10/#12)
  - medical questionnaire (Critical #6/#9)
  - payment and confirmation modal (Critical #7/#8/#14)
- Add environment-aware config and secret management for test credentials.
- Add CI pipeline stages (`smoke` on PR, `regression` nightly).
- Add richer reporting (traces/videos/HTML report), retries, and test data factories.

## GitHub repo submission

Push this folder to your GitHub repo and share the repo link as requested:

```bash
git init
git add .
git commit -m "Add Ezra healthcare Playwright Pytest POM critical tests"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```
