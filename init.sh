#!/bin/bash

set -e
set -x

rm -rf venv
virtualenv --python=python3 venv
source venv/bin/activate

pip install --upgrade pip
pip install --upgrade setuptools
pip install ipython

pip install -r requirements.txt
