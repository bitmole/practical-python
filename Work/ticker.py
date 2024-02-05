# ticker.py

from follow import follow
import csv

def stock_pipeline(stream, portfolio):
    rows = csv.reader(stream)
    # select columns
    rows = ([r[i] for i in [0, 1, 4]] for r in rows)
    # convert types
    rows = ([func(val) for func, val in zip((str,float,float), r)] for r in rows)
    # transform to dicts
    rows = (dict(zip(('name', 'price', 'change'), r)) for r in rows)
    # filter portfolio stocks
    rows = (r for r in rows if r['name'] in portfolio)
    return rows

def ticker(portfile, logfile, fmt='txt'):
    import report, tableformat

    rows = stock_pipeline(follow(logfile), report.read_portfolio(portfile))

    # print it!
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for r in rows:
        formatter.row((r['name'], f"${r['price']}", r['change']))


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
