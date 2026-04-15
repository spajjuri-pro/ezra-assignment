from playwright.sync_api import expect

from pages.base_page import BasePage


class EzraAuthPage(BasePage):
    def open(self):
        self.goto("/")

    def login_heading_visible(self) -> bool:
        heading = self.page.get_by_role("heading", name="Please sign in to your account", exact=False).first
        try:
            heading.wait_for(state="visible", timeout=10000)
        except Exception:
            return False
        return heading.is_visible()

    def email_input_visible(self) -> bool:
        return self.page.get_by_label("Email", exact=False).first.is_visible()

    def password_input_visible(self) -> bool:
        return self.page.get_by_label("Password", exact=False).first.is_visible()

    def submit_button_visible(self) -> bool:
        return self.page.get_by_role("button", name="Submit").first.is_visible()

    def go_to_signup(self):
        self.page.get_by_role("link", name="Join", exact=False).first.click()
        self.page.wait_for_url("**/join", timeout=10000)

    def signup_heading_visible(self) -> bool:
        heading = self.page.locator("h1", has_text="In a few steps").last
        try:
            heading.wait_for(state="visible", timeout=10000)
        except Exception:
            return False
        return heading.is_visible()

    def signup_required_fields_visible(self) -> bool:
        # Fields have no placeholders; select by visible input order on the join page
        visible_inputs = self.page.locator("input:visible")
        try:
            visible_inputs.first.wait_for(state="visible", timeout=10000)
        except Exception:
            return False
        count = visible_inputs.count()
        # Expect at least 5 visible inputs: first name, last name, email, phone, password
        return count >= 5

    def enter_login_email(self, email: str):
        self.page.get_by_label("Email", exact=False).first.fill(email)

    def enter_login_password(self, password: str):
        self.page.get_by_label("Password", exact=False).first.fill(password)

    def click_submit(self):
        self.page.get_by_role("button", name="Submit").first.click()

    def trigger_email_validation(self):
        self.page.get_by_label("Password", exact=False).first.click()

    def email_validation_message(self) -> str:
        error = self.page.get_by_text("The Email field is invalid.", exact=False).first
        if error.count() == 0:
            return ""
        return error.inner_text().strip()

    # --- TC1: Account Creation helpers ---

    def signup_link_visible(self) -> bool:
        return self.page.get_by_role("link", name="Join", exact=False).first.is_visible()

    def fill_signup_first_name(self, name: str):
        self.page.locator("input:visible").nth(0).fill(name)

    def fill_signup_last_name(self, name: str):
        self.page.locator("input:visible").nth(1).fill(name)

    def fill_signup_email(self, email: str):
        self.page.locator("input:visible").nth(2).fill(email)

    def fill_signup_phone(self, phone: str):
        self.page.locator("input:visible").nth(3).fill(phone)

    def fill_signup_password(self, password: str):
        self.page.locator("input[type='password']:visible").first.fill(password)

    def accept_terms(self):
        self.page.get_by_role("button", name="I agree to Ezra's terms of use", exact=False).first.click()

    def submit_signup(self):
        self.page.get_by_role("button", name="Submit").first.click()

    def signup_first_name_is_required(self) -> bool:
        first = self.page.locator("input:visible").nth(0)
        first.click()
        first.press("Tab")
        error = self.page.get_by_text("The Legal First Name field is required.", exact=False).first
        try:
            error.wait_for(state="visible", timeout=5000)
        except Exception:
            return False
        return error.is_visible()

    def signup_last_name_is_required(self) -> bool:
        last = self.page.locator("input:visible").nth(1)
        last.click()
        last.press("Tab")
        error = self.page.get_by_text("The Legal Last Name field is required.", exact=False).first
        try:
            error.wait_for(state="visible", timeout=5000)
        except Exception:
            return False
        return error.is_visible()

    # --- TC2: Login Authentication helpers ---

    def password_field_masks_input(self) -> bool:
        pwd_field = self.page.get_by_label("Password", exact=False).first
        return pwd_field.get_attribute("type") == "password"

    def login(self, email: str, password: str):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_submit()

    def is_logged_in(self) -> bool:
        """Returns True if post-login navigation items are visible (Sign out or Home)."""
        sign_out = self.page.get_by_text("Sign out", exact=False).first
        home_nav = self.page.get_by_role("link", name="Home", exact=False).first
        try:
            sign_out.or_(home_nav).wait_for(state="visible", timeout=15000)
        except Exception:
            return False
        return sign_out.is_visible() or home_nav.is_visible()
