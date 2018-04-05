# Homework - Week 5

### • hw1.py:
```python
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

    def middleDump(self):
        if self._rootNode == None:
            return
        n = self._rootNode
        n2 = n
        while n != None:
            if n.nextNode == None:
                print(n2.data)
                return
            n = n.nextNode.nextNode
            n2 = n2.nextNode
        print(n2.data)

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


if __name__ == "__main__":
    a = LinkedList()
    a.add(5)
    a.add(10)
    a.add(20)
    a.add(29)
    a.middleDump()
    print("--" * 10)
    a.delete(20)
    a.middleDump()

```

> ...