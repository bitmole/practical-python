# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None):
    """Parse a CSV file into a list of records
       structured as dicts.

    :filename: path to file
    :returns: list of records (dicts)

    """
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        if select:
            indices = [headers.index(c) for c in select]
            headers = select
            # filter & sanitize
            rows = [[row[i] for i in indices] for row in rows if row]

        records = [dict(zip(headers, row)) for row in rows] 

    return records
