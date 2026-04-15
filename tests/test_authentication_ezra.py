import uuid
import pytest

from data.test_data import (
    VALID_SIGNUP_FIRST_NAME,
    VALID_SIGNUP_LAST_NAME,
    VALID_SIGNUP_EMAIL,
    VALID_CREDENTIALS_EMAIL,
    VALID_CREDENTIALS_PASSWORD,
)

EMAIL_VALIDATION_CASES = [
    pytest.param("john.doe",              True,  "The Email field is invalid.", id="missing-at-sign"),
    pytest.param("invalid-email-format",  True,  "The Email field is invalid.", id="no-at-or-domain"),
    pytest.param("test@",                 True,  "The Email field is invalid.", id="missing-domain"),
    pytest.param("test@example.com",      False, "",                            id="valid-email"),
]


@pytest.mark.smoke
def test_login_page_displays_required_fields(auth_page):
    auth_page.open()
    assert auth_page.login_heading_visible()
    assert auth_page.email_input_visible()
    assert auth_page.password_input_visible()
    assert auth_page.submit_button_visible()


@pytest.mark.regression
@pytest.mark.parametrize("email, expects_error, expected_message", EMAIL_VALIDATION_CASES)
def test_login_email_field_validation(auth_page, email, expects_error, expected_message):
    """TC2/TC3: Verify email field validation for both valid and invalid inputs."""
    auth_page.open()
    auth_page.enter_login_email(email)
    auth_page.trigger_email_validation()
    message = auth_page.email_validation_message()
    if expects_error:
        assert message == expected_message
    else:
        assert message == ""


@pytest.mark.smoke
def test_login_with_valid_credentials(auth_page):
    """TC2: Verify a user can log in successfully with valid email and password."""
    auth_page.open()
    auth_page.login(VALID_CREDENTIALS_EMAIL, VALID_CREDENTIALS_PASSWORD)
    assert auth_page.is_logged_in()


@pytest.mark.regression
def test_signup_page_has_expected_text_and_primary_fields(auth_page):
    auth_page.open()
    auth_page.go_to_signup()
    assert auth_page.signup_heading_visible()
    assert auth_page.signup_required_fields_visible()


# ── TC1: Account Creation - New Member Registration ───────────────────────────


@pytest.mark.regression
def test_signup_form_fields_accept_valid_input(auth_page):
    """TC1: Verify signup form fields accept valid input without errors."""
    auth_page.open()
    auth_page.go_to_signup()
    auth_page.fill_signup_first_name(VALID_SIGNUP_FIRST_NAME)
    auth_page.fill_signup_last_name(VALID_SIGNUP_LAST_NAME)
    auth_page.fill_signup_email(VALID_SIGNUP_EMAIL)
    assert auth_page.signup_required_fields_visible()


@pytest.mark.regression
def test_signup_first_name_and_last_name_are_required(auth_page):
    """TC1: Verify Legal First Name and Legal Last Name fields are marked as required."""
    auth_page.open()
    auth_page.go_to_signup()
    assert auth_page.signup_first_name_is_required()
    assert auth_page.signup_last_name_is_required()


@pytest.mark.regression
def test_complete_signup_with_valid_data_reaches_dashboard(auth_page):
    """TC1: Complete signup with valid random credentials and verify dashboard is shown."""
    unique_id = uuid.uuid4().hex[:8]
    email = f"testuser.{unique_id}@mailinator.com"
    password = f"Test@{unique_id[:6]}1A"

    auth_page.open()
    auth_page.go_to_signup()
    auth_page.fill_signup_first_name("Test")
    auth_page.fill_signup_last_name("User")
    auth_page.fill_signup_email(email)
    auth_page.fill_signup_phone("2015550123")
    auth_page.fill_signup_password(password)
    auth_page.accept_terms()
    auth_page.submit_signup()
    assert auth_page.is_logged_in()


