#!bin/bash

# Parses the latitudes and longitudes given in a file and sends them to
# the Google Maps' API

coordfile=$1

# Commands to be used:

# Split large file into others:
# split <file> -n 349 <prefix>

# For <split file>:
content=$(cat <split file> | awk '{print $(NF-1), "|", $NF}'} | paste -s -d '|')

# Get JSON file:
jsonoutput=$(curl https://roads.googleapis.com/v1/snapToRoads?path=$content&interpolate=true&key=<your_key_goes_here>)
