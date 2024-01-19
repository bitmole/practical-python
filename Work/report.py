# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(path):
    '''Computes the total cost of a portfolio file'''
    portfolio = []

    with open(path, 'rt') as f:
        rows = csv.reader(f)
        _ = next(rows) # skip headers
        for row in rows:
            try:
                stock, shares, price = row
                portfolio.append({
                         'name': stock,
                         'shares': int(shares),
                         'price': float(price)})
            except ValueError:
                print("Couldn't parse", row)

    return portfolio

def read_prices(path):
    prices = {}
    with open(path, 'rt') as f:
        rows = csv.reader(f)
        prices = {s:float(p) for s,p in [r for r in rows if r]}
    return prices

def main(path_portfolio, path_prices):
    portfolio = read_portfolio(path_portfolio)
    prices = read_prices(path_prices)
    pprint(portfolio)
    pprint(prices)
    total_cost = sum(s['shares']*s['price'] for s in portfolio)
    cur_value = sum(s['shares']*prices[s['name']] for s in portfolio)
    print(f'Total cost: {total_cost:0.2f}')
    print(f'Current value: {cur_value:0.2f}')
    print(f'Total gain: {cur_value-total_cost:0.2f}')

if __name__ == "__main__":
    _, *rest = sys.argv
    path_portfolio = rest[0] if len(rest)>0 else 'Data/portfolio.csv'
    path_prices = rest[1] if len(rest)>1 else 'Data/prices.csv'
    main(path_portfolio, path_prices)
