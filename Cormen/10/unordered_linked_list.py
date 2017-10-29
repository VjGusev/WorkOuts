# doubly linked-list with a sentinel


class Node(object):
    '''One object of list'''
    def __init__(self, data, next_nd=None, prev_nd=None):
        self.data = data
        # maybe data has a key -> let's check
        try:
            self.key = data.key
            self.has_key = True
        except AttributeError:
            # data is a key
            self.has_key = False
            print("Data has no key attribute")

        self.next_nd = next_nd
        self.prev_nd = prev_nd

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next_nd

    def getPrev(self):
        return self.prev_nd

    def setNext(self, node):
        self.next_nd = node

    def setPrev(self, node):
        self.prev_nd = node


class NilNode(Node):
    '''Sentinel object of list'''
    def __init__(self, next_nd=None, prev_nd=None):
        next_nd = self if next_nd is None else next_nd
        prev_nd = self if prev_nd is None else prev_nd
        Node.__init__(self, None, next_nd=next_nd, prev_nd=prev_nd)


class DLinkedList(object):
    '''Doubly linked list with sentinel'''
    def __init__(self):
        self.nil = NilNode()

    # O(1)
    def InsertFirstNode(self, node):
        assert isinstance(node, Node), "Not right type"
        self.nil.getNext().setPrev(node)
        node.setNext(self.nil.getNext())
        node.setPrev(self.nil)
        self.nil.setNext(node)

    # O(n)
    def TraverseList(self):
        if(not self.isEmpty()):
            current = self.nil.getNext()
            while(not(current == self.nil)):
                print(current.getData())
                current = current.getNext()
        else:
            print("Empty list")

    # O(1)
    def DeleteNode(self, node):
        assert isinstance(node, Node), "Not right type"
        node.getNext().setPrev(node.getPrev())
        node.getPrev().setNext(node.setNext())

    # O(1)
    def isEmpty(self):
        return True if self.nil.getNext() == self.nil else False


n1 = Node(10)
n2 = Node(20)
n3 = Node(40)
l_nodes = [n1, n2, n3]
ll = DLinkedList()
for node in l_nodes:
    ll.InsertFirstNode(node)
ll.TraverseList()
