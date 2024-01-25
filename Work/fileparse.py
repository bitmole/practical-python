# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None):
    """Parse a CSV file into a list of records
       structured as dicts.

    :filename: path to file
    :returns: list of records (dicts)

    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        if select and types:
            assert len(select)==len(types)

        rows = (r for r in rows if r) # ignore empty rows

        # filter columns
        if select:
            indices = [headers.index(c) for c in select]
            headers = select
            rows = [[row[i] for i in indices] for row in rows]

        # convert
        if types:
            rows = [[t(val) for t, val in zip(types, row)] for row in rows]

        # package to records
        records = [dict(zip(headers, row)) for row in rows] 

    return records
