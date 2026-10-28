import pytest

from test_data.products import BACKPACK, BIKE_LIGHT

item_list = [BACKPACK]
multiple_items = [BACKPACK, BIKE_LIGHT]
EXPECTED_PRODUCT_COUNT = 6


@pytest.mark.parametrize("item_name", item_list)
def test_add_to_cart(inventory_page, item_name):
    inventory_page.add_to_cart(item_name)
    cart_page = inventory_page.go_to_cart()
    cart_page.verify_added_item(1, item_name)


@pytest.mark.parametrize("item_name", item_list)
def test_remove_from_cart(inventory_page, item_name):
    inventory_page.add_to_cart(item_name)
    cart_page = inventory_page.go_to_cart()
    cart_page.remove_from_cart_page(item_name)
    cart_page.verify_item_count_in_cart(0)


@pytest.mark.parametrize("item_name", item_list)
def test_remove_from_inventory_page(inventory_page, item_name):
    inventory_page.add_to_cart(item_name)
    inventory_page.remove_from_inventory_page(item_name)
    cart_page = inventory_page.go_to_cart()
    cart_page.verify_item_count_in_cart(0)


def test_add_multiple_to_cart(inventory_page):
    for item in multiple_items:
        inventory_page.add_to_cart(item)
    cart_page = inventory_page.go_to_cart()
    for item in multiple_items:
        cart_page.verify_added_item(2, item)


def test_remove_multiple_from_cart(inventory_page):
    for item in multiple_items:
        inventory_page.add_to_cart(item)
    cart_page = inventory_page.go_to_cart()
    cart_page.remove_from_cart_page(multiple_items[0])
    cart_page.verify_item_count_in_cart(1)
    cart_page.verify_added_item(1, multiple_items[1])
    cart_page.verify_item_deleted(multiple_items[0])
    cart_page.remove_from_cart_page(multiple_items[1])
    cart_page.verify_item_count_in_cart(0)
    cart_page.verify_item_deleted(multiple_items[1])


def test_remove_multiple_from_inventory_page(inventory_page):
    for item in multiple_items:
        inventory_page.add_to_cart(item)
    inventory_page.remove_from_inventory_page(multiple_items[0])
    cart_page = inventory_page.go_to_cart()
    cart_page.verify_item_count_in_cart(1)
    cart_page.verify_added_item(1, multiple_items[1])
    cart_page.verify_item_deleted(multiple_items[0])
    inventory_page = cart_page.continue_shopping()
    inventory_page.remove_from_inventory_page(multiple_items[1])
    cart_page = inventory_page.go_to_cart()
    cart_page.verify_item_count_in_cart(0)
    cart_page.verify_item_deleted(multiple_items[1])


def test_continue_shopping(inventory_page):
    for item in multiple_items:
        inventory_page.add_to_cart(item)
    cart_page = inventory_page.go_to_cart()
    inventory_page = cart_page.continue_shopping()
    inventory_page.verify_inventory_page_loaded(EXPECTED_PRODUCT_COUNT)
