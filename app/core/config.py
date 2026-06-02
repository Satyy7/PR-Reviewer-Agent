from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    gemini_api_key: str = ""

    github_token: str = ""

    github_webhook_secret: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()