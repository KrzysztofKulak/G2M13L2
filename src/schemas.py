from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, EmailStr


class TagIn(BaseModel):
    name: str = Field(max_length=25)


class TagOut(TagIn):
    id: int

    class Config:
        orm_mode = True


class NoteIn(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150)
    done: bool | None
    tags: List[int] | None


class NoteOut(NoteIn):
    id: int
    created_at: datetime
    tags: List[TagOut]

    class Config:
        orm_mode = True


class NoteStatusUpdate(BaseModel):
    done: bool


class UserIn(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserCreated(BaseModel):
    user: UserOut
    detail: str = "User successfully created"


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr
