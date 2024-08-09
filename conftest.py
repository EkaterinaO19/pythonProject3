import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
"""Фикстуры позволяют инициализировать объекты, которые затем могут быть использованы в тестах. 
Это улучшает читаемость и уменьшает дублирование кода."""

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashBoardPage(page)

"""Эти фикстуры создают экземпляры LoginPage и DashboardPage, 
которые могут быть использованы в тестах."""

#
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