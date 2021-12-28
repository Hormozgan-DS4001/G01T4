from configure import Entry, Label, Scale, Button, Frame, TopLevel
from panel_add_boat_mission import BoatMission
from tkinter import ttk


class AddMission(Frame):
    def __init__(self, callback_add_mission, callback_k_boat, show_mission, close, master=None):
        super(AddMission, self).__init__(master)
        self.close = close
        self.callback_add_mission = callback_add_mission  # return object mission
        self.callback_k_boat = callback_k_boat
        self.show_mission = show_mission

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
        name = self.ent_name.get()
        x = self.scale_x.get()
        y = self.scale_y.get()
        mis = self.callback_add_mission(name, x, y)
        BoatMission(mis, self.callback_k_boat)
        self.show_mission()
        self.ent_name.delete(0, "end")
        self.scale_x.set(0)
        self.scale_y.set(0)
        self.close()

