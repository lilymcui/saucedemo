# SauceDemo UI Test Automation

An automated UI testing framework built with Python, pytest, and Playwright to validate an online shopping website named SauceDemo.

## 1. Technologies Used

- **Python 3.14** - Programming language
- **pytest** - Test framework
- **Playwright** - Browser automation
- **pytest-playwright** - pytest and Playwright integration
- **pytest-html** - HTML test reports
- **Black** - Code formatting
- **Ruff** - Python code linting
- **GitHub Actions** — Continuous integration

## 2. Test Coverage

The framework covers the main SauceDemo online shopping operations.

| Feature | Test Scenarios |
|---|---|
| Login | Test login with valid credentials, invalid credentials, a locked-out user, and empty credentials |
| Sort products by name or price | Verify the products are sorted correctly by name or price |
| Add to cart | Add single and multiple items to the cart. Verify that the correct items are added and that the user can return to the Inventory page from the Cart page |
| Remove from cart | Remove single and multiple items from both the Inventory page and the Cart page, and verify that the items are removed correctly |
| Checkout | Verify that the correct items are checked out and that the subtotal and total are calculated correctly. Verify successful checkout with all required user information entered and error messages when required fields are missing. Finally, verify that `problem_user` cannot correctly enter the last name |  
| Logout | Verify that the user can successfully log out of the application and return to the Login page |

Tests verify expected UI behavior and error messages.

## 3. Project Structure

```text
saucedemo/
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── test_logout.py
│  
├── pages/
│   ├── cart_page.py
│   ├── checkout_complete_page.py
│   ├── checkout_overview_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── test_data/
│   ├── products.py
│   └── users.json
│
├── utils/
│   └── users_loader.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

**Folder descriptions:**

- `tests/` — Contains automated UI test cases.
- `pages/` — Contains Page Object Model (POM) calsses to separate UI interactions with test logic
- `test_data/` — Stores test data separately from test logic.
- `utils/` - Stores helper functions.
- `conftest.py` — Defines shared pytest fixtures.

## 4. Framework Design

The project uses Page Object Model(POM) design pattern to separate UI interactions with test logic for easier maintance.

### Page Object Model(POM) 

Each page is represented by a class containing UI interaction and verification methods associated with that page.

### Pytest Fixtures

Fixtures provide reusable test setup and user data for multiple tests.

### Test data separation

User login information and product names are stored separately from test logic for easier maintenance.

## 5. Installation

### Prerequisites

Python and Git must be installed.

### Clone the Repository

```bash
git clone https://github.com/lilymcui/saucedemo.git
cd saucedemo
```
### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Install Playwright Browsers
```bash
python -m playwright install chromium
```

## 6. Running Tests

### Run all tests

```bash
python -m pytest
```

### Run only one test file, for example, the login tests

```bash
python -m pytest tests/test_login.py
```

### Run tests in headed mode

```bash
python -m pytest --headed
```

## 7. Test Reports and Failure Evidence

### HTML Report

An HTML report will be generated that contains the information about all the tests. The report can be found at:
`reports/report.html`.

### Screenshots

Screenshots will be taken to show the browser's state when a test fails, which helps investigate the failure. The screenshots can be found inside this folder: `test-results/`.

### Playwright Traces
A `trace.zip` will be generated when a test fails to help investigate the failure. The `trace.zip` can be found inside this folder: `test-results/`.

## 8. Known Defect

The `problem_user` cannot correctly enter the last name during checkout, and this is a known defect by design. This test is marked as `xfail` to indicate that the failure as expected, so it doesn't cause the test suite or CI pipeline to fail.

## 9. Continuous Integration

GitHub Actions automatically runs the test suite when code is pushed.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Chromium.
5. Executes the pytest test suite.
6. Uploads the HTML report and failure evidence as a workflow artifact.

