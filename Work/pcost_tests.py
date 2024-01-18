import unittest
import pcost as pc

class KnownOutput(unittest.TestCase):
    def test_known_output(self):
        self.assertEqual(pc.main(), 'Total cost 44671.15')

if __name__ == "__main__":
    unittest.main()
