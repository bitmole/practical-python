import unittest
import report as rep
from portfolio import Portfolio

class KnownOutput(unittest.TestCase):

    def test_read_portfolio(self):
        self.assertEqual(len(rep.read_portfolio('./Data/portfolio.csv')), 7)

    def test_missing_fields(self):
        self.assertEqual(len(rep.read_portfolio('./Data/missing.csv')), 5)

class PortfolioTests(unittest.TestCase):

    def test_total_cost(self):
        port = Portfolio(rep.read_portfolio('Data/portfolio.csv'))
        self.assertEqual(port.total_cost, 44671.15)

if __name__ == "__main__":
    unittest.main()
