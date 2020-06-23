import os
from glob import glob
from importlib import import_module

for path in sorted(glob(os.path.dirname(__file__) + '/*.py')):
    module_name = path.split('/')[-1].split('.py')[0]
    if module_name != '__init__':
        module = import_module('.' + module_name, 'app.routes')
