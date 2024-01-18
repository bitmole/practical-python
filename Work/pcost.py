# pcost.py
#
# Exercise 1.27

def portfolio_cost():
    total = 0
    f = open('./Data/portfolio.csv', 'rt')
    _ = next(f) # skip headers
    for line in f:
        stock, shares, price = line.split(',')
        shares, price = int(shares), float(price)
        total += shares * price
    f.close()
    return total

def main():
    total = portfolio_cost()
    return f'Total cost {total:0.2f}'

