import unittest

class LltTest(unittest.TestCase):
    def test_llt(self):
        from llt.core import llt
        self.assertIsNone(llt('cat', 'pro', 'tas', 'lab1,lab2'))