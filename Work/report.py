#!/usr/bin/env python
# report.py
#
# Exercise 2.4

import csv
import fileparse
import tableformat
from stock import Stock
from portfolio import Portfolio
import logging
logging.basicConfig(
        # filename = 'app.log',
        # filemode = 'w',
        level = logging.WARNING,
        )

def read_portfolio(path, **opts):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(path, 'rt') as file:
        portfolio = Portfolio.from_csv(file)
    return portfolio

def read_prices(path):
    """
    Parses price data file into stock price dictionary
    """
    with open(path, 'rt') as file:
        prices = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    return {n:p for n, p in prices}

def make_report(portfolio, prices):
    return [(s.name, s.shares, prices[s.name], prices[s.name] - s.price) 
            for s in portfolio]

def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        formatter.row((name, shares, f'${price:0.2f}', f'{change:0.2f}'))

def portfolio_report(path_portfolio, path_prices, fmt='txt'):
    # collect report data
    portfolio = read_portfolio(path_portfolio)
    prices = read_prices(path_prices)
    report = make_report(portfolio, prices)

    # print it!
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) < 3:
        raise SystemExit(f'Usage: {argv[0]} portfile pricefile [format(txt|csv|html)]')
    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else: # optional format arg?
        portfolio_report(argv[1], argv[2], fmt=argv[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
