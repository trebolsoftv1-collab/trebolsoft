
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: str = "*"
    SUPABASE_PROJECT_URL: str = ""
    SUPABASE_JWKS_URL: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
