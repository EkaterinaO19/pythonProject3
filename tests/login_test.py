import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage

# Используем фикстуры для упрощения тестов.
@allure.feature('Авторизаци')
@allure.story('Авторизации недействительные учетные данные')
@allure.title('Авторизаиця с недействительными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_failure(login_page):
    # login_page = LoginPage(page)
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login('invalid', 'invalid')
    # with allure.step('Url не изменился'):
    #     assert login_page.url == 'https://zimaev.github.io/pom/'
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


# Создается объект DashboardPage.
# Проверяется, что на странице отображается корректное приветственное сообщение.


@allure.feature('Login')
@allure.story('Login Feature')
@allure.title('Авторизаиця с корректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    # login_page = LoginPage(page)
    # dashboard_page = DashBoardPage(page)
    """В этих тестах : Удалены импорты классов страниц Фикстура page не передается в теста Фикстуры login_page и dashboard_page используются для инициализации соответствующих объектов."""

    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f"Welcome {username}")


"""В этом тесте: 
Используется декоратор pytest.mark.parametrize для задания нескольких наборов данных.
Тест запускается для каждой пары username и password"""

"""Параметризация тестов позволяет запускать одну и ту же тестовую функцию с разными наборами входных данных. Это особенно полезно, когда вы хотите проверить, что ваш код работает корректно для разных сценариев.
Вместо того чтобы создавать отдельные тестовые функции для каждого набора данных, вы можете использовать параметризацию, чтобы сократить дублирование кода и улучшить общую структуру тестов."""
"""Это делается с помощью декоратора @pytest.mark.parametrize."""


