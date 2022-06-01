from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    role: int
    is_active: bool = Field(False)

    class Config:
        orm_mode = True

class UserCreate(User):
    ...

class UserLogin(BaseModel):
    email: EmailStr
    password: str