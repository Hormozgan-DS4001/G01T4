from model import Core
from view import ManagerPanel


database = Core()

win = ManagerPanel(database.new_boat, database.new_mission, database.show_boat, database.show_mission, database.k_boat)
win.mainloop()


