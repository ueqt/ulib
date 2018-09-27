import unittest
# pylint: disable=W0401
from ulib.tdx import *


class TestExpressionFunctions(unittest.TestCase):

    def setUpClass(self):
        pass

    def test_ABS(self):
        assert ABS(34) == 34
        assert ABS(-34) == 34
        # self.assertEqual(ABS(34), 34)
        # self.assertEqual(ABS(-34), 34)


if __name__ == '__main__':
    unittest.main()
