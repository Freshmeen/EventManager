from backend.app.api.v1.exceptions.base import BadRequestException


class EmailAlreadyExistsException(BadRequestException):
    def __init__(self, email: str):
        super().__init__(f"Email {email} already registered", "EMAIL_ALREADY_EXISTS")
