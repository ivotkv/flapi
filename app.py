#!/usr/bin/env python

import src.rest
import src.routes
from src.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
