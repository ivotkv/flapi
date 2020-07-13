import yaml
from os.path import abspath, dirname, join

WORKING_DIR = dirname(dirname(abspath(__file__)))
CONFIG_FILE = join(WORKING_DIR, 'config.yaml')

with open(CONFIG_FILE, 'r') as f:
    config = yaml.safe_load(f.read())
