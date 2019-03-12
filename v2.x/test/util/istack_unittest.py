import unittest
from utils.i_stack import * 

class TestIStack(unittest.TestCase):

    def setUp(self):
        self.item = IStack()

    def test_isEmpty(self):
        self.assertFalse(self.item.l_pop())


if __name__ == '__main__':
    unittest.main()
