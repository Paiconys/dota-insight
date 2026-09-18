from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_ENV = Path(__file__).resolve().parents[1] / ".env"


class Settings(BaseSettings):
    app_name: str = "Dota Insight Hub"
    debug: bool = False
    database_url: str = ""

    model_config = SettingsConfigDict(env_file=_ENV, extra="ignore")


settings = Settings()
