from playwright.sync_api import Page, expect

SAUCEDEMO_URL = "https://www.saucedemo.com/"


class LoginPage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self) -> None:
        self.page.goto(SAUCEDEMO_URL)

    def login(self, username: str, password: str) -> None:
        self.page.locator("[data-test='username']").fill(username)
        self.page.locator("[data-test='password']").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def verify_successful_login(self) -> None:
        expect(self.page.locator("[data-test='title']")).to_contain_text("Products")

    def verify_invalid_login(self) -> None:
        expect(self.page.locator("[data-test='error']")).to_have_text(
            "Epic sadface: Username and password do not match any user in this service"
        )

    def verify_empty_credentials_login(self) -> None:
        expect(self.page.locator("[data-test='error']")).to_have_text(
            "Epic sadface: Username is required"
        )

    def verify_locked_out_user(self) -> None:
        expect(self.page.locator("[data-test='error']")).to_have_text(
            "Epic sadface: Sorry, this user has been locked out."
        )

    def verify_on_login_page(self) -> None:
        expect(self.page.locator("[data-test='username']")).to_be_visible()
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()
