#!/usr/bin/env python

import app.api
import app.routes
from app.app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
