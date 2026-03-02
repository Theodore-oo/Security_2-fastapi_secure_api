from pydantic import BaseModel

class UserCreate(BaseModel):
        username: str
        password: str

class UserResponse(BaseModel):
        id: int
        username: str
        role: str

        class Config:
                from_attributes = True

class Token(BaseModel):
        access_token: str
        token_type: str

class ItemCreate(BaseModel):
        title: str
        description: str

class ItemResponse(BaseModel):
        id: int
        title: str
        description: str

        class Config: 
                from_attributes = True