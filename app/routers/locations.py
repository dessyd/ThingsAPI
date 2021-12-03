import datetime
from typing import List, Optional

from fastapi import  status, HTTPException, Depends, APIRouter, Response

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql.roles import GroupByRole

from .. import models, schemas
from ..database import get_db

router = APIRouter( 
    prefix="/locations",
    tags=['Locations']
)

@router.get("/", response_model=List[models.LocationOut])

def get_all_locations(db: Session = Depends(get_db),
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

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(id: int, db: Session = Depends(get_db)):

    location = db.query(schemas.Location).filter(schemas.Location.id == id)
    first_location = location.first()

    if first_location == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Location with id: {id} does not exeist")

    location.delete(synchronize_session=False)
    db.commit()

    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    return

@router.put("/{id}", response_model=models.LocationOut)
def update_location(id: int, location: models.LocationUpdate , db: Session = Depends(get_db)):

    location_query = db.query(schemas.Location).filter(schemas.Location.id == id)
    first_location = location_query.first()

    if first_location  == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Location with id: {id} does not exeist")
    
    #
    # Update timestamp
    #
    location_dict = location.dict()
    location_dict['created_at'] = datetime.datetime.now()

    location_query.update(location_dict, synchronize_session=False)
    db.commit()

    # return location.first()
    return first_location