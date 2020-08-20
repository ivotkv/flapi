# Flapi

A minimal Flask API framework.

# Setup

You need to have Python 3 installed, as well as the PostgreSQL libraries and standard build utils, e.g.:

```sh
yum install python3 python3-devel postgresql-devel gcc-c++ make
```

Packages vary depending on OS, see [here](https://github.com/ivotkv/ops/blob/master/howtos/amazonlinux2.md) for Amazon Linux 2 instructions. Then build the virtual environment:

```sh
./build_venv.sh
```

## Virtual Environment

Before running any scripts or the server itself, always make sure you have your virtual environment activated:

```sh
source venv/bin/activate
```

## Configuration

Copy the `config.yaml.example` template to `config.yaml` and modify accordingly:

### app

* `secret_key`: the secret key used to encrypt session data. One way to generate it would be:

    ```python
    import secrets
    secrets.token_urlsafe(16)
    ```

### db

Provide your PostgreSQL connection details here.

## PostgreSQL

You will need to have a PostgreSQL server running, then create an appropriate user and database, e.g.:

```sql
CREATE USER flapi PASSWORD 'flapi';

CREATE DATABASE flapi ENCODING 'UTF8' OWNER flapi;

\c flapi

ALTER SCHEMA public OWNER TO flapi;
```

And initialise the tables using `./reset_db.py`:

```sh
./reset_db.py
```

If you later need to reset the database, just use the same script.

# Using the API

To start the Flask app, activate your `venv` and run:

```sh
./app.py
```

If all went well, <http://localhost:5000/status> should return `OK`.

Once you have the Flask app running, you should be able to access the REST API:

* <http://localhost:5000/user> - List all Users
* <http://localhost:5000/user/1> - User with id 1

You can provide GET params to filter by field, e.g.:

* <http://localhost:5000/user?first_name=Bob> - List all Users with first_name "Bob"

The standard `GET`, `POST`, `PUT` and `DELETE` operations are supported.

Note that model names are not pluralized.

# Development

## Adding and Changing Models

All models are defined in the `src/models/` directory. Any `.py` files created inside it will automatically be imported.

Models are defined using the [SQLAlchemy Declarative](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/) syntax and must extend `db.Model`.

The `db` object has references to common SQLAlchemy objects and functions, as well as other helpers to facilitate development.

If models also extend `CRUDable`, they will be made available via the REST API automatically.

## Database Migrations

To make changes to the schema, first make your changes in `src/models/` then run:

```sh
flask db migrate -m "Description of changes"
```

This will generate a script in `migrations/versions/`. Verify it then run:

```sh
flask db upgrade
```

## Adding Routes

Flask routes are defined in the `src/routes/` directory. Any `.py` files created inside it will automatically be imported.
