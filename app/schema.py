from re import T
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

# A thing, the physical object is made of 
# a Board, 
# zero or more Sensor(s) 
# zero or more Actuator(s)
# and pysicallly located at Location
class Thing(Base):
    __tablename__ = "things"
    id = Column(Integer, primary_key=True, nullable=False)
    physical_id = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    board_id = Column(Integer, ForeignKey("boards.id", ondelete="CASCADE"), nullable=False)
    board = relationship("Board")
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="CASCADE"),nullable=False)
    location = relationship("Location")

# A Board is the generic description
class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, nullable=False)   
    name = Column(String, nullable=True)

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, nullable=False)  
    name = Column(String, nullable=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()')) 
    
class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, nullable=False)
    enabled = Column(Boolean, server_default='TRUE', nullable=False)
    board_id = Column(Integer, ForeignKey("boards.id", ondelete="CASCADE"), nullable=False)  
    board = relationship("Board")  
    type_id = Column(Integer, ForeignKey("sensortypes.id", ondelete="CASCADE"),nullable=False)
    type = relationship("SensorType")

class SensorType(Base):
    __tablename__ = "sensortypes"
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(String, nullable=False)
