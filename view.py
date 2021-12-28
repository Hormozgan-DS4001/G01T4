import datetime

from configure import Entry, Tk, TopLevel, Frame, LabelFrame, Button, Scale, Label
from tkinter import ttk
from add_boat_panel import AddBoat
from add_mission import AddMission
import tkinter as tk


class ManagerPanel(Tk):
    def __init__(self, callback_add_boat, callback_add_mission, callback_show_boat, callback_show_mission,
                 callback_k_boat):
        super(ManagerPanel, self).__init__()
        self.callback_add_boat = callback_add_boat
        self.callback_add_mission = callback_add_mission
        self.callback_show_boat = callback_show_boat
        self.callback_show_mission = callback_show_mission
        self.callback_k_boat = callback_k_boat

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

        Label(lbl_frm, text="BOATS LIST..↴").grid(row=2, column=0)
        self.tree_boat = ttk.Treeview(lbl_frm, show="headings", selectmode="browse")
        self.tree_boat["column"] = ("Name", "Tag", "Crow", "Passenger", "Mission Name")
        self.tree_boat.heading("Name", text="Name")
        self.tree_boat.heading("Tag", text="Tag")
        self.tree_boat.heading("Crow", text="Crow")
        self.tree_boat.heading("Passenger", text="Passenger")
        self.tree_boat.heading("Mission Name", text="Mission Name")
        self.tree_boat.grid(row=3, column=0)
        self.tree_boat.bind("<Double-1>", self.boat_panel)
        self.list_boat = []

        Label(lbl_frm, text="MISSION LIST..↴").grid(row=4, column=0)
        self.tree_mis = ttk.Treeview(lbl_frm, show="headings", selectmode="browse")
        self.tree_mis["column"] = ("Name", "Start Time", "Amount Boat")
        self.tree_mis.heading("Name", text="Name")
        self.tree_mis.heading("Start Time", text="Start Time")
        self.tree_mis.heading("Amount Boat", text="Amount Boat")
        self.tree_mis.grid(row=5, column=0)
        self.tree_mis.bind("<Double-1>", self.mission_panel)
        self.li_mission = []

    def show_boat(self):
        boats = self.callback_show_boat()
        self.list_boat = []
        count = 0
        for boat in boats:
            self.list_boat.append(boat)
            tag = boat.tag[:2] + "-" + boat.tag[2] + "-" + boat.tag[3:]
            if boat.mission is False:
                self.tree_boat.insert("", "end", values=(boat.name, tag, boat.crew, boat.passenger, "-"),
                                      text=str(count))
            else:
                self.tree_boat.insert("", 0, values=(boat.name, tag, boat.crew, boat.passenger, boat.mission),
                                      text=str(count))
            count += 1

    def show_mission(self):
        missions = self.callback_show_mission
        self.li_mission = []
        count = 0
        for mission in missions:
            self.li_mission.append(mission)
            if mission.status is False:
                self.tree_mis.insert("", "end", values=(mission.name, "-", mission.boats), text=str(count))

            else:
                a = datetime.datetime.now()
                res = a - mission.time
                self.tree_mis.insert("", 0, values=(mission.name, res.strftime("%y-%m-%d %H:%M:%S"), mission.boats),
                                     text=str(count))
            count += 1



    def add_boat(self):
        panel = AddBoat(self.callback_add_boat, self.not_tab)
        self.not_tab.add(panel, text="ADD BOAT")

    def new_mission(self):
        panel = AddMission(self.callback_add_mission, self.callback_k_boat, self.not_tab)
        self.not_tab.add(panel, text="ADD MISSION")

    def boat_panel(self, event):
        pass

    def mission_panel(self, event):
        pass
