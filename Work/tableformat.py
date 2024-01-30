# tableformat.py

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
