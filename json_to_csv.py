#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Converts a json file to csv"""

import json
import csv
import os

def getJSONData(json_filename):
    """Gets the data from the JSON file."""
    json_filepath = os.path.join(os.getcwd(), json_filename)
    with open(json_filepath, 'r') as inputfile:
        content = inputfile.readlines()

    return content

def convertToCSV(json_data):
    """Converts the JSON data into a CSV file."""

    json_parsed = json.loads(json_data)
    csvfilename = 'coords.csv'
    with open(csvfilename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

    print("File %s saved." % csvfilename)
