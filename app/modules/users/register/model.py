from app.db.base import Base
from app.shared.model.base import UUIDSTampz
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Boolean
from app.modules.users.register.schema import Sexe,Nation

class User(Base,UUIDSTampz):

    __tablename__ = "users"

    first_name:Mapped[str]=mapped_column(String(20),nullable=False,index=True)

    last_name:Mapped[str]=mapped_column(String(20),nullable=False,index=True)

    email:Mapped[str]=mapped_column(String(50),unique=True,nullable=False,index=True)

    password:Mapped[str]=mapped_column(String(250),nullable=False)

    is_verified:Mapped[bool]=mapped_column(Boolean,nullable=False,default=False)

    sexe:Mapped[Sexe]=mapped_column(String(20),nullable=False)

    code_use:Mapped[str|None]=mapped_column(String(10),nullable=True,unique=True,index=True)

    nation:Mapped[Nation]=mapped_column(String(50),nullable=False)

    phone:Mapped[str|None]=mapped_column(String(20),nullable=True)