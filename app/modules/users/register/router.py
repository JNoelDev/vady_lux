from fastapi import APIRouter,status,Depends
from app.modules.users.register.schema import UserRead,UserRegister
from app.modules.users.register.service import UserService
from app.modules.users.register.repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router=APIRouter(prefix="/users",tags=["/users"])


def _get_service(db:AsyncSession=Depends(get_db)) -> UserService:
    repo=UserRepository(db)
    return UserService(repo)

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Regiser for user",
    response_model=UserRead
)
async def register(payload:UserRegister,service:UserService=Depends(get_db)):
    user= await service.register(payload)
    return UserRead.model_validate(user)