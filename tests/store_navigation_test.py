import pytest
import allure


@allure.feature('Navigation')
@allure.story('Navigation Feature')
@allure.title('Navigation through burger menu')
@allure.severity(allure.severity_level.CRITICAL)
def navigation_burger_check(logged_in_page, navigation_page):
    navigation_page.navigate_and_check_url("about")
    navigation_page.navigate_and_check_url("all_items")
    navigation_page.navigate_and_check_url("logout")
    navigation_page.navigate_and_check_url("reset")
