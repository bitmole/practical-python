#!/usr/bin/env python

# pcost.py
#
# Exercise 1.27

import csv
import sys
from . import report

def portfolio_cost(path):
    portfolio = report.read_portfolio(path)
    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfile')
    total = portfolio_cost(argv[1])
    print(f'Total cost ${total}')

if __name__ == "__main__":
    import sys
    main(sys.argv)
