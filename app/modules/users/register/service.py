from app.modules.users.register.repository import UserRepository
from app.modules.users.register.schema import UserRegister,UserRead
from app.modules.users.register.model import User
from app.core.email import send_email
from fastapi import HTTPException,status
from app.core.security import hash_password
import secrets
_CODE_ATTEMPS=5

def _code() -> str:
    return f"{secrets.randbelow(1_000_000):06d}"

class UserService:
    def __init__(self,repo:UserRepository):
        self.repo=repo

    async def generate_code(self):
        code_user:str|None=None
        for _ in range(_CODE_ATTEMPS):
            candidate=_code()
            code = await self.repo.get_by_code(candidate)
            if not code:
                code_user=candidate
                break

        if code_user is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Impossible to generate code"
            )
        return code_user

    async def create_user(self,data:UserRegister) -> User:
        user_data = {
            "first_name":data.first_name,
            "last_name":data.last_name,
            "email":data.email,
            "password":hash_password(data.password),
            "sexe":data.sexe,
            "nation":data.nation,
            "phone":data.phone
        }
        return await self.repo.create(user_data)
        
    async def send_a_mail(self,code:str,email:str) -> bool:
        html=f"Please enter this code {code}"
        subject="Code vérification"
        return await send_email([email],subject,html)


    async def register(self,payload:UserRegister) -> UserRead|None:
        verify_email = await self.repo.get_by_email(str(payload.email))
        if verify_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,detail="Email has already registered"
            )
        
        user =await self.create_user(payload)
        code= await self.generate_code()
        print(f"{code}")
        send=await self.send_a_mail(code,user.email)
        if send:
            return await self.repo.update(
                user,{"code_user":code}
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Impossible to send a mail"
            )

            
        
        
        



        

        

        