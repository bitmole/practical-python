# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, 
              select=None, 
              types=None, 
              has_headers=True, 
              delimiter=',', 
              silence_errors=False):
    """Parse a CSV file into a list of records
       structured as dicts.

    :filename:      path to file
    :select:        columns
    :types:         conversion functions
    :has_headers
    :delimiter
    :silence_errors
    :returns: list of records (dicts)

    """
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    if select and types and len(select) != len(types):
        raise RuntimeError('select and types lists must have the same shape')

    # type conversion helper
    def convert(row, i):
        converted = []
        for val, t in zip(row, types):
            try:
                converted.append(t(val))
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert", row)
                    print(f"Row {i}: Reason", e)
        return converted

    records = []
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
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

        # convert to types
        if types:
            rows = [[convert(row, i)] for i, row in enumerate(rows, start=1)]

        # package to records
        if has_headers:
            records = [dict(zip(headers, row)) for row in rows] 
        else:
            records = [tuple(r) for r in rows]

    return records
