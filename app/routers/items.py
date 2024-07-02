from fastapi import APIRouter, Depends
from app.schemas.items_schemas import ItemCreate, ItemResponse
from app.services.items_service import create_item_service, get_items_service
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return await create_item_service(item, db)

@router.get("/", response_model=List[ItemResponse])
async def get_items(db: Session = Depends(get_db)):
    return await get_items_service(db)