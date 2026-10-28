import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.products import BACKPACK, BIKE_LIGHT
from utils.users_loader import load_users


@pytest.fixture
def inventory_page(page: Page):
    test_data = load_users()
    username = test_data["valid_users"][0]["username"]
    password = test_data["valid_users"][0]["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    return InventoryPage(page)


@pytest.fixture
def cart_page_with_item(inventory_page):
    item = BACKPACK
    inventory_page.add_to_cart(item)
    cart_page = inventory_page.go_to_cart()
    return (cart_page, item)


@pytest.fixture
def problem_user_cart(page: Page):
    test_data = load_users()
    username = test_data["problem_user"][0]["username"]
    password = test_data["problem_user"][0]["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart(BACKPACK)
    cart_page = inventory_page.go_to_cart()
    return cart_page


@pytest.fixture
def cart_page_with_multi_items(inventory_page):
    items = []
    items.append(BACKPACK)
    items.append(BIKE_LIGHT)
    inventory_page.add_to_cart(items[0])
    inventory_page.add_to_cart(items[1])
    cart_page = inventory_page.go_to_cart()
    return (cart_page, items)


@pytest.fixture
def user_info():
    return {"first_name": "Joe", "last_name": "Black", "postal": "V9W 3P1"}
