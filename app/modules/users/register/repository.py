from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.users.register.model import User
from sqlalchemy import Select

class UserRepository:
    def __init__(self,db:AsyncSession):
        self.db=db

    async def get_by_email(self,email:str) -> User|None:
        user = await self.db.execute(Select(User).where(User.email==email))
        return user.scalar_one_or_none()

    async def get_by_code(self,code:str) -> User|None:
        code_user = await self.db.execute(Select(User).where(User.code_user==code))
        return code_user.scalar_one_or_none()

    async def create(self,data:dict) -> User:
        user=User(**data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update(self,user:User,data:dict):
        for key,value in data.items():
            setattr(user,key,value)
        await self.db.commit()
        await self.db.refresh(user)
        return user