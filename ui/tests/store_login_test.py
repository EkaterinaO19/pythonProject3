import pytest
import allure


@allure.feature('Login')
@allure.story('Login Feature')
@allure.title('Авторизаиця с корректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username, password', [
    ('standard_user', 'secret_sauce'),
    ('visual_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('error_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce')
])
def test_login_success(store_login_page, store_inventory_page, username, password):
    store_login_page.navigate()
    store_login_page.login(username, password)

    store_inventory_page.assert_logo("Swag Labs")


@allure.feature('Login')
@allure.story('Login Feature')
@allure.title('Авторизаиця с некорректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username, password', [
    ('locked_out_user', 'secret_sauce'),
])
def test_login_failure(store_login_page, username, password):
    store_login_page.navigate()
    store_login_page.login(username, password)
    store_login_page.err_message() == "Epic sadface: Sorry, this user has been locked out."


