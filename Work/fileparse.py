# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True):
    """Parse a CSV file into a list of records
       structured as dicts.

    :filename: path to file
    :select: columns
    :types: conversion functions
    :returns: list of records (dicts)

    """
    if select and types:
        assert len(select)==len(types)

    if select:
        assert has_headers

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)

        rows = (r for r in rows if r) # ignore empty rows

        # filter columns
        if select:
            indices = [headers.index(c) for c in select]
            headers = select
            rows = [[row[i] for i in indices] for row in rows]
        elif types:
            assert len(headers)==len(types)

        # convert
        if types:
            rows = [[t(val) for t, val in zip(types, row)] for row in rows]

        # package to records
        if has_headers:
            records = [dict(zip(headers, row)) for row in rows] 
        else:
            records = [tuple(r) for r in rows]

    return records
