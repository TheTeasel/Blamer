#!/bin/bash

# Check is torsocks is installed
if ! command -v torsocks on &> /dev/null
then
    # If it's not then ask the user to install it
    echo "Torsocks could not be found! Please install the torsocks package."
    exit
fi

# If torsocks is installed then disable it
source torsocks off