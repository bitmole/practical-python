# tableformat.py

def create_formatter(fmt):
    if fmt=='txt':
        return TextTableFormatter()
    elif fmt=='csv':
        return CSVTableFormatter()
    elif fmt=='html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    for s in portfolio:
        data = [str(getattr(s, a)) for a in columns]
        formatter.row(data)
    
class TableFormatter:
    """
    Formatter ABC
    """
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, data):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, data):
        for d in data:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, data):
        print(','.join(data))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, data):
        print('<tr>', end='')
        for d in data:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

