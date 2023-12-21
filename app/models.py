from sqlalchemy import Column, Integer, String
from .database import Base

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    region = Column(String)
    language = Column(String)
    culturetip = Column(String)
    localcustom = Column(String)
