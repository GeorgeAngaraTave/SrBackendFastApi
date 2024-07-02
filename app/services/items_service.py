from app.schemas.items_schemas import ItemCreate, ItemResponse
from app.repositories.item_repository import create_item, get_items
from sqlalchemy.orm import Session
from typing import List

async def create_item_service(item: ItemCreate, db: Session) -> ItemResponse:
    return await create_item(item, db)

async def get_items_service(db: Session) -> List[ItemResponse]:
    return await get_items(db)