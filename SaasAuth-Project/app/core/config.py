from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "NexusAuth"
    API_V1_STR: str = "/api/v1"
    
    # Security
    # In production, this MUST be a long, random string
    SECRET_KEY: str 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str

    # CORS - Add your frontend URLs here
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Automatically load variables from a .env file
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )

settings = Settings()
