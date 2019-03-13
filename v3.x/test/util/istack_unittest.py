# coding=UTF-8
#!/usr/bin/python3

import unittest
from utils.i_stack import IStack

#######################################
#
# test cases for the first stack in IStack
#
# chenxu zhang
# 2019.3
#######################################
class TestLeftStack(unittest.TestCase):

    def setUp(self):
        self.item = IStack()

    def test_isEmpty(self):
        self.item = IStack()
        self.assertFalse(self.item.l_pop())

    def test_left_push_withInt(self):
        self.item.l_push(26)
        count = self.item.l_size()
        self.assertEqual(count,1)

    def test_left_push_withInvalid_type(self):
        result = self.item.l_push('string')
        count = self.item.l_size()
        self.assertFalse(result)
    
    def test_left_push_with_values(self):
        self.item.l_push(26)
        count = self.item.l_size()
        self.assertEqual(count,1)
        for num in range(5):
            self.item.l_push(num)
        count = self.item.l_size()
        self.assertEqual(count,6)


    def test_left_pop_withInt(self):
        self.item.l_push(33)
        value = self.item.l_pop()
        self.assertEqual(value,33)
        count = self.item.l_size()
        self.assertEqual(count,0)

    def test_left_pop_out_of_range(self):
        self.item.l_push(33)
        self.item.l_push(55)
        value = self.item.l_pop()
        self.assertEqual(value,55)

        count = self.item.l_size()
        self.assertEqual(count,1)

        self.item.l_pop()
        result = self.item.l_pop()
        self.assertFalse(result)
       
    def test_left_pop_empty_stack(self):
        result = self.item.l_pop()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
