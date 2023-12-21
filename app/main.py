import strawberry
from fastapi import FastAPI, Depends
from strawberry.asgi import GraphQL
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
from sqlalchemy.orm import Session

from .models import Country as CountryModel
from .schemas import Country, CountryInput
from .dependencies import get_db
from .crud import get_country_info, delete_country, update_country
from .database import SessionLocal

app = FastAPI()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def post_country_info(self, country_input: CountryInput) -> Optional[Country]:
        with SessionLocal() as db:
            new_country = CountryModel(
                name=country_input.name, 
                region=country_input.region, 
                language=country_input.language, 
                culturetip=country_input.culturetip, 
                localcustom=country_input.localcustom
            )
            db.add(new_country)
            db.commit()
            db.refresh(new_country)
            return Country(
                name=new_country.name, 
                region=new_country.region, 
                language=new_country.language,
                culturetip=new_country.culturetip,
                localcustom=new_country.localcustom
            )

    @strawberry.mutation
    def delete_country(self, name: str) -> bool:
        with SessionLocal() as db:
            return delete_country(db, name)

    @strawberry.mutation
    def update_country(self, name: str, region: Optional[str] = None, language: Optional[str] = None, culturetip: Optional[str] = None, localcustom: Optional[str] = None) -> Optional[Country]:
        with SessionLocal() as db:
            updated_country = update_country(db, name, region, language, culturetip, localcustom)
            if updated_country:
                return Country(name=updated_country.name, region=updated_country.region, language=updated_country.language, culturetip=updated_country.culturetip, localcustom=updated_country.localcustom)
            else:
                return None


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"


    @strawberry.field
    def get_country_info(self, name: str) -> Country:
        with SessionLocal() as db:
            country_model = get_country_info(db, name)
            if country_model is None:
                return None
            return Country(name=country_model.name, region=country_model.region, language=country_model.language, culturetip=country_model.culturetip, localcustom=country_model.localcustom)

    # @strawberry.field
    # def get_culture_tips(self, country_name: str) -> List[CultureTip]:
    #     # Fetch culture tips for a specific country
    #     pass

    # @strawberry.field
    # def get_local_customs(self, country_name: str) -> List[LocalCustom]:
    #     # Fetch local customs for a specific country
    #     pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)