# -*- coding: utf-8 -*-

import unittest

class LltTest(unittest.TestCase):
    def test_llt(self):
        from llt.core import Core
        core = Core()
        self.assertIsNone(core.llt('ok'))

#    def test_start(self):
#        from llt.core import start
#        self.assertEqual(start(), 'start!')
