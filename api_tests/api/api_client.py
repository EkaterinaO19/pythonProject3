import requests
from api_tests.api.endpoints import REGISTER
from api_tests.models.register import RegisterRequest, RegisterResponse


class APIClient:
    def register_user(register_request: RegisterRequest) -> RegisterResponse:
        response = requests.post(REGISTER, json=register_request.to_dict())
        response_data = response.json()

        if response.status_code == 200:
            return RegisterResponse.from_dict(response_data)
        else:
            response.raise_for_status()