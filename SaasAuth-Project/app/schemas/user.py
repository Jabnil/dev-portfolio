from pydantic import BaseModel, EmailStr, ConfigDict, Field
from uuid import UUID
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    org_id: UUID

class UserUpdate(BaseModel):
    password: Optional[str] = None
    full_name: Optional[str] = None

class User(UserBase):
    id: UUID
    org_id: UUID
    permissions: List[str] = []

    model_config = ConfigDict(from_attributes=True)
