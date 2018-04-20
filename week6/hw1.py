import random


class Node:
    def __init__(self, data):
        self._data = data
        self._nextNode = None

    @property
    def data(self):
        return self._data

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, value):
        self._nextNode = value


class LinkedList:
    def __init__(self):
        self._rootNode = None

    def add(self, data):
        tmp = Node(data)
        if self._rootNode == None:
            self._rootNode = tmp
            return
        v = self._rootNode
        while v.nextNode != None:
            v = v.nextNode
        v.nextNode = tmp

    def dump(self):
        if self._rootNode == None:
            return
        v = self._rootNode
        while v != None:
            print(v.data)
            v = v.nextNode

    def delete(self, data):
        if self._rootNode == None:
            return
        if self._rootNode.data == data:
            self._rootNode = self._rootNode.nextNode
            return
        v1 = self._rootNode
        v2 = v1.nextNode
        while v2 != None:
            if v2.data == data:
                v1.nextNode = v2.nextNode
            return
            v1 = v2
            v2 = v2.nextNode

    def create_cycle(self):
        size = self.find_size()
        rnd = random.randint(0, size)
        m = self._find_lastnode()
        t = self._find_node(rnd)
        m.nextNode = t

    def _find_node(self, rnd):
        tmp = self._rootNode
        for i in range(1, rnd):
            tmp = tmp.nextNode
        return tmp

    def _find_lastnode(self):
        if self._rootNode == None:
            return
        n = self._rootNode
        while n.nextNode != None:
            n = n.nextNode
        return n

    def find_size(self):
        if self._rootNode == None:
            return
        n = self._rootNode
        size = 0
        while n != None:
            size += 1
        n = n.nextNode
        return size

    def contains_cycle(self):
        n = self._rootNode
        n2 = n
        while True:
            n = n.nextNode
        if n2 == None:
            return False
        if n2.nextNode == None or n2.nextNode.nextNode == None:
            return False
        n2 = n2.nextNode.nextNode
        if n2 == n:
            return True
        return False


if __name__ == "__main__":
    a = LinkedList()
    a.add(5)
    a.add(10)
    a.add(20)
    a.add(29)
    a.dump()
    print("--" * 10)
    a.delete(20)
    a.create_cycle()
    print(a.contains_cycle())
