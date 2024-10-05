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

## Try it out

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
curl -X POST http://localhost:8000/stocks \
  -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "name": "NVDA", "price": 111.5 }'
curl -X POST http://localhost:8000/stocks \
  -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "name": "AAPL", "price": 222.8 }'

curl -X GET http://localhost:8000/stocks/1
curl -X GET http://localhost:8000/stocks/2
```

or add in pgadmin:

```sql
INSERT INTO stocks VALUES (1, 'NVDA', 111.5);
INSERT INTO stocks VALUES (2, 'AAPL', 222.8);

SELECT * FROM stocks;
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

### Basic

* [FastAPI - SQL (Relational) Databases](https://fastapi.tiangolo.com/id/tutorial/sql-databases/?h=postgres)
  * [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)
* [Postgresql & PgAdmin powered by compose](https://github.com/khezen/compose-postgres)
* [Docker-compose創建PostgreSQL](https://cde566.medium.com/docker-compose%E5%89%B5%E5%BB%BApostgresql-7f3f9519fa20)
* [FastAPI + SQLAlchemy+PostgreSQL — FastAPI的ORM](https://medium.com/@King610160/fastapi-sqlalchemy-postgresql-fastapi%E7%9A%84orm-00818bc63106)
* [Creating a Simple Task CRUD App with FastAPI, PostgreSQL, SQLAlchemy, and Docker](https://plainenglish.io/blog/creating-a-simple-task-crud-app-with-fastapi-postgresql-sqlalchemy-and-docker)
* [Dockerizing FastAPI and PostgreSQL Effortless Containerization: A Step-by-Step Guide](https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb)

### Advanced

* [minimal-fastapi-postgres-template](https://github.com/androchentw/minimal-fastapi-postgres-template)
* [fastapi-beyond-CRUD](https://github.com/jod35/fastapi-beyond-CRUD)
* [DevOps with Fast API & PostgreSQL: How to containerize Fast API Application with Docker](https://dev.to/mbuthi/devops-with-fast-api-postgresql-how-to-containerize-fast-api-application-with-docker-1jdb)
* [Async Web REST API with FastAPI + SQLAlchemy 2.0 Postgres ORM + Docker + Pytest + Alembic](https://github.com/reinhud/async-fastapi-postgres-template)
* [Pytest API Testing Masterclass with FastAPI, Postgres and SQLAlchemy - 2 Part Series](https://github.com/Pytest-with-Eric/api-testing-masterclass)

### GCP

* [Connect to Cloud SQL for PostgreSQL from Cloud Run](https://cloud.google.com/sql/docs/postgres/connect-instance-cloud-run)
* [cloud-sql-python-connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)
  * FastAPI + SQLAlchemy ORM
  * Async Driver Usage: asyncpg (Postgres)
  * pg8000
  * [cloud-sql-fastapi](https://github.com/jackwotherspoon/cloud-sql-fastapi/tree/main)
* [Cloud Run, Cloud SQL, Terraform Pgvector (FastAPI Your Data — Episode 6)](https://medium.com/@saverio3107/connecting-cloud-run-with-cloud-sql-using-terraform-fastapi-your-data-episode-6-8673812e3941)
  * [fastapi-your-data](https://github.com/androchentw/fastapi-your-data)
* [How to Connect a FastAPI Server to PostgreSQL and Deploy on GCP Cloud Run](https://glenn-viroux.medium.com/how-to-connect-a-fastapi-server-to-postgresql-and-deploy-on-gcp-cloud-run-4950af0e2e44)
