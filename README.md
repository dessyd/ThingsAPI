# ThingsAPI

The project is self contained in a `docker-compose` file.

To start it do the following

```bash
docker compose up -d
```

This will launch the various components.

## Database initialization

The first time the database engine is started, only the project database is created but with no schema.

To create the various tables and their relationships, `alembic`comes to the rescue:

```bash
# Create the DDL
alembic revision --autogenerate -m "Creating db schema”
# Apply it
alembic upgrade head  
```

This can be verified by logging in `adminer` on http://localhost:8080 and selecting the Postgres database driver.

## Accessing the application

All API calls should be made to http://localhost:8000

## APIs documentation

The list of all APIs is available at http://locahost:8000/docs or http://localhost:8000/redoc depending on your documentation format choice.