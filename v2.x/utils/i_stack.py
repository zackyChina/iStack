# coding=UTF-8
#!/usr/bin/python2

#######################################
#
# It used for stack operation
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

    def __init__(self):
        # initialize a array with two dimsion
        self.items = [array.array('i', []), array.array('i', [])]

    #--------------------------------------
    # methods for stack 1
    def l_push(self, data):
        if isinstance(data, int) != True:
            logging.warning('only integer type is allowed')
            return False
        self.items[0].append(data)

    def l_pop(self):
        logging.info('stack 1 pop')
        if not self.__isEmpty(0):
            return False
        return self.items[0].pop()

    #------------------------------------------
    # methods for stack 2
    # add data into 2nd statck
    def r_push(self, data):
        self.items[1].append(data)

    # retrive data from 2nd stack
    def r_pop(self):
        logging.info('stack 2 pop')
        if not self.__isEmpty(1):
            return False
        return self.items[1].pop()
    
    # check whether array is empty
    def __isEmpty(self, index):
        if not self.items[index]:
            logging.warning('pop from empty stack')
            return False
            
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    op = IStack()
    op.l_push('35')
    print 'result:'
    print op.l_pop()
    op.l_push(234)
    print op.l_pop()
