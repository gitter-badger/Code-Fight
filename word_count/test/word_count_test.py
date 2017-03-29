"""Simple test example"""

import unittest2
from sparktestingbase.testcase import SparkTestingBaseTestCase
from word_count.solution import answer


class WordCountTest(SparkTestingBaseTestCase):
    """Simple hell world example test."""

    def test_order_by_key(self):
        """Test a parallelize & collect."""
        input = ["hello world"]
        rdd = self.sc.parallelize(input)
        result = answer(rdd)
        assert result == [('hello', 1), ('world',1)]

    def test_order_by_value(self):
        input = ["hello world world"]
        rdd = self.sc.parallelize(input)
        result = answer(rdd)
        assert result == [('world', 2), ('hello',1)]

if __name__ == "__main__":
    unittest2.main()
