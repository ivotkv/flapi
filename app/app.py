from flask import Flask
from flask_cors import CORS

from .config import config

app = Flask(__name__)
app.config.update(
    {
        "SQLALCHEMY_DATABASE_URI": config["db"]["uri"],
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
)
CORS(app)
