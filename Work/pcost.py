# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(path):
    total = 0
    f = open(path, 'rt')
    rows = csv.reader(f)
    _ = next(f) # skip headers
    for row in rows:
        stock, shares, price = row
        try:
            total += int(shares) * float(price)
        except ValueError:
            print("Couldn't parse", row)

    f.close()
    return total

def main(path):
    total = portfolio_cost(path)
    return f'Total cost {total:0.2f}'

if __name__ == "__main__":
    _, *rest = sys.argv
    path = rest[0] if rest else 'Data/portfolio.csv'
    print(main(path))

