from configure import Entry, Label, Scale, Button, Frame, TopLevel
from tkinter import ttk


class AddMission(Frame):
    def __init__(self, callback_add_mission, callback_k_boat, master=None):
        super(AddMission, self).__init__(master)
        self.callback_add_mission = callback_add_mission  # return object mission
        self.callback_k_boat = callback_k_boat

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text="Name: ").grid(row=0, column=0)
        self.ent_name = Entry(frm1)
        self.ent_name.grid(row=0, column=1)
        Label(frm1, text="X: ").grid(row=1, column=0)
        self.scale_x = Scale(frm1, width=18, length=122, from_=1, to=500, orient="horizontal")
        self.scale_x.grid(row=1, column=1)
        Label(frm1, text="Y: ").grid(row=2, column=0)
        self.scale_y = Scale(frm1, width=18, length=122, from_=1, to=200, orient="horizontal")
        self.scale_y.grid(row=2, column=1)

        Button(self, text="Create", command=self.add_mission).grid(row=1, column=0)

    def add_mission(self):
        BoatMission("sdf", self.callback_k_boat, self)


class BoatMission(TopLevel):
    def __init__(self, mission, k_boat, master=None):
        super(BoatMission, self).__init__(master)
        self.k_boat = k_boat
        self.mission = mission

        Label(self, text="For Add Boat To Mission Please Double Click on Boat!!!")
        self.tree = ttk.Treeview(self, show="headings", selectmode="browse")
        self.tree["column"] = ("name", "tag", "distance")
        self.tree.heading("name", text="Name")
        self.tree.heading("tag", text="Tag")
        self.tree.heading("distance", text="Distance")
        self.tree.grid(row=1, column=0)
        self.tree.bind("<Double-1>", self.add_boat_mission)
        self.list = []
        count = 0
        for boat in self.k_boat():
            self.list.append(boat)
            self.tree.insert("", "end", values=[boat.name, boat.tag, boat.distance], text=str(count))
            count += 1

    def add_boat_mission(self, event):
        item = self.tree.identify("item", event.x, event.y)
        ID = self.tree.item(item)["text"]
        res = self.list[int(ID)]
        self.mission.add_boat(res)
