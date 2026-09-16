from pydantic import BaseModel,EmailStr
from datetime import datetime
from enum import Enum

class Sexe(str,Enum):
    male="Male"
    female="Female"

class Nation(str,Enum):
    madagascar="Madagascar"
    other="Other"

class UserRegister(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    password:str
    sexe:Sexe
    nation:str
    phone:str|None=None

class UserRead(BaseModel):
    model_config = {"from_attributes":True}
    first_name:str
    last_name:str
    email:EmailStr
    is_verified:bool
    sexe:Sexe
    nation:str
    phone:str|None
    created_at:datetime|None
    updated_at:datetime|None
    