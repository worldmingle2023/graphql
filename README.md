## Requirements
pip install fastapi uvicorn

pip install "strawberry-graphql[debug-server]"

## Run
uvicorn app.main:app --reload #then navigate to [http://127.0.0.1:8000/graphql ](http://127.0.0.1:8000/graphql)

alembic revision --autogenerate -m "Description of changes"

alembic upgrade head


## Docs
https://fastapi.tiangolo.com/how-to/graphql/

https://github.com/strawberry-graphql/strawberry

https://strawberry.rocks

## Test
```python
Post:
mutation PostCountryInfo($input: CountryInput!) {
  postCountryInfo(countryInput: $input) {
    name
    region
    language
    culturetip
    localcustom
  }
}
{
  "input": {
    "name": "Sample Country",
    "region": "Sample Region",
    "language": "Sample Language",
    "culturetip": "Sample Culture Tip",
    "localcustom": "Sample Local Custom"
  }
}

Get:
{
  getCountryInfo(name: "Sample Country") {
    name
  }
}

Get (pagination):
{
  listCountries(skip: a, limit: b) {
    countries {
      name
      region
    }
    retrievedCount
    remainingCount
  }
}

Delete:
mutation {
  deleteCountry(name: "CountryName") 
}

Put:
mutation {
  updateCountry(name: "CountryName", region: "NewRegion", language: "NewLanguage", culturetip: "NewCultureTip", localcustom: "NewLocalCustom") {
    name
    region
    language
    culturetip
    localcustom
  }
}
