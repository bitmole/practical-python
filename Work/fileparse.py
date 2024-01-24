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
        else:
            indices = []

        records = []
        for row in rows:
            if indices:
                row = [row[i] for i in indices]
            records.append(dict(zip(headers, row)))

    return records
