from playwright.sync_api import Page, expect

from pages.checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_item_count(self, expected_count: int) -> None:
        expect(self.page.locator("[data-test='inventory-item']")).to_have_count(
            expected_count
        )

    def verify_correct_item(self, expected_item_name: str) -> None:
        item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(expected_item_name, exact=True)
        )
        expect(item).to_be_visible()

    def verify_subtotal(self) -> None:
        """Verify that the displayed subtotal equals the sum of the item prices."""
        prices_with_sign = self.page.locator(
            "[data-test='inventory-item-price']"
        ).all_text_contents()
        prices = []
        for price_with_sign in prices_with_sign:
            prices.append(self._parse_amount(price_with_sign))
        expected_subtotal = sum(prices)

        actual_subtotal_with_sign = self.page.locator(
            "[data-test='subtotal-label']"
        ).text_content()

        actual_subtotal = self._parse_amount(actual_subtotal_with_sign)

        assert round(actual_subtotal, 2) == round(expected_subtotal, 2)

    def verify_total_calculation(self) -> None:
        """Verify the displayed total is the sum of the displayed subtotal and displayed tax."""
        subtotal_with_sign = self.page.locator(
            "[data-test='subtotal-label']"
        ).text_content()
        subtotal = self._parse_amount(subtotal_with_sign)

        tax_with_sign = self.page.locator("[data-test='tax-label']").text_content()
        tax = self._parse_amount(tax_with_sign)

        total_with_sign = self.page.locator("[data-test='total-label']").text_content()
        total = self._parse_amount(total_with_sign)

        assert round(subtotal + tax, 2) == round(total, 2)

    def go_to_complete(self) -> CheckoutCompletePage:
        self.page.get_by_role("button", name="Finish").click()
        return CheckoutCompletePage(self.page)

    def _parse_amount(self, amount_with_sign: str | None) -> float:
        """Extract the numeric amount from the text and return it as a float."""
        assert amount_with_sign is not None, "Expected an amount, but found no text"
        _, amount = amount_with_sign.split("$")
        return float(amount)
