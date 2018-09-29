import unittest
import numpy as np
# pylint: disable=W0401
from ulib.tdx import *


class TestExpressionFunctions(unittest.TestCase):

    def setUp(self):
        # pylint: disable=W0201
        self.C = np.array([1, 2, 3, 4, 5])

    def test_ABS(self):
        assert np.equal(ABS(self.C), np.array([1, 2, 3, 4, 5])).all()
        assert np.equal(ABS(0-self.C), np.array([1, 2, 3, 4, 5])).all()
        # self.assertEqual(ABS(34), 34)
        # self.assertEqual(ABS(-34), 34)


if __name__ == '__main__':
    unittest.main()
