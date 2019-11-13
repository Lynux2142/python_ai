#!/bin/bash

PY_VERSION=`python -V | cut -c 8-`
if [[  $PY_VERSION == "3.7.4" ]]
then
	python setup.py sdist bdist_wheel
else
	echo "Python version must be 3.7.4 actualy is $PY_VERSION"
fi
