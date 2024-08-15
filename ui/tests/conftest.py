import time
import pytest
import os
from playwright.sync_api import Page, BrowserContext, sync_playwright
from datetime import datetime

from ui.pages.checkout_step_two_page import CheckoutStepTwoPage
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashBoardPage
from ui.pages.navigation_page import NavigationPage
from ui.pages.store_inventory_page import StoreInventoryPage
from ui.pages.store_login_page import StoreLoginPage
from ui.pages.store_product_page import StoreProductPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_step_one_page import CheckoutStepOnePage

"""Фикстуры позволяют инициализировать объекты, которые затем могут быть использованы в тестах. 
Это улучшает читаемость и уменьшает дублирование кода."""

SCREENSHOTS_DIR = "test_screenshots"
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get('logged_in_page')
        if page:
            screenshot_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)
            page.screenshot(path=screenshot_path)


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, logged_in_page: Page):
    yield
    screenshot_name = f"{request.node.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)
    logged_in_page.screenshot(path=screenshot_path)


# @pytest.fixture
# def logged_in_page(page: Page):
#     login_page = StoreLoginPage(page)
#     login_page.navigate()
#     login_page.login('standard_user', 'secret_sauce')
#     return page

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=True)
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    return browser_context.new_page()


@pytest.fixture(scope="function")
def logged_in_page(browser_context: BrowserContext, page: Page):
    expires_in_one_hour = int(time.time()) + 3600

    browser_context.add_cookies([{
        'name': 'session-username',
        'value': 'standard_user',
        'domain': 'www.saucedemo.com',
        'path': '/',
        'expires': expires_in_one_hour
    }])
    # Navigate to the inventory page directly
    page.goto('https://www.saucedemo.com/inventory.html')
    return page


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page: Page):
    return DashBoardPage(page)


@pytest.fixture
def store_login_page(page: Page):
    return StoreLoginPage(page)


@pytest.fixture
def store_inventory_page(page: Page):
    return StoreInventoryPage(page)


@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def store_product_page(page: Page):
    return StoreProductPage(page)


@pytest.fixture
def navigation_page(page: Page):
    return NavigationPage(page)


@pytest.fixture
def checkout_step_one_page(page: Page):
    return CheckoutStepOnePage(page)


@pytest.fixture
def checkout_step_two_page(page: Page):
    return CheckoutStepTwoPage(page)

# #
# # @pytest.fixture(scope="session")
# # def browser_context_args(browser_context_args):
# #     return {
# #         "viewport": {
# #             "width": 1920,
# #             "height": 1080,
# #         }
# #     }
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "stepik",
#                     "value": "sd4fFfv!x_cfcstepik",
#                     "url": "https://example.com"  # Замените на нужный URL
#                 },
#             ]
#         },
#     }
