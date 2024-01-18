import unittest
import pcost as pc

class KnownOutput(unittest.TestCase):
    def test_main_output(self):
        self.assertEqual(pc.main(), 'Total cost 44671.15')
    def test_portfolio_cost(self):
        self.assertEqual(pc.portfolio_cost(), 44671.15)

if __name__ == "__main__":
    unittest.main()
