# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(path):
    total_cost = 0
    f = open(path, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for i, row in enumerate(rows, start=1):
        rec = dict(zip(headers, row))
        try:
            total_cost += int(rec['shares']) * float(rec['price'])
        except ValueError:
            print(f"Row {i}: Couldn't convert: {row}")

    f.close()
    return total_cost

def main(path):
    total = portfolio_cost(path)
    return f'Total cost {total:0.2f}'

if __name__ == "__main__":
    _, *rest = sys.argv
    path = rest[0] if rest else 'Data/portfolio.csv'
    print(main(path))

