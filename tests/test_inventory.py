import pytest

from test_data.products import BACKPACK

item_list = [BACKPACK]

name_sort_list = [
    {"sort": "az", "expected": "Name (A to Z)", "reverse": False},
    {"sort": "za", "expected": "Name (Z to A)", "reverse": True},
]

price_sort_list = [
    {"sort": "lohi", "expected": "Price (low to high)", "reverse": False},
    {"sort": "hilo", "expected": "Price (high to low)", "reverse": True},
]


@pytest.mark.parametrize("name_sort", name_sort_list)
def test_sort_by_name(inventory_page, name_sort):
    inventory_page.sort_by_name(name_sort)


@pytest.mark.parametrize("price_sort", price_sort_list)
def test_sort_by_price(inventory_page, price_sort):
    inventory_page.sort_by_price(price_sort)


@pytest.mark.parametrize("item_name", item_list)
def test_remove_button(inventory_page, item_name):
    inventory_page.add_to_cart(item_name)
    inventory_page.verify_remove_button(item_name)
