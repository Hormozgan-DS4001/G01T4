import datetime
from data_structure.data_structure import Sll, HashTable


class Boat:
    def __init__(self, name: str, tag: str, crew: int, passenger: int, x: int, y: int):
        self.name = name
        self.tag = tag
        self.crew = crew
        self.passenger = passenger
        self.x = x
        self.y = y
        self.mission = False

    def change_cr_pass(self, crew: int, passenger: int):
        self.crew = crew
        self.passenger = passenger

    def distance_boat(self, x_miss, y_miss):
        distance = (((self.x - x_miss) ** 2) + ((self.y - y_miss) ** 2)) ** (1 / 2)
        return distance

    def status(self, mission: "Mission" = None):
        flag = False
        if mission:
            flag = mission.status
        self.mission = flag
        return self.mission


class Mission:
    def __init__(self, name: str, x: int, y: int):
        self.boats = 0
        self.name = name
        self.x = x
        self.y = y
        self.status = True
        self.time = datetime.datetime.now()

    def end(self):
        self.status = False
        self.time = 0
        self.boats = 0

    def add_boat(self, boat: "Boat"):
        boat.status(self)
        self.boats += 1


class Core:
    def __init__(self):
        self.li_mission = Sll()
        self.li_boat = HashTable()
        self.key = []

    def set_boat_pos(self, tag, x, y):
        pass

    def new_boat(self):
        pass

    def new_mission(self):
        pass

    def k_boat(self, x, y, k=20):
        res = self._quickSort(self.key, 0, len(self.key) - 1, x, y)
        for i in range(k):
            yield self.li_boat[res[i]]

    def _partition(self, arr, low, high, x, y):
        i = low - 1
        pivot = self.li_boat[arr[high]].distance_boat(x, y)

        for j in range(low, high):
            if self.li_boat[arr[j]].distance_boat(x, y) <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quickSort(self, arr, low, high, x, y):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self._partition(arr, low, high, x, y)
            self._quickSort(arr, low, pi - 1, x, y)
            self._quickSort(arr, pi + 1, high, x, y)






