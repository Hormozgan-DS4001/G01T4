from typing import Union

class hashTable:
    class Node:
        def __init__(self, key : str, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return f"node[{self.key}, {self.value}]"

    def __init__(self, size : int = 25, iterable = None):
        self.__len = 0
        self.__table = [None for i in range(size)]
        if iterable:
            for key, value in iterable:
                self[key] = value

    def __hashFunc(self, key : int) -> int:
        limit = len(self.__table)
        return key % limit

    def __allocSpace(self):
        if self.__len >= 3/4 * len(self.__table):
            temp_table = []
            for element in self.__table:
                if isinstance(element, hashTable.Node):
                    temp_table.append(element)
            self.__len = 0
            self.__table = [None for i in range(2 * len(self.__table))]
            for item in temp_table:
                self[item.key] = item.value
            temp_table = None
    
    def __deallocSpace(self):
        if self.__len <= 1/4 * len(self.__table) and self.__len > 25:
            temp_table = []
            for element in self.__table:
                if isinstance(element, hashTable.Node):
                    temp_table.append(element)
            self.__len = 0
            self.__table = [None for i in range(int(1/2 * len(self.__table)))]
            for item in temp_table:
                self[item.key] = item.value
            temp_table = None

    def __insert(self, key, value):
        place : int = self.__hashFunc(hash(key))
        while (isinstance(self.__table[place], hashTable.Node) and self.__table[place].key != key):
            place = self.__hashFunc(place + 1)
        if self.__table[place] != None:
            self.__table[place] = None
        self.__table[place] = self.Node(key, value)
        self.__len += 1
        self.__allocSpace()


    def __deleteData(self, key : str):
        place : int = self.__hashFunc(hash(key))
        while (isinstance(self.__table[place], hashTable.Node) or self.__table[place] == "deleted"):
            if self.__table[place] != "deleted":
                if self.__table[place].key == key:
                    break
            place = self.__hashFunc(place + 1)
        if self.__table[place] == None:
            return
        else:
            self.__table[place] = "deleted"
        self.__len -= 1
        self.__deallocSpace()


    def __getData(self, key : str) -> Union[None, int]:
        place : int = self.__hashFunc(hash(key))
        while (isinstance(self.__table[place], hashTable.Node) or self.__table[place] == "deleted"):
            if self.__table[place] != "deleted":
                if self.__table[place].key == key:
                    return self.__table[place].value
            place = self.__hashFunc(place + 1)
        if self.__table[place] == None:
            return
        else:
            return
            #self.__table[place] = "deleted"


    def __iter__(self):
        for elem in self.__table:
            if isinstance(elem, hashTable.Node):
                yield elem.key, elem.value

    def __len__(self):
        return self.__len

    def __repr__(self):
        return repr(self.__table)

    def __getitem__(self, key):
        return self.__getData(key)

    def __setitem__(self, key, value):
        self.__insert(key, value)

    def __delitem__(self, key):
        self.__deleteData(key)

ht = hashTable
