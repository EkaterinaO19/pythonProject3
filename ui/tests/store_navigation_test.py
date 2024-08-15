import allure


@allure.feature('Navigation')
@allure.story('Navigation Feature')
@allure.title('Navigation through burger menu')
@allure.severity(allure.severity_level.CRITICAL)
def navigation_burger_check(logged_in_page, navigation_page):
    with allure.step("Navigate to 'about' page and check URL"):
        navigation_page.navigate_and_check_url("about")

    with allure.step("Navigate to 'all_items' page and check URL"):
        navigation_page.navigate_and_check_url("all_items")

    with allure.step("Navigate to 'logout' page and check URL"):
        navigation_page.navigate_and_check_url("logout")

    with allure.step("Navigate to 'reset' page and check URL"):
        navigation_page.navigate_and_check_url("reset")

