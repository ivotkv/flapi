import os
from uuid import uuid4

from .app import app


@app.route("/status")
def status():
    return 'OK', 200
