from pathlib import Path

import pytest

from pages.ezra_auth_page import EzraAuthPage

ENV_URLS = {
    "staging": "https://myezra-staging.ezra.com/",
    # Update the placeholders below with your real target URLs.
    "qa": "https://myezra-qa.ezra.com/",
    "prod": "https://myezra.ezra.com/",
}


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        choices=tuple(ENV_URLS.keys()),
        help="Target environment key (staging/qa/prod)",
    )
    

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    # --base-url is provided by pytest-playwright. If set, use it.
    override_url = pytestconfig.getoption("--base-url")
    if override_url:
        return override_url

    # Otherwise resolve URL from the selected environment.
    env = pytestconfig.getoption("--env")
    return ENV_URLS[env]


@pytest.fixture
def auth_page(page, base_url):
    return EzraAuthPage(page=page, base_url=base_url)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or report.passed:
        return

    page = item.funcargs.get("page")
    if not page:
        return

    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(artifacts_dir / f"{item.name}.png"), full_page=True)
