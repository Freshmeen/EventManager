from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Books API"
    DB_URL: str = "mysql+aiomysql://event_manager_example:qwerty@localhost:3307/mydb"

    class Config:
        env_file = ".env"


settings = Settings()
