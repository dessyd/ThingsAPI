from re import T
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
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
    boardid = Column(Integer,nullable=False)
    locationid = Column(Integer,nullable=False)

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
    
class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, nullable=False)
    boardid = Column(Integer, nullable=False)
    enabled = Column(Boolean, server_default='TRUE', nullable=False)
    type = Column(Integer, nullable=False)

class SensorType(Base):
    __tablename__ = "sensortypes"
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(String, nullable=False)
