# follow.py
import os, sys
import time

def follow(logfile):
    with open(logfile) as f:
        f.seek(0, os.SEEK_END) # move file pointer 0 bytes from EOF

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1) # sleep briefly & retry
                continue
            yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

def convert(lines):
    for line in lines:
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        yield (name, price, change)

def ticker(portfile, tickerfile):
    import report
    portfolio = report.read_portfolio(portfile)
    for name, price, change in convert(follow(tickerfile)):
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'usage: {argv[0]} portfile tickerfile')

    ticker(argv[1], argv[2])

if __name__ == "__main__":
    main(sys.argv)
