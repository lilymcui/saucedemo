from playwright.sync_api import Page, expect


class CheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_checkout_successful(self) -> None:
        expect(self.page.locator("[data-test='complete-header']")).to_have_text(
            "Thank you for your order!"
        )

    def verify_badge_disappeared(self) -> None:
        expect(
            self.page.locator("[data-test='shopping-cart-badge']")
        ).not_to_be_visible()
