#!/bin/bash

if [[ ! -d venv ]];
then
    virtualenv venv
    pip install antlr4-python3-runtime
fi
. ./venv/bin/activate