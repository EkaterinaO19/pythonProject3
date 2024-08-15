from typing import Optional


class RegisterRequest:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def to_dict(self) -> dict:
        return {
            "email": self.email,
            "password": self.password
        }


class RegisterResponse:
    def __init__(self, id: Optional[int], token: Optional[str]):
        self.id = id
        self.token = token

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            token=data.get("token")
        )
