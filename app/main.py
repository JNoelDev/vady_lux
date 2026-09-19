from fastapi import FastAPI
from app.core.config import get_settings
from app.modules.users.register.router import router as register_router

settings=get_settings()

app=FastAPI(
    title="VADY-LUX APIS",
    docs_url=f"{settings.prefix_app}/docs" if settings.environment=="production" else None,
    redoc_url=f"{settings.prefix_app}/redoc" if settings.environment=="production" else None,
)

app.include_router(register_router,prefix=settings.prefix_app)

