from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from datetime import datetime

class TenantBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    slug: str = Field(..., description="Unique URL-friendly identifier")

class TenantCreate(TenantBase):
    pass

class TenantUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None

class Tenant(TenantBase):
    id: UUID
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
