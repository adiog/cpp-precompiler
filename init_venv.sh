#!/bin/bash

function check()
{
    if ! which $1;
    then
        echo Install $1
        CHECK_FAILED=TRUE
    fi
}

function check_if_failed()
{
    if [[ -n "${CHECK_FAILED}" ]];
    then
        exit 1
    fi
}

if ! which clang-format;
then
    sudo apt install clang-format
fi

check virtualenv
check python3
check pip3
check_if_failed

if [[ ! -d venv ]];
then
    virtualenv -p python3 venv
fi

pushd $PWD
. ./venv/bin/activate
pip3 install antlr4-python3-runtime
popd
export PYTHONPATH=$PYTHONPATH:$PWD
export PATH=$PATH:$PWD
export WORKSPACE=$PWD
