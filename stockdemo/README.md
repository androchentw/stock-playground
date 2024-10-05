# stockdemo

## Setup

```sh
pip3 install -r requirements.txt

# poetry config virtualenvs.in-project true
# poetry init 
# poetry add $(cat requirements.txt)
# poetry install
# poetry env info --path
```

```sh
# API Doc: http://127.0.0.1:8000/docs
# Endpoint: http://127.0.0.1:8000/stocks/1

# Run way 1: simply run the server
uvicorn main:app --reload

# Run way 2: docker compose way
docker compose -f docker-compose.yml --env-file=.env up -d
docker compose -f docker-compose.yml --env-file=.env down # -v
# docker-compose down --remove-orphans

# tag
docker tag stockdemo androchentw/stockdemo:1.0.0-dev
docker push androchentw/stockdemo:1.0.0-dev

# clean up
docker rm $(docker ps --filter status=exited -q)
docker rmi $(docker images -f "dangling=true" -q)
```

```text

├───app
│   ├───api
│   │   ├───dependencies        # FastAPI dependency injection 
│   │   └───routes              # endpoint definintions
│   ├───core                    # settings
│   ├───db
│   │   ├───models              # SQLAlchemy models
│   │   └───repositories        # CRUD related stuff
│   ├───models                  
│   │   ├───domain              # schemas related to domain entities
│   │   └───utility_schemas     # schemas for other validation
│   └───services                # not just CRUD related stuff
├───migrations
│   └───versions
└───tests
    ├───fixtures                # where test specific fixtures live
    └───unit_tests                
        └───test_api            # testing endpoints

stockdemo/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   ├── database.py
│   └── schemas.py
│
├── tests/
│   ├── __init__.py
│   ├── test_stock.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── pytest.ini
```

## Access

* API Docs
  * Swagger: [http://localhost:8000/docs]
  * ReDoc: [http://localhost:8000/redoc]
* pgadmin: [http://localhost:5050]
  * `pgadmin4@pgadmin.org` / `admin`
  * Register server (ref .env)
    * Name: `postgres_db`
    * Connection: `postgres`    // same as specified in docker-compose-yml services.`postgres`
    * Username: `postgres`
    * Password: `changeme`

```sh
curl http://localhost:8000/stocks \
  -X POST -H 'Content-Type: application/json' \
  -d '{ "name": "NVDA", "price": 100.5 }'

curl http://localhost:8000/stocks/1
```

or add in pgadmin:

```sql
INSERT INTO stocks VALUES (1, 'NVDA', 100.5);

SELECT * FROM stocks
```

## SQL

```sql
SHOW data_directory;

# docker cp postgres_data/test.csv postgres:/var/lib/postgresql/data

# import table 
COPY public."MyData" FROM '/var/lib/postgresql/data/test.csv' DELIMITER ',' CSV HEADER;  
#show table 
SELECT * FROM public."MyData";
```

## Ref

* [Creating a Simple Task CRUD App with FastAPI, PostgreSQL, SQLAlchemy, and Docker](https://plainenglish.io/blog/creating-a-simple-task-crud-app-with-fastapi-postgresql-sqlalchemy-and-docker)
* [Dockerizing FastAPI and PostgreSQL Effortless Containerization: A Step-by-Step Guide](https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb)
* [DevOps with Fast API & PostgreSQL: How to containerize Fast API Application with Docker](https://dev.to/mbuthi/devops-with-fast-api-postgresql-how-to-containerize-fast-api-application-with-docker-1jdb)
* [Postgresql & PgAdmin powered by compose](https://github.com/khezen/compose-postgres)
* [Async Web REST API with FastAPI + SQLAlchemy 2.0 Postgres ORM + Docker + Pytest + Alembic](https://github.com/reinhud/async-fastapi-postgres-template)
* [Docker-compose創建PostgreSQL](https://cde566.medium.com/docker-compose%E5%89%B5%E5%BB%BApostgresql-7f3f9519fa20)
