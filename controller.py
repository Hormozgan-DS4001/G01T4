from model import Core
from view import ManagerPanel
from pickle import load, dump
from os.path import exists as file_exists

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()


win = ManagerPanel(database.new_boat, database.new_mission, database.show_boat, database.show_mission, database.k_boat,
                   database.set_boat_pos)
win.mainloop()

file = open("database.bin", "wb")
dump(database, file)
file.close()
