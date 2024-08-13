import requests
from api_tests.models.register import RegisterRequest, RegisterResponse

REGISTER_URL = "https://reqres.in/api/register"


class UserAPI:
    def register_user(self, email: str, password: str) -> RegisterResponse:
        request_data = RegisterRequest(email=email, password=password)
        response = requests.post(REGISTER_URL, json=request_data.to_dict())
        response_data = response.json()

        if response.status_code == 200:
            return RegisterResponse.from_dict(response_data)
        else:
            response.raise_for_status()