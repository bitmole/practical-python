import unittest
import report as rep

class KnownOutput(unittest.TestCase):

    def test_read_portfolio(self):
        self.assertEqual(len(rep.read_portfolio('./Data/portfolio.csv')), 7)

    def test_missing_fields(self):
        self.assertEqual(len(rep.read_portfolio('./Data/missing.csv')), 5)

if __name__ == "__main__":
    unittest.main()
