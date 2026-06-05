from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):

    gemini_api_key: str = ""

    groq_api_key: str = ""

    github_token: str = ""

    github_webhook_secret: str = ""

    gemini_model: str = (
        "gemini-2.5-flash"
    )

    groq_model: str = (
        "llama-3.3-70b-versatile"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

# import os

# print("=" * 80)
# print("CWD:", os.getcwd())
# print("ENV GITHUB_TOKEN:", repr(os.getenv("GITHUB_TOKEN")))
# print("=" * 80)

# print("SETTINGS TOKEN:", repr(settings.github_token))