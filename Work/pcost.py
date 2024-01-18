# pcost.py
#
# Exercise 1.27

def portfolio_cost(path):
    total = 0
    f = open(path, 'rt')
    _ = next(f) # skip headers
    for line in f:
        stock, shares, price = line.split(',')
        try:
            shares, price = int(shares), float(price)
            total += shares * price
        except ValueError:
            print("Couldn't parse", line.strip())

    f.close()
    return total

def main():
    total = portfolio_cost('./Data/portfolio.csv')
    return f'Total cost {total:0.2f}'

