from functools import lru_cache
from pydantic_settings import SettingsConfigDict,BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=("ENV",".env"),extra="ignore")

    environment:str=Field(...,alias="ENVIRONMENT")
    prefix_app:str=Field(...,alias="PREFIX_APP")
    database_url:str=Field(...,alias="DATABASE_URL")
    app_name:str=Field(...,alias="APP_NAME")

    
@lru_cache
def get_settings() -> Settings:
    return Settings()
