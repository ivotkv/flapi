#!/usr/bin/env python

import os
import sys

from src.models import db
from src.config import config

# confirm
if input('Reset database? [y/N] ').lower() != 'y':
    sys.exit()

db.engine.execute('''\
DROP SCHEMA public CASCADE;
CREATE SCHEMA public AUTHORIZATION {username};
COMMENT ON SCHEMA public IS 'standard public schema';
GRANT ALL ON SCHEMA public TO {username};
GRANT ALL ON SCHEMA public TO PUBLIC;
'''.format(username=config['db']['username']))

db.create_all()

os.system('flask db stamp')
