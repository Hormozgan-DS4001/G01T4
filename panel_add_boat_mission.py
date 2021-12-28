from configure import Frame, Button, Entry, Label, TopLevel
from tkinter import Spinbox, ttk
import tkinter


class BoatMission(TopLevel):
    def __init__(self, mission, k_boat, show_mission, show_boat):
        super(BoatMission, self).__init__()
        self.k_boat = k_boat
        self.mission = mission
        self.show_mi = show_mission
        self.show_bo = show_boat
        self.li_boat = []

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text="Show Boat:").grid(row=0, column=0)
        var = tkinter.StringVar()
        var.set("20")
        self.spin = Spinbox(frm1, from_=0, to=4000, state="readonly", textvariable=var, command=self.show_k_boat)
        self.spin.grid(row=0, column=1)

        Button(self, text="End Mission", command=self.end).grid(row=1, column=0)

        self.tree_boat = ttk.Treeview(self, show="headings", selectmode="browse")
        self.tree_boat["column"] = ("Name", "Tag", "Crow", "Passenger", "Mission Name")
        self.tree_boat.heading("Name", text="Name")
        self.tree_boat.heading("Tag", text="Tag")
        self.tree_boat.heading("Crow", text="Crow")
        self.tree_boat.heading("Passenger", text="Passenger")
        self.tree_boat.heading("Mission Name", text="Mission Name")
        self.tree_boat.bind("<Double-1>", self.add_boat)
        self.tree_boat.grid(row=2, column=0)
        self.show_k_boat()

    def end(self):
        self.mission.end()
        self.show_bo()
        self.show_mi()
        self.destroy()

    def show_k_boat(self):
        self.tree_boat.delete(*self.tree_boat.get_children())
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
        self.show_mi()
        self.show_bo()




