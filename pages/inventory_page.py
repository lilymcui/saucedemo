from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.login_page import LoginPage


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def add_to_cart(self, item_name: str) -> None:
        item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(item_name, exact=True)
        )
        item.get_by_role("button", name="Add to cart").click()

    def remove_from_inventory_page(self, item_name: str) -> None:
        item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(item_name, exact=True)
        )
        item.get_by_role("button", name="Remove").click()

    def go_to_cart(self) -> CartPage:
        self.page.locator("[data-test='shopping-cart-link']").click()
        return CartPage(self.page)

    def sort_by_name(self, name_sort: dict) -> None:
        self.page.locator("[data-test='product-sort-container']").select_option(
            name_sort["sort"]
        )
        actual_names = self.page.locator(
            "[data-test='inventory-item-name']"
        ).all_text_contents()

        expected_names = sorted(actual_names, reverse=name_sort["reverse"])

        assert actual_names == expected_names
        expect(self.page.locator("[data-test='active-option']")).to_have_text(
            name_sort["expected"]
        )

    def sort_by_price(self, price_sort: dict) -> None:
        self.page.locator("[data-test='product-sort-container']").select_option(
            price_sort["sort"]
        )
        actual_prices_with_sign = self.page.locator(
            "[data-test='inventory-item-price']"
        ).all_text_contents()
        actual_prices = []
        for price_with_sign in actual_prices_with_sign:
            actual_prices.append(float(price_with_sign[1:]))

        expected_prices = sorted(actual_prices, reverse=price_sort["reverse"])

        assert actual_prices == expected_prices
        expect(self.page.locator("[data-test='active-option']")).to_have_text(
            price_sort["expected"]
        )

    def verify_remove_button(self, item_name: str) -> None:
        item = self.page.locator("[data-test='inventory-item']").filter(
            has=self.page.get_by_text(item_name, exact=True)
        )
        expect(item.get_by_role("button", name="Remove")).to_be_visible()

    def logout(self) -> LoginPage:
        self.page.get_by_role("button", name="Open Menu").click()
        self.page.locator("[data-test='logout-sidebar-link']").click()
        return LoginPage(self.page)

    def verify_inventory_page_loaded(self, product_count: int) -> None:
        expect(self.page.locator("[data-test='title']")).to_have_text("Products")
        expect(self.page.locator("[data-test='inventory-item']")).to_have_count(
            product_count
        )
