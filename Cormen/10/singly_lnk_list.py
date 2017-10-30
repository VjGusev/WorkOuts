# singly linked list without sentinel
# for simplicity data in node is only integer

import copy as cp


class MyException(Exception):
    pass


class NotNodeError(MyException):
    '''raise when data is not node'''
    def __init__(self, msg):
        self.msg = msg


class ExcNodeChecker(object):
    def __init__(self):
        pass

    def checkIt(self, obj):
        try:
            if(not(isinstance(obj, Node)) and not(obj is None)):
                raise NotNodeError(msg="Fuck! Not Node!")
        except NotNodeError as exp:
            print(exp.msg)
            raise


class Node(object):
    '''singe node of list'''
    def __init__(self, num, next_nd=None):
        self.data = num
        self.next_nd = next_nd

    def setNext(self, node):
        exp_checker = ExcNodeChecker()
        exp_checker.checkIt(node)
        self.next_nd = node

    def getNext(self):
        return self.next_nd

    def getData(self):
        return self.data


# manipulate node entites
class SingLinkList(object):
    '''singly linked list with None at the end'''
    def __init__(self, head=None):
        self.head = cp.copy(head)
        # TODO: determine length -> go trough all links
        self.length = 0
        while(not(head is None)):
            self.length += 1
            head = head.getNext()
        self.nodeChecker = ExcNodeChecker()

    # O(1) - at the head
    def addNodes(self, *nodes):
        for node in nodes:
            self.nodeChecker.checkIt(node)
            self.length += 1
            new_node = cp.copy(node)
            if(self.head is None):
                self.head = new_node
            else:
                new_node.setNext(self.head)
                self.head = new_node

    # O(n) - traverse all
    def getLast(self):
        tmp = self.head
        while(not(tmp.getNext() is None)):
            tmp = tmp.getNext()
        return tmp

    def traverseLst(self):
        tmp = self.head
        # print(tmp.getData())
        while(not(tmp is None)):
            print(tmp.getData())
            tmp = tmp.getNext()

    # O(1)
    def getLen(self):
        return self.length

    def getHead(self):
        return self.head

    def setHead(self, node):
        self.nodeChecker.checkIt(node)
        self.head = node

    def addLen(self, addLen):
        self.length += addLen


def concatLists(lst_1, lst_2):
    end_lst_1 = lst_1.getLast()
    lst_1.addLen(lst_2.getLen())
    end_lst_1.setNext(lst_2.getHead())
    return lst_1
