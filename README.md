# Flask App

Boilerplate for a basic Flask app.

## Setup

You need to have Python 3 installed, as well as the PostgreSQL libraries and standard build utils, e.g.:

```sh
yum install postgresql-devel gcc-c++ make
```

Packages vary depending on OS, e.g. you might need to just install `postgresql`. Then build the virtual environment:

```sh
./init.sh
```

## PostgreSQL

You will need to have a PostgreSQL server running, then create an appropriate user and database, e.g.:

```sql
CREATE USER flaskapp PASSWORD 'flaskapp';

CREATE DATABASE flaskapp ENCODING 'UTF8' OWNER flaskapp;

\c flaskapp

ALTER SCHEMA public OWNER TO flaskapp;
```

And initialise the tables using `./reset_db.py`:

```sh
./reset_db.py
```

If you later need to reset the database, just use the same script.

## Using the API

Run the Flask app:

```sh
./server.py
```

### REST

Once you have the Flask app running, you should be able to access the REST API at locahost port 5000:

* <http://localhost:5000/user> - List all Users
* <http://localhost:5000/user/1> - User with id 1

You can provide GET params to filter by relationship ID, e.g.:

* <http://localhost:5000/user?company_id=1> - List all Users for Company with ID 1
