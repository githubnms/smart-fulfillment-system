from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.inventory_service import get_inventory

router = APIRouter()

@router.get("/inventory")
def fetch_inventory(db: Session = Depends(get_db)):
    return get_inventory(db)