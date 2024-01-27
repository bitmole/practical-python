# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(data, 
              select=None, 
              types=None, 
              has_headers=True, 
              delimiter=',', 
              silence_errors=False):
    """Parse a CSV stream into a list of records
       structured as dicts.

    :data:          file-like object
    :select:        selected columns
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
    def convert(rows):
        assert types
        for i, row in enumerate(rows):
            try:
                yield [t(val) for t, val in zip(types, row)] 
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert", row)
                    print(f"Row {i}: Reason", e)

    rows = csv.reader(data, delimiter=delimiter)
    if has_headers:
        headers = next(rows)

    rows = (r for r in rows if r) # generate only non-empty rows

    # filter columns
    if select:
        indices = [headers.index(c) for c in select]
        headers = select
        rows = ([row[i] for i in indices] for row in rows)

    # convert to types
    if types:
        rows = convert(rows)

    # package to records
    if has_headers:
        return [dict(zip(headers, row)) for row in rows] 
    else:
        return [tuple(r) for r in rows]
