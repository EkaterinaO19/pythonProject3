import pytest
import allure


@allure.feature('Cart')
@allure.story('Add item to cart')
@allure.title('Add item to cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(logged_in_page, store_inventory_page, cart_page):
    store_inventory_page.add_to_cart()
    store_inventory_page.navigate_to_cart()
    cart_product_name = cart_page.get_product_name()
    product_name = store_inventory_page.get_product_name()
    assert cart_product_name == product_name


@allure.feature('Cart')
@allure.story('Add item to cart')
@allure.title('Add badge with amount of product added to cart')
@allure.severity(allure.severity_level.MINOR)
def test_add_badge_to_cart(logged_in_page, store_login_page, store_inventory_page):
    store_inventory_page.add_to_cart()
    product_amount = store_inventory_page.get_product_quantity()
    cart_badge_quantity = store_inventory_page.get_cart_badge()
    assert product_amount == cart_badge_quantity


@allure.feature('Cart')
@allure.story('Add item to cart')
@allure.title('Add item to cart on product page')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_on_product_page(logged_in_page, store_product_page):
    store_product_page.navigate()
    store_product_page.add_to_cart()
    store_product_page.assert_remove_btn()


# @allure.feature('Cart')
# @allure.story('Checkout item')
# @allure.title('Navigate to checkout page')
# @allure.severity(allure.severity_level.CRITICAL)
# def test_continue_shopping(logged_in_page, store_inventory_page,cart_page):

# with allure.step("Add items to the cart"):
#     store_inventory_page.add_to_cart()
#
# with allure.step("Navigate to the cart"):
#     store_inventory_page.navigate_to_cart()
#
# with allure.step("Proceed to checkout"):
#     cart_page.checkout()
#
# with allure.step("Verify the checkout page URL"):
#     current_url = 'https://www.saucedemo.com/checkout-step-one.html'
#     assert current_url == cart_page.get_current_url(), f"Expected URL: {current_url}, but got {cart_page.get_current_url()}"


@allure.feature('Cart')
@allure.story('Checkout item')
@allure.title('Navigate to checkout page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_product(logged_in_page, store_inventory_page, cart_page):
    store_inventory_page.add_to_cart()
    store_inventory_page.navigate_to_cart()
    cart_page.checkout()

    expected_url = 'https://www.saucedemo.com/checkout-step-one.html'
    assert expected_url == cart_page.get_current_url(), f"Expected URL: {expected_url}, but got {cart_page.get_current_url()}"


@allure.feature('Cart')
@allure.story('Checkout item')
@allure.title('Fill in checkout form')
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_product(logged_in_page, store_inventory_page, cart_page, checkout_step_one_page):
    store_inventory_page.add_to_cart()
    store_inventory_page.navigate_to_cart()
    cart_page.checkout()

    checkout_step_one_page.fill_name("John")
    checkout_step_one_page.fill_lastname("Smith")
    checkout_step_one_page.fill_postal_code("12345")
    checkout_step_one_page.click_continue_button()
    expected_url = 'https://www.saucedemo.com/checkout-step-two.html'
    assert expected_url == checkout_step_one_page.get_url(), f"Expected URL: {expected_url}, but got {checkout_step_one_page.get_url()}"


