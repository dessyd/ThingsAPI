from typing import List, Optional
from sqlalchemy.sql.roles import GroupByRole

from starlette.status import HTTP_403_FORBIDDEN
from .. import schema, model
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db

router = APIRouter( 
    prefix="/locations",
    tags=['Locations']
)

@router.get("/", response_model=List[model.LocationOut])
# @router.get("/")

def get_locations(db: Session = Depends(get_db),
                  limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    locations = db.query(schema.Location).filter(schema.Location.name.contains(search)).limit(limit).offset(skip).all()

    return locations