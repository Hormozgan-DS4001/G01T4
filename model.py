

class Boat:
    def __init__(self, name: str, tag: str, crew: int, passenger: int):
        self.name = name
        self.tag = tag
        self.crew = crew
        self.passenger = passenger
        self.distance = 0
        self.mission = False

    def change_cr_pass(self, crew: int, passenger: int):
        self.crew = crew
        self.passenger = passenger

    def set_boat_pos(self, x_boat, x_miss, y_boat, y_miss):
        distance = (((x_boat - x_miss) ** 2) + ((y_boat - y_miss) ** 2)) ** (1 / 2)
        self.distance = distance
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
        self.time = 0

    def end(self):
        self.status = False
        self.time = 0
        self.boats = 0

    def add_boat(self, boat: "Boat"):
        boat.status(self)
        self.boats += 1


class Core:
    def __init__(self):
        pass





