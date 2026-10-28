import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from utils.users_loader import load_users

test_data = load_users()


@pytest.mark.parametrize("user_credentials", test_data["valid_users"])
def test_valid_login(page: Page, user_credentials):
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    login_page.verify_successful_login()


@pytest.mark.parametrize("user_credentials", test_data["invalid_password_users"])
def test_invalid_password_login(page: Page, user_credentials):
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    login_page.verify_invalid_login()


@pytest.mark.parametrize("user_credentials", test_data["invalid_username_users"])
def test_invalid_username_login(page: Page, user_credentials):
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    login_page.verify_invalid_login()


@pytest.mark.parametrize("user_credentials", test_data["user_with_empty_credentials"])
def test_empty_credentials_login(page: Page, user_credentials):
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    login_page.verify_empty_credentials_login()


@pytest.mark.parametrize("user_credentials", test_data["locked_out_user"])
def test_locked_out_user_login(page: Page, user_credentials):
    username = user_credentials["username"]
    password = user_credentials["password"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    login_page.verify_locked_out_user()
