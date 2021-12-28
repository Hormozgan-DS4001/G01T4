from LinkedList import LinkedList

class HashChain:
    def __init__(self):
        self.hashtable_size = 7000
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            self.hashtable[i] = LinkedList()

    def hashcode(self, key):
        return key % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        self.hashtable[i].insertsorted(element)

    def search(self, key):
        i = self.hashcode(key)
        return self.hashtable[i].search(key) != -1

    def display(self):
        for i in range(self.hashtable_size):
            print('[',i,']',end=' ')
            self.hashtable[i].display()
        print()


class Sll:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = self._Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        t = self.head
        while t:
            yield t.data
            t = t.next
