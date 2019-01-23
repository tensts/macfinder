#!/bin/bash

if [ "$1" = "" ]; then
    echo "Usage ./runtest.sh interface"
    exit 1
fi
sudo ./macfinder-test.py $1
