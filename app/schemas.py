from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Request Schema


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

# Response Schema


class Post(PostBase):
    owner_id: int
    id: int
    created_at: datetime
    owner: UserOut

    class Config:
        orm_mode = True  # for pydantic to accept orm types


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True  # for pydantic to accept orm types


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: bool
