# pcost.py
#
# Exercise 1.27

def main():
    total = 0
    f = open('./Data/portfolio.csv', 'rt')
    _ = next(f) # skip headers
    for line in f:
        stock, shares, price = line.split(',')
        shares, price = int(shares), float(price)
        total += shares * price
    f.close()
    return f'Total cost {total:0.2f}'
