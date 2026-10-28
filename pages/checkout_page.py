from playwright.sync_api import Page, expect

from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_info(self, first_name: str, last_name: str, postal: str) -> None:
        self.page.locator("[data-test='firstName']").fill(first_name)
        self.page.locator("[data-test='lastName']").fill(last_name)
        self.page.locator("[data-test='postalCode']").fill(postal)

    def verify_checkout_message(self) -> None:
        expect(self.page.locator("[data-test='title']")).to_have_text(
            "Checkout: Your Information"
        )

    def verify_invalid_input(self, error_message: str) -> None:
        expect(self.page.locator("[data-test='error']")).to_have_text(error_message)

    def click_on_continue(self) -> None:
        self.page.get_by_role("button", name="Continue").click()

    def go_to_overview(self) -> CheckoutOverviewPage:
        self.click_on_continue()
        return CheckoutOverviewPage(self.page)

    def verify_last_name(self, expected_last_name: str) -> None:
        expect(self.page.locator("[data-test='lastName']")).to_have_value(
            expected_last_name
        )
