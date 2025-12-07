from fastapi import HTTPException


class APIException(HTTPException):
    def __init__(self, status_code: int, detail: str, error_code: str | None = None):
        super().__init__(status_code=status_code, detail=detail)
        if error_code is not None:
            self.error_code = error_code

    def __repr__(self):
        return super().__repr__()[:-1] + f", error_code={self.error_code!r})"
