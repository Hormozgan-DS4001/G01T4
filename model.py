import datetime
from data_structure.data_structure import Sll, HashTable, DArray


class Boat:
    def __init__(self, name: str, tag: str, crew: int, passenger: int, x: int, y: int):
        self.name = name
        self.tag = tag
        self.crew = crew
        self.passenger = passenger
        self.x = x
        self.y = y
        self.flag = False

    def change_cr_pass(self, crew: int, passenger: int):
        self.crew = crew
        self.passenger = passenger

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def distance_boat(self, x_miss, y_miss):
        distance = (((self.x - x_miss) ** 2) + ((self.y - y_miss) ** 2)) ** (1 / 2)
        return distance

    def status(self, mission: "Mission" = None):
        if mission:
            self.flag = mission
        if self.flag:
            return self.flag.status
        return False


class Mission:
    def __init__(self, name: str, x: int, y: int):
        self.boats = 0
        self.name = name
        self.x = x
        self.y = y
        self.status = name
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
        self.M_tag = 0
        self.P_tag = 0
        self.A_tag = 0
        self.L_tag = 0
        self.S_tag = 0
        self.key = DArray()

    def set_boat_pos(self, tag, x, y):
        res = self.li_boat[tag]
        if res is None:
            return False
        res.change_pos(x, y)

    def new_boat(self, name: str, tag: str, crew: int, passenger: int, x: int, y: int):
        if tag[2] == "L" and self.L_tag < 800:
            self.L_tag += 1
        elif tag[2] == "M" and self.M_tag < 800:
            self.M_tag += 1
        elif tag[2] == "P" and self.P_tag < 800:
            self.P_tag += 1
        elif tag[2] == "S" and self.S_tag < 800:
            self.S_tag += 1
        elif tag[2] == "A" and self.A_tag < 800:
            self.A_tag += 1
        else:
            return
        new_boat = Boat(name, tag, crew, passenger, x, y)
        self.li_boat[tag] = new_boat
        self.key.append(tag)

    def new_mission(self, name: str, x: int, y: int):
        mission = Mission(name, x, y)
        self.li_mission.add(mission)
        return mission

    def k_boat(self, x, y, k=20):
        self._quickSort(self.key, 0, len(self.key) - 1, x, y)
        count = 0
        for i in range(len(self.key)):
            if count >= k:
                break
            if not self.li_boat[self.key[i]].status():
                count += 1
                yield self.li_boat[self.key[i]]

    def show_boat(self):
        return self.li_boat

    def show_mission(self):
        return self.li_mission

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
