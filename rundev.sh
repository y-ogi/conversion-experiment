#!/usr/bin/env bash

PYTHON_BIN=/usr/bin/python2.5

$PYTHON_BIN manage.py runserver -a 0.0.0.0 -p 8000 --high_replication --datastore_path=.datastore 
