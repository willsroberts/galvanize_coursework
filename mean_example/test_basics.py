import unittest
from basics import mean

class StatsTest(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(1+1,2)

    def test_mean_func(self):
        self.assertEqual(mean(range(9)), 4.0)
