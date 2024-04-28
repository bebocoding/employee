from typing import Optional
from pydantic import UUID4, ConfigDict, BaseModel, EmailStr
from datetime import datetime

# Request Schema


class EmployeeCreate(BaseModel):
    username: str
    name: str
    department: str
    position: str
    password: str


class EmployeeOut(BaseModel):
    employee_id: UUID4
    username: str
    name: str
    department: str
    position: str


class TokenData(BaseModel):
    employee_id: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class EmployeeLocationCreate(BaseModel):
    latitude: float
    longitude: float
    image_path: str = None


class EmployeeLocationOut(BaseModel):
    location_id: UUID4
    latitude: float
    longitude: float
    timestamp: datetime
    image_path: str | None


class EmployeeLogin(BaseModel):
    username: str
    password: str
