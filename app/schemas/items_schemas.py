from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemResponse(ItemCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True