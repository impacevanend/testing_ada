import unittest


def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 5)


if __name__ == '__main__':
    unittest.main()
