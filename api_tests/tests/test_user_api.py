import pytest
from api_tests.api.user_api import UserAPI


def test_register_user_success():
    user_api = UserAPI()
    email = "eve.holt@reqres.in"
    password = "pistol"

    response = user_api.register_user(email, password)

    assert response.id is not None, "ID should not be None"
    assert response.token is not None, "Token should not be None"
    assert response.token == "QpwL5tke4Pnpja7X4", "Token should match expected value"
