from app.modules.users.register.repository import UserRepository
from app.modules.users.register.schema import UserRegister,UserRead
from fastapi import HTTPException,status
from app.core.security import hash_password
import secrets
_CODE_ATTEMPS=5

def verification_code() -> str:
    return f"{secrets.randbelow(1_000_000):06d}"

class UserService:
    def __init__(self,repo:UserRepository):
        self.repo=repo

    async def generate_code(self):
        code_user:str|None=None
        for _ in range(_CODE_ATTEMPS):
            candidate=verification_code()
            code = await self.repo.get_by_code(candidate)
            if not code:
                code_user=candidate
                break

        if code_user is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Impossible to generate code"
            )

    async def create_user(self,data:UserRegister):
        user = await self.repo.create(
            {
                "first_name":data.first_name,
                "last_name":data.last_name,
                "email":data.email,
                "password":hash_password(data.password),
                "sexe":data.sexe,
                "nation":data.nation,
                "phone":data.phone
            }
        )

    async def register(self,payload:UserRegister):
        verify_email = await self.repo.get_by_email(payload.email)
        if verify_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,detail="Email has already registered"
            )

        code = await self.generate_code()


        

        

        