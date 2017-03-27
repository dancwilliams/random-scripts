# -*- coding: utf-8 -*-
import unittest

from subnet_cruncher.main import *

class TestSubnetCruncher(unittest.TestCase):
    
    def test_crunch_subnets(self):
        cidr_list = [23, 23, 27, 23, 23, 23, 28, 23, 23, 25, 29, 25, 25, 25, 26, 25, 24, 31, 26, 31, 31, 31]
        results = subnet_crunch(cidr_list)
        expected = [20, 23, 26]
        self.assertEqual(results, expected)