from sqlalchemy.orm import Session
from app.models.items import Item
from app.schemas.items_schemas import ItemCreate, ItemResponse
from typing import List

async def create_item(item: ItemCreate, db: Session) -> ItemResponse:
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def get_items(db: Session) -> List[ItemResponse]:
    return db.query(Item).all()