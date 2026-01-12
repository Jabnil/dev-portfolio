from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List

class PermissionBase(BaseModel):
    codename: str
    description: str

class RoleBase(BaseModel):
    name: str
    permissions: List[str] # List of codenames

class RoleCreate(RoleBase):
    org_id: UUID

class Role(RoleBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)
