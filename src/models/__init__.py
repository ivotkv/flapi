import os
from glob import glob
from importlib import import_module

from ..db import db

__all__ = ['db']

for path in sorted(glob(os.path.dirname(__file__) + '/*.py')):
    module_name = path.split('/')[-1].split('.py')[0]
    if module_name != '__init__':
        module = import_module('.' + module_name, 'src.models')
        for name in dir(module):
            value = getattr(module, name)
            if isinstance(value, type) and issubclass(value, db.Model):
                locals()[name] = value
                __all__.append(name)
