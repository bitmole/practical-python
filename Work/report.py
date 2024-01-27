#!/usr/bin/env python
# report.py
#
# Exercise 2.4

import csv
import fileparse

def read_portfolio(path):
    """
    Parses data file into stock portfolio
    """
    with open(path, 'rt') as file:
        portfolio = fileparse.parse_csv(file, types=[str, int, float])
    return portfolio

def read_prices(path):
    """
    Parses price data file into stock price dictionary
    """
    with open(path, 'rt') as file:
        prices = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    return {n:p for n, p in prices}

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
        p = f'${p:0.2f}' # pre-format price
        print(f'{s:>10s} {n:>10d} {p:>10s} {d:>10.2f}')

    # print summary
    print('='*43)
    print(f'Purchase price: {purchase_price:>10.2f}')
    print(f' Current value: {cur_value:>10.2f}')
    print(f'    Total gain: {cur_value-purchase_price:>10.2f}')

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} portfile pricefile')
    print_report(argv[1], argv[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
