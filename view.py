from configure import Entry, Tk, TopLevel, Frame, LabelFrame, Button, Scale, Label
from tkinter import ttk
import tkinter as tk


class ManagerPanel(Tk):
    def __init__(self, callback_add_boat, callback_add_mission, callback_show_boat, callback_show_mission):
        super(ManagerPanel, self).__init__()
        self.callback_add_boat = callback_add_boat
        self.callback_add_mission = callback_add_mission
        self.callback_show_boat = callback_show_boat
        self.callback_show_mission = callback_show_mission

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        self.main_frm = Frame(self)
        self.main_frm.grid(row=0, column=0)
        self.not_tab.add(self.main_frm, text="Manager")
        lbl_frm = LabelFrame(self.main_frm)
        lbl_frm.grid(row=0, column=0)

        self.frm_map = Frame(lbl_frm, height=200, width=500, bg="#ffffff")
        self.frm_map.grid(row=0, column=0)

        frm_btn = Frame(lbl_frm)
        frm_btn.grid(row=1, column=0)
        Button(frm_btn, text="New Boat", command=self.add_boat).grid(row=0, column=0)
        Button(frm_btn, text="New Mission", command=self.new_mission).grid(row=0, column=1)

    def new_mission(self):
        pass

    def add_boat(self):
        pass

m = ManagerPanel("ma", "a;d", "slfjsd", "sldfjs")
m.mainloop()