from backend.app.api.v1.exceptions.base import BadRequestException

class TooShortPasswordException(ValueError):
    def __init__(self):
        super().__init__("Password should be at least 8 characters")