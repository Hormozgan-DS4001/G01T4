from configure import Frame, Button, Entry, Label
from tkinter import Spinbox, ttk
import tkinter


class BoatToMission(Frame):
    def __init__(self, mission, k_boat, master=None):
        super(BoatToMission, self).__init__(master)
        self.k_boat = k_boat
        self.mission = mission
        self.li_boat = []

        var = tkinter.StringVar(self)
        var.set("20")
        self.spin = Spinbox(self, from_=0, to=4000, state="readonly", textvariable=var, command=self.show_k_boat)
        self.spin.grid(row=0, column=0)

        self.tree_boat = ttk.Treeview(self, show="headings", selectmode="browse")
        self.tree_boat["column"] = ("Name", "Tag", "Crow", "Passenger", "Mission Name")
        self.tree_boat.heading("Name", text="Name")
        self.tree_boat.heading("Tag", text="Tag")
        self.tree_boat.heading("Crow", text="Crow")
        self.tree_boat.heading("Passenger", text="Passenger")
        self.tree_boat.heading("Mission Name", text="Mission Name")
        self.tree_boat.bind("<Double-1>", self.add_boat)
        self.tree_boat.grid(row=1, column=0)
        self.show_k_boat()

    def show_k_boat(self):
        k = self.spin.get()
        count = 0
        for boat in self.k_boat(self.mission.x, self.mission.y, int(k)):
            tag = boat.tag[:2] + "-" + boat.tag[2] + "-" + boat.tag[3:]
            self.li_boat.append(boat)
            self.tree_boat.insert("", "end", values=(boat.name, tag, boat.crew, boat.passenger, "-"), text=str(count))
            count += 1

    def add_boat(self, event):
        item = self.tree_boat.identify("item", event.x, event.y)
        ID = self.tree_boat.item(item)["text"]
        res = self.li_boat[int(ID)]
        self.mission.add_boat(res)
        self.show_k_boat()




