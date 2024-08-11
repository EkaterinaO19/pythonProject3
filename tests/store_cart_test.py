import pytest
import allure


@allure.feature('Cart')
@allure.story('Add item to cart')
@allure.title('Add item to cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_test(store_login_page, store_inventory_page, cart_page):
    store_login_page.navigate()
    store_login_page.login('standard_user', 'secret_sauce')
    store_inventory_page.add_to_cart()
    store_inventory_page.navigate_to_cart()
    cart_product_name = cart_page.get_product_name()
    product_name = store_inventory_page.get_product_name()
    assert cart_product_name == product_name


@allure.feature('Cart')
@allure.story('Add item to cart')
@allure.title('Add badge with amount of product added to cart')
@allure.severity(allure.severity_level.MINOR)
def test_add_badge_to_cart_test(logged_in_page, store_login_page, store_inventory_page):
    store_inventory_page.add_to_cart()
    product_amount = store_inventory_page.get_product_quantity()
    cart_badge_quantity = store_inventory_page.get_cart_badge()
    assert product_amount == cart_badge_quantity


@allure.feature('Cart')
@allure.story('Add item to cart')
@allure.title('Add item to cart on product page')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_on_product_page(logged_in_page, store_login_page, store_product_page):
    store_product_page.navigate()
    store_product_page.add_to_cart()
    store_product_page.assert_remove_btn()

