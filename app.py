import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

@strawberry.type
class User:
    name: str
    age: int


#@strawberry.type
#class Query:
#    @strawberry.field
#    def user(self) -> User:
#        return User(name="Patrick", age=100)

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)