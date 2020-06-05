# Flask App

Boilerplate for a basic Flask app.

## Setup
```sh
./init.sh
```

## PostgreSQL
You will need to have a PostgreSQL server running, then create an appropriate user and database:
```sql
CREATE USER username PASSWORD 'password';

CREATE DATABASE dbname ENCODING 'UTF8' OWNER username;

\c dbname

ALTER SCHEMA public OWNER TO username;
```
And initialise the tables tables from Python:
```python
from app.db import db

db.create_all()
```
If you later need to reset the database, just drop the PostgreSQL schema:
```sql
\c dbname

DROP SCHEMA public CASCADE;

CREATE SCHEMA public AUTHORIZATION username;

COMMENT ON SCHEMA public IS 'standard public schema';

GRANT ALL ON SCHEMA public TO username;

GRANT ALL ON SCHEMA public TO PUBLIC;
```
And re-initialise from Python as above.

## Using the API

Run the Flask app:
```sh
./server.py
```

### REST
Once you have the Flask app running, you should be able to access the REST API at locahost port 5000:
* http://localhost:5000/model1 - List all Model1s
* http://localhost:5000/model1/1 - Model1 with id 1

You can provide GET params to filter by relationship ID, e.g.:
* http://localhost:5000/model2?model1_id=1 - List all Model2s for Model1 with ID 1
