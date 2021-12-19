

class Boat:
    def __init__(self, name, ):
        pass

    def set_boat_pos(self, x, y):
        pass

    def status(self, mission: "Mission"):
        pass


class Mission:
    def __init__(self, name: str, x: int, y: int):
        self.boats = []
        self.name = name
        self.x = x
        self.y = y
        self.status = True
        self.time = 0

    def end(self):
        self.status = False
        self.time = 0

    def add_boat(self):
        pass


class Core:
    def __init__(self):
        pass








