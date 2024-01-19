# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(path):
    '''Computes the total cost of a portfolio file'''
    portfolio = []

    with open(path, 'rt') as f:
        rows = csv.reader(f)
        _ = next(rows) # skip headers
        for row in rows:
            try:
                stock, shares, price = row
                portfolio.append((stock, int(shares), float(price)))
            except ValueError:
                print("Couldn't parse", row)

    return [{'name': stock, 'shares': shares, 'price': price} 
            for (stock,shares,price) in portfolio]

def main(path):
    portfolio = read_portfolio(path)
    total = sum(s['shares']*s['price'] for s in portfolio)
    return f'Total cost {total:0.2f}'

if __name__ == "__main__":
    _, *rest = sys.argv
    path = rest[0] if rest else 'Data/portfolio.csv'
    print(main(path))

