import unittest
import report as rep

class KnownOutput(unittest.TestCase):

    def test_main_output(self):
        self.assertEqual(rep.main('Data/portfolio.csv'), 'Total cost 44671.15')

    def test_portfolio_cost(self):
        expected = [
                ('AA', 100, 32.2), 
                ('IBM', 50, 91.1), 
                ('CAT', 150, 83.44), 
                ('MSFT', 200, 51.23), 
                ('GE', 95, 40.37), 
                ('MSFT', 50, 65.1), 
                ('IBM', 100, 70.44)
                ]
        self.assertEqual(rep.portfolio_cost('./Data/portfolio.csv'), expected)

    def test_missing_fields(self):
        expected = [
                ('AA', 100, 32.2), 
                ('IBM', 50, 91.1), 
                ('CAT', 150, 83.44), 
                ('GE', 95, 40.37), 
                ('MSFT', 50, 65.1), 
                ]
        self.assertEqual(rep.portfolio_cost('Data/missing.csv'), expected)

if __name__ == "__main__":
    unittest.main()
