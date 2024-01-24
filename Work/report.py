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
        headers = next(rows)
        types = [str, int, float]
        for row in rows:
            try:
                rec = {h:f(val) for h,f,val in zip(headers,types,row)}
                portfolio.append(rec)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio

def read_prices(path):
    prices = {}
    with open(path, 'rt') as f:
        rows = csv.reader(f)
        prices = {s:float(p) for s,p in [r for r in rows if r]}
    return prices

def make_report(portfolio, prices):
    rows = []
    for s in portfolio:
        name = s['name']
        nshares = s['shares']
        cur_price = prices[s['name']]
        change = cur_price - s['price']
        rows.append((name, nshares, cur_price, change))
    return rows

def print_report(path_portfolio, path_prices):
    # collect report data
    portfolio = read_portfolio(path_portfolio)
    prices = read_prices(path_prices)
    purchase_price = sum(s['shares']*s['price'] for s in portfolio)
    cur_value = sum(s['shares']*prices[s['name']] for s in portfolio)

    # print headers
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s '*len(headers) % headers)
    print(len(headers) * ((10*'-') + ' '))

    # print rows
    for s, n, p, d in make_report(portfolio, prices):
        p = f'${p:0.2f}'
        print(f'{s:>10s} {n:>10d} {p:>10s} {d:>10.2f}')

    # print summary
    print('='*43)
    print(f'Purchase price: {purchase_price:>10.2f}')
    print(f' Current value: {cur_value:>10.2f}')
    print(f'    Total gain: {cur_value-purchase_price:>10.2f}')

if __name__ == "__main__":
    _, *rest = sys.argv
    path_portfolio = rest[0] if len(rest)>0 else 'Data/portfolio.csv'
    path_prices = rest[1] if len(rest)>1 else 'Data/prices.csv'
    print_report(path_portfolio, path_prices)
