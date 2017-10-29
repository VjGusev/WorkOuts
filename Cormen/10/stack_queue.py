# create stack from one queue

from collections import deque


class QStack(object):

    def __init__(self, leng):
        self.length = leng
        self.data = deque(maxlen=leng)

    def push(self, el):
        self.data.append(el)  # -> O(1)

    def pop(self):
        # n-1 times pops and appaends O(1) + O(1) --> 2n*O(1) = O(n)
        for _ in range(self.length - 1):
            tmp_el = self.data.pop()
            self.data.append(tmp_el)

        return self.data.pop()


qst = QStack(5)
qst.push(2)
qst.push(3)
qst.push(4)
qst.push(5)
print(qst.pop())
print(qst.pop())
