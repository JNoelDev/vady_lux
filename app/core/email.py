from fastapi_mail import (
    FastMail,MessageSchema,MessageType,ConnectionConfig
)
from app.core.config import get_settings

settings=get_settings()

mail_enabled=(
    settings.enable_mail_notification
)

if mail_enabled:
    mail_config=ConnectionConfig(
        MAIL_USERNAME=settings.mail_username,
        MAIL_PASSWORD=settings.mail_password,
        MAIL_FROM=settings.mail_from,
        MAIL_PORT=settings.mail_port,
        MAIL_SERVER=settings.mail_server,
        MAIL_FROM_NAME=settings.mail_from_name,
        MAIL_STARTTLS=settings.mail_starttls,
        MAIL_SSL_TLS=settings.mail_ssl_tls,
        MAIL_CREDENTIALS=settings.mail_credentials,
        VALIDATE_CERTS=settings.validate_certs,
        DOMAIN=settings.domain
    )

    fastapi_mail=FastMail(mail_config)

else:
    fastapi_mail=None

def create_message(recipients:str,subject:str,body:str) -> MessageSchema:
    return MessageSchema(
        recipients=recipients,subject=subject,body=body,subtype=MessageType.html
    )

async def send_message(recipients:str,subject:str,body:str) -> bool:
    if fastapi_mail is None:
        return False
    message=create_message(
        recipients,subject,body
        )
    await fastapi_mail.send_message(message)
    return True