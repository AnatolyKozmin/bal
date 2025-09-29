from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cors_origins: str = "http://localhost:5173"
    gsheet_id: str
    gsheet_worksheet: str = "Лист1"

    class Config:
        env_prefix = "BAL_"


settings = Settings()


