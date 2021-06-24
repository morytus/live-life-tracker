# -*- coding: utf-8 -*-

import unittest

class LltTest(unittest.TestCase):
    def test_cmd(self):
        from llt.core import llt
        self.assertIsNone(llt('ok'))

#    def test_start(self):
#        from llt.core import start
#        self.assertEqual(start(), 'start!')
