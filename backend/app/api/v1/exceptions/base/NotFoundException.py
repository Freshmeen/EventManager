from backend.app.api.v1.exceptions.base.ApiException import APIException
from fastapi import status


class NotFoundException(APIException):
    def __init__(self, message: str, error_code: str = None):
        super().__init__(status.HTTP_404_NOT_FOUND, message, error_code)
