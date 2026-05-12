from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    """Base user schema with common fields"""
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """Schema for creating a new user (registration)"""
    password: str


class UserResponse(BaseModel):
    """Schema for user response (safe to return to client)"""
    id: int
    username: str
    email: str
    avatar_url: str | None = None
    status: str
    is_online: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Allows converting SQLAlchemy models


class UserLogin(BaseModel):
    """Schema for user login"""
    username: str
    password: str


class Token(BaseModel):
    """Schema for token response"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"