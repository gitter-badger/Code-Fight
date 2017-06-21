"""Simple test example"""

import unittest2
from sparktestingbase.testcase import SparkTestingBaseTestCase
from word_count.solution import answer
from .solution import answer as asw
from lib.tools.timeout import *

class WordCountTest(SparkTestingBaseTestCase):
    """Simple hell world example test."""

    def test_order_by_key(self):
        """Test a parallelize & collect."""
        input = ["hello world"]
        rdd = self.sc.parallelize(input)
        timeout_ = timeout(answer, 5)
        result = timeout_(rdd)
        expected = asw(rdd)
        self.assertTrue(self.assertRDDEqualsWithOrder(expected, result))
    
    def test_order_by_value(self):
        input = ["hello world world"]
        rdd = self.sc.parallelize(input)
        timeout_ = timeout(answer, 5)
        result = timeout_(rdd)
        expected = asw(rdd)
        print(result.collect())
        print(expected.collect())
        self.assertTrue(self.assertRDDEqualsWithOrder(expected, result))

    def test_same_value(self):
        input = ["hello hello world world"]
        rdd = self.sc.parallelize(input)
        timeout_ = timeout(answer, 5)
        result = timeout_(rdd)
        expected = asw(rdd)
        self.assertTrue(self.assertRDDEqualsWithOrder(expected, result))

    
   
if __name__ == "__main__":
    unittest2.main()
