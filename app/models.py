from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#
# Locations
#

class LocationBase(BaseModel):
    name: Optional[str] = "-"
    lat: float
    lon: float

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationOut(LocationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
