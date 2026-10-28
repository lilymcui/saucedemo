def test_logout(inventory_page):
    login_page = inventory_page.logout()
    login_page.verify_on_login_page()
