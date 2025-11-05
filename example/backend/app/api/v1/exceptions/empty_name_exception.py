from example.backend.app.api.v1.exceptions.api_exception import APIException


class EmptyNameException(APIException):
    def __init__(self):
        super().__init__(status_code=400, detail="Name cannot be empty", error_code="EMPTY_NAME")