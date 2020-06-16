#!/bin/bash

set -e
set -x

rm -rf venv
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install --upgrade setuptools
pip install ipython
pip install flake8

if [ -d /usr/local/opt/openssl/lib ]; then
    export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
fi

pip install -r requirements.txt
