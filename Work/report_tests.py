import unittest
import report as rep

class KnownOutput(unittest.TestCase):

    def test_read_portfolio(self):
        expected = [
            {'name': 'AA', 'shares': 100, 'price': 32.2}, 
            {'name': 'IBM', 'shares': 50, 'price': 91.1},
            {'name': 'CAT', 'shares': 150, 'price': 83.44},
            {'name': 'MSFT', 'shares': 200, 'price': 51.23},
            {'name': 'GE', 'shares': 95, 'price': 40.37}, 
            {'name': 'MSFT', 'shares': 50, 'price': 65.1},
            {'name': 'IBM', 'shares': 100, 'price': 70.44}
        ]
        self.assertEqual(rep.read_portfolio('./Data/portfolio.csv'), expected)

    def test_missing_fields(self):
        expected = [
            {'name': 'AA', 'shares': 100, 'price': 32.2}, 
            {'name': 'IBM', 'shares': 50, 'price': 91.1},
            {'name': 'CAT', 'shares': 150, 'price': 83.44},
            {'name': 'GE', 'shares': 95, 'price': 40.37}, 
            {'name': 'MSFT', 'shares': 50, 'price': 65.1},
        ]
        self.assertEqual(rep.read_portfolio('Data/missing.csv'), expected)

if __name__ == "__main__":
    unittest.main()
