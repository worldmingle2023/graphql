from pydantic import BaseModel
import strawberry

class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    region: str
    language: str
    culturetip: str
    localcustom: str

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True

@strawberry.type
class Country:
    name: str
    region: str
    language: str
    culturetip: str
    localcustom: str

@strawberry.input
class CountryInput:
    name: str
    region: str
    language: str
    culturetip: str
    localcustom: str