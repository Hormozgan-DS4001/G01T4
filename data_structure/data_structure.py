from typing import List, Optional


class HashTable:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, size: int = 20):
        self.array: List[Optional[HashTable._Node]] = [None] * size
        self.size = size
        self.count = 0

    def __getitem__(self, key):
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                return
            elif self.array[index] == "deleted":
                continue
            elif self.array[index].key == key:
                return self.array[index].value

    def __setitem__(self, key, value):
        if self.count >= 0.75 * self.size:
            self._extend()
        new_node = HashTable._Node(key, value)
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None or self.array[index] == "deleted":
                self.array[index] = new_node
                self.count += 1
                return
            elif self.array[index].key == key:
                self.array[index].value = value
                return
        raise ValueError("Hashtable is full")

    def __iter__(self):
        count = 0
        while count < self.size:
            if self.array[count] is None:
                count += 1
                continue
            else:
                yield self.array[count].value
                count += 1

    def __delitem__(self, key):
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                raise KeyError(f"Not Found {key}")
            elif self.array[index] == "deleted":
                continue
            elif self.array[index].key == key:
                self.array[index] = "deleted"
                self.count -= 1
                if self.count <= 0.25 * self.size:
                    self._shrink()
                return

        raise KeyError(f"Not Found {key}")

    def _hash_function(self, x, i):
        return (hash(x) + i) % self.size

    def _shrink(self):
        old_array = self.array
        self.size = int(self.size / 2)
        self.array = [None] * self.size
        self.count = 0
        for element in old_array:
            if isinstance(element, HashTable._Node):
                for i in range(self.size):
                    index = self._hash_function(element.key, i)
                    if self.array[index] is None:
                        self.array[index] = element
                        self.count += 1
                        break

    def _extend(self):
        old_array = self.array
        self.size *= 2
        self.array = [None] * self.size
        self.count = 0
        for element in old_array:
            if isinstance(element, HashTable._Node):
                for i in range(self.size):
                    index = self._hash_function(element.key, i)
                    if self.array[index] is None:
                        self.array[index] = element
                        self.count += 1
                        break

    def values(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].value

    def key(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].key


class Sll:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def __iter__(self):
        t = self.head
        while t:
            yield t.data
            t = t.next

    def add(self, data):
        new_node = self._Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node


class DArray:
    def __init__(self, capacity=10):
        self.length = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def __repr__(self):
        return "DArray" + repr(self.array[:self.length])

    def __len__(self):
        return self.length

    def __iter__(self):
        count = 0
        while count < self.length:
            yield self.array[count]

    def __getitem__(self, item):
        assert 0 <= item < self.length
        return self.array[item]

    def __setitem__(self, key, value):
        assert 0 <= key < self.length, 'Index out of range'
        self.array[key] = value

    def is_empty(self):
        return self.length == 0

    def append(self, data):
        if self.capacity == self.length:
            self._resize(2 * self.capacity)
        self.array[self.length] = data
        self.length += 1

    def _resize(self, capacity):
        a = [None] * capacity
        for i in range(self.length):
            a[i] = self.array[i]
        self.capacity = capacity
        self.array = a
