#!/bin/bash

set -e
set -x

rm -rf venv
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install --upgrade setuptools
pip install ipython

pip install -r requirements.txt
