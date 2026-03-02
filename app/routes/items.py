from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/items", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user)):
        db_item = models.Item(title=item.title, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item