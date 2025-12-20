from fastapi import status

from backend.app.api.v1.exceptions.base import APIException


class ForbiddenException(APIException):
    def __init__(self, message: str = "Forbidden: insufficient permissions", error_code: str = "FORBIDDEN"):
        super().__init__(status.HTTP_403_FORBIDDEN, message, error_code)