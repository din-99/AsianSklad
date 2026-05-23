from pydantic import BaseModel
from typing import Optional

# Товары
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    image_url: Optional[str] = None
    model_config = {"from_attributes": True}
# Пользователи
class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str

class UserOut(BaseModel):
    id: int
    email: str
    full_name: str
    model_config = {"from_attributes": True}

# Токен
class Token(BaseModel):
    access_token: str
    token_type: str

class CategoryOut(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True}