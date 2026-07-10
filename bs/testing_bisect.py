from bisect import bisect_left , bisect_right
import unittest


class TestBisect(unittest.TestCase):

    nums = [1 , 4 , 7]

    def setUp(self):
        pass

    def test_bisect_left_1(self):
        # print(self.nums)
        self.assertEqual(bisect_left(self.nums , 3) , 1)


    def test_bisect_left_2(self):
        self.assertEqual(bisect_left(self.nums , 4) , 1)

    def test_bisect_right_1(self):
        self.assertEqual(bisect_right(self.nums , 3) , 1)

    def test_bisect_right_2(self):
        self.assertEqual(bisect_right(self.nums , 4) , 2)


if __name__ == 'main':
    # arr = [1 , 2, 3 , 4]
    """
    # always return r 

    bisect left
    <   >=
    f   t

    rval for first one >= 
    rval - 1 for last one strictly less 
    
    bisect right 
    
    <=  >
    f   t

    rval for first one strictly greater
    rval - 1 for 

    """
    unittest.main() # finds the classes and methods in them that start with test

    