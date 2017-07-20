#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Converts a json file to csv"""

import json
import csv
import os

def getJSONData(json_filename):
    json_filepath = os.path.join(os.getcwd(), json_filename)
    with open(json_filepath, 'r') as inputfile:

def convertToCSV():
    """Converts the JSON data into a CSV file."""
