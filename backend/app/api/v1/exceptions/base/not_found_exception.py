from fastapi import status

from backend.app.api.v1.exceptions.base.api_exception import APIException


class NotFoundException(APIException):
    def __init__(self, message: str, error_code: str = None):
        super().__init__(status.HTTP_404_NOT_FOUND, message, error_code)
