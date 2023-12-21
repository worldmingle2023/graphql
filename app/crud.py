from sqlalchemy.orm import Session
from typing import Optional

from .models import Country as CountryModel

def get_country_info(db: Session, name: str):
    return db.query(CountryModel).filter(CountryModel.name == name).first()

def delete_country(db: Session, name: str) -> bool:
    country = db.query(CountryModel).filter(CountryModel.name == name).first()
    if country:
        db.delete(country)
        db.commit()
        return True
    else:
        return False

def update_country(db: Session, name: str, region: str = None, language: str = None, culturetip: str = None, localcustom: str = None) -> Optional[CountryModel]:
    country = db.query(CountryModel).filter(CountryModel.name == name).first()
    if country:
        if region is not None:
            country.region = region
        if language is not None:
            country.language = language
        if culturetip is not None:
            country.culturetip = culturetip
        if localcustom is not None:
            country.localcustom = localcustom
        db.commit()
        return country
    else:
        return None