from flask import Flask
from flask_cors import CORS

from .config import config

app = Flask(__name__)

app.secret_key = config['app']['secret_key']

dburi = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(**config['db'])
app.config.update(
    {
        'SQLALCHEMY_DATABASE_URI': dburi,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }
)

CORS(app, supports_credentials=True)
