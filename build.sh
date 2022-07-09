#!/bin/bash

if (); then
    echo "No bitches?"
    read placeholder
fi

pyinstaller -F --clean src/RATT.py
rm -rf build/RATT
mv dist/RATT build/RATT