from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Books API"
    DB_URL: str = "mysql+aiomysql://event_manager:qwerty@localhost:3307/event_manager"

    class Config:
        env_file = ".env"


settings = Settings()
