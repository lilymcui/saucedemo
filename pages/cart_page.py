from typing import TYPE_CHECKING

from playwright.sync_api import Page, expect

from pages.checkout_page import CheckoutPage

if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_added_item(self, expected_count: int, item_name: str) -> None:
        expect(self.page.locator("[data-test='shopping-cart-badge']")).to_have_text(
            str(expected_count)
        )
        expect(self.page.locator("[data-test='inventory-item']")).to_have_count(
            expected_count
        )
        item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(item_name, exact=True)
        )
        expect(item).to_be_visible()

    def remove_from_cart_page(self, item_name: str) -> None:
        cart_item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(item_name, exact=True)
        )
        cart_item.get_by_role("button", name="Remove").click()

    def verify_item_count_in_cart(self, item_count: int) -> None:
        if item_count == 0:
            expect(
                self.page.locator("[data-test='shopping-cart-badge']")
            ).not_to_be_visible()
        expect(self.page.locator("[data-test='inventory-item']")).to_have_count(
            item_count
        )

    def go_to_checkout(self) -> CheckoutPage:
        self.page.get_by_role("button", name="Checkout").click()
        return CheckoutPage(self.page)

    def verify_item_deleted(self, item_name: str) -> None:
        item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(item_name, exact=True)
        )
        expect(item).not_to_be_visible()

    def continue_shopping(self) -> "InventoryPage":
        # Local import avoids a circular dependency with InventoryPage.
        from pages.inventory_page import InventoryPage

        self.page.get_by_role("button", name="Continue Shopping").click()
        return InventoryPage(self.page)
