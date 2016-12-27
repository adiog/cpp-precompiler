#!/bin/bash

# BASH_CLEANUP {{{
BASH_CLEANUP_FILE=`mktemp`
trap BASH_CLEANUP EXIT

function BASH_CLEANUP() {
  BASH_CLEANUP_FILE_REV=`mktemp`
  tac $BASH_CLEANUP_FILE > $BASH_CLEANUP_FILE_REV
  . $BASH_CLEANUP_FILE_REV
  rm $BASH_CLEANUP_FILE $BASH_CLEANUP_FILE_REV
}

function BASH_FINALLY() {
  echo "$*" >> $BASH_CLEANUP_FILE
}

function BASH_MKTEMP() {
  BASH_TMP=`mktemp`
  echo "rm $BASH_TMP" >> $BASH_CLEANUP_FILE
  echo $BASH_TMP
}

function BASH_MKTEMP_DIR() {
  BASH_TMP=`mktemp -d`
  echo "rm -fr $BASH_TMP" >> $BASH_CLEANUP_FILE
  echo $BASH_TMP
}
# }}}

WRAPPED_ARGS=""

for arg in $*;
do
    if [[ $arg == *.cc ]];
    then
        coarg=${arg/.cc/.co.cc}
        ./precompile.sh $arg $coarg
        #BASH_FINALLY "rm $coarg"
    else
        coarg=$arg
    fi

    if [[ $arg == -std* ]];
    then
        STD_PRESENT=true
    fi
    if [[ $arg == -lpthread ]];
    then
        LPTHREAD_PRESENT=true
    fi

    WRAPPED_ARGS="$WRAPPED_ARGS $coarg"
done

if [[ -z "$STD_PRESENT" ]];
then
    echo "missing -std= specifier ..."
    exit 1
fi

if [[ -z "$LPTHREAD_PRESENT" ]];
then
    echo "missing -lpthread ..."
    exit 1
fi

g++ $WRAPPED_ARGS
