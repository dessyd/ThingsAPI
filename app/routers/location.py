from typing import List, Optional
from sqlalchemy.sql.roles import GroupByRole

from starlette.status import HTTP_403_FORBIDDEN
from .. import models, schemas
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db

router = APIRouter( 
    prefix="/locations",
    tags=['Locations']
)

@router.get("/", response_model=List[models.LocationOut])

def get_locations(db: Session = Depends(get_db),
                  limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    locations = db.query(schemas.Location).filter(schemas.Location.name.contains(search)).limit(limit).offset(skip).all()

    return locations

@router.get("/{id}", response_model=models.LocationOut)
# @router.get("/{id}")
def get_location(id: int, db: Session = Depends(get_db)):

    location = db.query(schemas.Location).filter(schemas.Location.id == id).first()

    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Location with id: {id} is unknown")

    return location

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=models.LocationOut)
def create_location(location: models.LocationCreate, db: Session = Depends(get_db)):

    new_location = schemas.Location(**location.dict())
    #
    # Should add logic to avoid duplicate locations
    #
    db.add(new_location)
    db.commit()
    db.refresh(new_location)

    return new_location