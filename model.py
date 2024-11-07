from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum



class Gender(str, Enum):
    male = "male"
    female = "female"

class Roles(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id:Optional[UUID] = uuid4()
    first_name :str
    last_name : str
    gender: Gender
    role: List[Roles]


class UserUpdateRequest(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    role: Optional[List[Roles]] =None
