import unittest

from kurz import Kurz


class TestModReduce(unittest.TestCase):
    """LinearCombination.__mod__ must reduce coefficients mod n."""

    def test_coefficients_reduced(self):
        le = Kurz()
        x = le.var()
        y = le.var()
        n = 7

        reduced = (15 * x + 20 * y + 100) % n

        self.assertEqual(reduced.coeff(x), 15 % n)
        self.assertEqual(reduced.coeff(y), 20 % n)
        self.assertEqual(reduced.coeff(le.vone), 100 % n)


if __name__ == '__main__':
    unittest.main()
