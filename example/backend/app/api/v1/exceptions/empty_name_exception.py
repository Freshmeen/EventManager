from fastapi.responses import Response, JSONResponse


class EmptyNameException(Exception):
    pass


def empty_name_exception_handler(*_) -> Response:
    return JSONResponse(
        status_code=400,
        content={"message": "Name cannot be empty"},
    )