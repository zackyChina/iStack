# coding=UTF-8
#!/usr/bin/python3

import unittest
from utils.i_stack import IStack

class TestRightStack(unittest.TestCase):

    def setUp(self):
        self.item = IStack()

    def test_two_stack(self):
        self.item.l_push(26)
        self.item.l_push(27)
        count = self.item.l_size()
        self.assertEqual(count,2)
        
        self.item.r_push(36)
        self.item.r_push(37)
        self.item.r_push(38)
        count = self.item.r_size()
        self.assertEqual(count,3)


    def test_isEmpty(self):
        self.item = IStack()
        self.assertFalse(self.item.r_pop())

    def test_right_push_withInt(self):
        self.item.r_push(26)
        count = self.item.r_size()
        self.assertEqual(count,1)

    def test_right_push_withInvalid_type(self):
        result = self.item.r_push('string')
        count = self.item.r_size()
        self.assertFalse(result)
    
    def test_right_push_with_values(self):
        self.item.r_push(26)
        count = self.item.r_size()
        self.assertEqual(count,1)
        for num in range(5):
            self.item.r_push(num)
        count = self.item.r_size()
        self.assertEqual(count,6)


    def test_right_pop_withInt(self):
        self.item.r_push(33)
        value = self.item.r_pop()
        self.assertEqual(value,33)
        count = self.item.r_size()
        self.assertEqual(count,0)

    def test_left_pop_out_of_range(self):
        self.item.r_push(33)
        self.item.r_push(55)
        value = self.item.r_pop()
        self.assertEqual(value,55)

        count = self.item.r_size()
        self.assertEqual(count,1)

        self.item.r_pop()
        result = self.item.r_pop()
        self.assertFalse(result)
       
    def test_right_pop_empty_stack(self):
        result = self.item.r_pop()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
