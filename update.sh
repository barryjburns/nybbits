#!/bin/bash

git pull;
pushd .;
cd www/static;
./prep.sh;
popd;
python3 manage.py collectstatic;

