from functools import lru_cache
from pydantic_settings import SettingsConfigDict,BaseSettings
from pydantic import Field
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.getenv("ENV",".env"),extra="ignore")

    environment:str=Field(...,alias="ENVIRONMENT")
    prefix_app:str=Field(...,alias="PREFIX_APP")
    database_url:str=Field(...,alias="DATABASE_URL")
    app_name:str=Field(...,alias="APP_NAME")

    mail_username:str=Field(...,alias="MAIL_USERNAME")
    mail_password:str=Field(...,alias="MAIL_PASSWORD")
    mail_from:str=Field(...,alias="MAIL_FROM")
    mail_port:str=Field(...,alias="MAIL_PORT")
    mail_server:str=Field(...,alias="MAIL_SERVER")
    mail_from_name:str=Field(...,alias="MAIL_FROM_NAME")
    mail_starttls:bool=Field(...,alias="MAIL_STARTTLS")
    mail_ssl_tls:bool=Field(...,alias="MAIL_SSL_TLS")
    mail_credentials:bool=Field(...,alias="MAIL_CREDENTIALS")
    validate_certs:bool=Field(...,alias="VALIDATE_CERTS")
    domain:str=Field(...,alias="DOMAIN")
    enable_mail_notification:bool=Field(...,alias="ENABLE_MAIL_NOTIFICATION")
    
@lru_cache
def get_settings() -> Settings:
    return Settings()
