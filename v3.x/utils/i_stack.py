# coding=UTF-8
#!/usr/bin/python3

#######################################
#
# It implements a simple double stack in one array.
# The array with two dimension which restrict only integer value accepted.
# provides push & pop 2 methods for each stack in one array
# methods l_ for stack 1, methods r_ for stack 2
#
# chenxu zhang
# 2019.3
#######################################
import array
import logging

# We can use this stack for integer push or pop operation.


class IStack(object):
    __LEFT_STACK = 0
    __RIGHT_STACK = 1

    def __init__(self):
        # initialize a array with two dimension which restrict only integer value accepted
        self.items = [array.array('i', []), array.array('i', [])]

    # --------------------------------------
    # methods for stack 1
    def l_push(self, data):
        if isinstance(data, int) != True:
            logging.warning('only integer type is allowed')
            return False
        self.items[self.__LEFT_STACK].append(data)

    def l_pop(self):
        logging.info('stack 1 pop')
        if not self.__isEmpty(self.__LEFT_STACK):
            return False
        return self.items[self.__LEFT_STACK].pop()

    # get the count of first stack's element
    def l_size(self):
         return len(self.items[self.__LEFT_STACK])

    # ------------------------------------------
    # methods for stack 2
    # add data into 2nd statck
    def r_push(self, data):
        if isinstance(data, int) != True:
            logging.warning('only integer type is allowed')
            return False
        self.items[self.__RIGHT_STACK].append(data)

    # retrive data from 2nd stack
    def r_pop(self):
        logging.info('stack 2 pop')
        if not self.__isEmpty(self.__RIGHT_STACK):
            return False
        return self.items[self.__RIGHT_STACK].pop()
    
    # get the count of the 2nd stack's element
    def r_size(self):
         return len(self.items[self.__RIGHT_STACK])
    
    # check whether array is empty
    def __isEmpty(self, index):
        
        print('stack %d count %d' % (index,self.l_size()))
        if not self.items[index]:
            logging.warning('pop from empty stack')
            return False
        return True
            

if __name__ == '__main__':
    op = IStack()
    op.l_push('66')
    print('result:')
    print(op.l_pop())
    op.l_push(234)
    op.l_push(77)
    print(op.l_pop())
