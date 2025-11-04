from fastapi import FastAPI
from example.backend.app.api.v1.exceptions.empty_name_exception import EmptyNameException, empty_name_exception_handler


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(EmptyNameException, empty_name_exception_handler)
