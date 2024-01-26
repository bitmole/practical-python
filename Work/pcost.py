# pcost.py
#
# Exercise 1.27

import csv
import sys
import report

def portfolio_cost(path):
    portfolio = report.read_portfolio(path)
    return sum(s['shares'] * s['price'] for s in portfolio)

def main(path):
    total = portfolio_cost(path)
    return f'Total cost {total:0.2f}'

if __name__ == "__main__":
    _, *rest = sys.argv
    path = rest[0] if rest else 'Data/portfolio.csv'
    print(main(path))

