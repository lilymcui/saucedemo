import pytest


def test_successful_checkout(cart_page_with_item, user_info):
    cart_page, item = cart_page_with_item
    checkout_page = cart_page.go_to_checkout()
    checkout_page.verify_checkout_message()
    first_name = user_info["first_name"]
    last_name = user_info["last_name"]
    postal = user_info["postal"]
    checkout_page.fill_info(first_name, last_name, postal)
    checkout_overview_page = checkout_page.go_to_overview()
    checkout_overview_page.verify_item_count(1)
    checkout_overview_page.verify_correct_item(item)
    checkout_overview_page.verify_subtotal()
    checkout_complete_page = checkout_overview_page.go_to_complete()
    checkout_complete_page.verify_checkout_successful()
    checkout_complete_page.verify_badge_disappeared()


def test_successful_multi_items_checkout(cart_page_with_multi_items, user_info):
    cart_page, items = cart_page_with_multi_items
    checkout_page = cart_page.go_to_checkout()
    checkout_page.verify_checkout_message()
    first_name = user_info["first_name"]
    last_name = user_info["last_name"]
    postal = user_info["postal"]
    checkout_page.fill_info(first_name, last_name, postal)
    checkout_overview_page = checkout_page.go_to_overview()
    checkout_overview_page.verify_item_count(2)
    for item_name in items:
        checkout_overview_page.verify_correct_item(item_name)
    checkout_overview_page.verify_subtotal()
    checkout_overview_page.verify_total_calculation()
    checkout_complete_page = checkout_overview_page.go_to_complete()
    checkout_complete_page.verify_checkout_successful()
    checkout_complete_page.verify_badge_disappeared()


def test_missing_firstname_checkout(cart_page_with_item, user_info):
    cart_page, _ = cart_page_with_item
    checkout_page = cart_page.go_to_checkout()
    checkout_page.verify_checkout_message()
    first_name = ""
    last_name = user_info["last_name"]
    postal = user_info["postal"]
    checkout_page.fill_info(first_name, last_name, postal)
    checkout_page.click_on_continue()
    checkout_page.verify_invalid_input("Error: First Name is required")


def test_missing_lastname_checkout(cart_page_with_item, user_info):
    cart_page, _ = cart_page_with_item
    checkout_page = cart_page.go_to_checkout()
    checkout_page.verify_checkout_message()
    first_name = user_info["first_name"]
    last_name = ""
    postal = user_info["postal"]
    checkout_page.fill_info(first_name, last_name, postal)
    checkout_page.click_on_continue()
    checkout_page.verify_invalid_input("Error: Last Name is required")


def test_missing_postalcode_checkout(cart_page_with_item, user_info):
    cart_page, _ = cart_page_with_item
    checkout_page = cart_page.go_to_checkout()
    checkout_page.verify_checkout_message()
    first_name = user_info["first_name"]
    last_name = user_info["last_name"]
    postal = ""
    checkout_page.fill_info(first_name, last_name, postal)
    checkout_page.click_on_continue()
    checkout_page.verify_invalid_input("Error: Postal Code is required")


@pytest.mark.xfail(
    reason="known saucedemo error: problem user cannot enter last name during checkout",
    strict=True,
)
def test_problem_user_checkout(problem_user_cart, user_info):
    checkout_page = problem_user_cart.go_to_checkout()
    checkout_page.verify_checkout_message()
    first_name = user_info["first_name"]
    last_name = user_info["last_name"]
    postal = user_info["postal"]
    checkout_page.fill_info(first_name, last_name, postal)
    checkout_page.verify_last_name(last_name)
