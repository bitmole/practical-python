# ticker.py

from follow import follow
import csv

def filter_symbols(rows, portfolio):
    for r in rows:
        if r['name'] in portfolio:
            yield r

def convert_types(rows, types):
    for r in rows:
        yield [func(val) for func, val in zip(types, r)]

def make_dicts(rows, headers):
    for r in rows:
        yield dict(zip(headers, r))

def select_columns(rows, indices):
    for r in rows:
        yield [r[i] for i in indices]

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt='txt'):
    import report, tableformat
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)

    # print it!
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for r in rows:
        formatter.row((r['name'], str(r['price']), str(r['change'])))


def main(args):
    if len(args) < 3:
        raise SystemExit('usage: ticker portfile logfile [fmt(txt|csv|html)]')

    if len(args) == 3:
        ticker(args[1], args[2])
    else:
        ticker(args[1], args[2], fmt=args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
