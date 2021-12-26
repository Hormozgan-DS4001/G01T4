import random

from configure import Button, Label, LabelFrame, Entry, Frame, Scale, Tk
import tkinter
from tkinter import Spinbox, messagebox


class AddBoat(Tk):
    def __init__(self, callback_add_boat):
        super(AddBoat, self).__init__()
        self.callback_add = callback_add_boat
        self.passenger = 0
        self.crow = 0
        self.typ = ""


        frm0 = Frame(self)
        frm0.grid(row=0, column=0)
        Label(frm0, text="Name Boat:").grid(row=0, column=0)
        self.ent_nam = Entry(frm0)
        self.ent_nam.grid(row=0, column=1)

        frm1 = Frame(self)
        frm1.grid(row=1, column=0)
        Label(frm1, text="Number(00 to 99): ").grid(row=0, column=0)
        self.ent_fi_num = Spinbox(frm1, from_=00, to=99, state="readonly", format="%02.0f")
        self.ent_fi_num.grid(row=0, column=1)
        Label(frm1, text="Type: ").grid(row=0, column=2)
        self.option_var = tkinter.StringVar()
        self.option_var.set("------")
        value = ["Motorboat", "PY-Yacht", "AD-Destroyer-Tender", "Landing-Craft", "Submarine"]
        tkinter.OptionMenu(frm1, self.option_var, *value,
                           command=self.result_om).grid(row=0, column=3, sticky="w")
        Label(frm1, text="Number(000 to 999): ").grid(row=0, column=4)
        self.ent_sec_num = Spinbox(frm1, from_=000, to=999, state="readonly", format="%03.0f")
        self.ent_sec_num.grid(row=0, column=5)
        Label(frm1, text="X:").grid(row=1, column=0, sticky="E")
        self.ent_x = Scale(frm1, width=18, length=122, from_=1, to=500, orient="horizontal")
        self.ent_x.grid(row=1, column=1)
        Label(frm1, text="Y:").grid(row=1, column=2)
        self.ent_y = Scale(frm1, width=18, length=122, from_=1, to=200, orient="horizontal")
        self.ent_y.grid(row=1, column=3)

        self.frm_scale = Frame(self)
        Label(self.frm_scale, text="Passenger: ").grid(row=0, column=0)
        self.scale_pass = Scale(self.frm_scale, width=18, length=122, from_=1, to=self.passenger, orient="horizontal")
        self.scale_pass.grid(row=0, column=1)
        Label(self.frm_scale, text="Crew: ").grid(row=1, column=0)
        self.scale_crew = Scale(self.frm_scale, width=18, length=122, from_=1, to=self.crow, orient="horizontal")
        self.scale_crew.grid(row=1, column=1)

        frm2 = Frame(self)
        frm2.grid(row=3, column=0)
        Button(frm2, text="OK", command=self.add_boat).grid(row=0, column=0)
        Button(frm2, text="Auto", command=self.add_boat_aut).grid(row=0, column=1)

    def add_boat(self):
        if self.typ == "":
            messagebox.showerror("ERROR", "Pleas Choice TYPE!!")
            return
        number1 = self.ent_fi_num.get()
        number2 = self.ent_sec_num.get()
        name = self.ent_nam.get()
        tag = str(number1) + self.typ + str(number2)
        x = self.ent_x.get()
        y = self.ent_y.get()
        passenger = self.scale_pass.get()
        crew = self.scale_crew.get()
        self.callback_add(name, tag, crew, passenger, x, y)

    def add_boat_aut(self):
        if self.typ == "":
            messagebox.showerror("ERROR", "Pleas Choice TYPE!!")
            return

        number1 = "55"
        r1 = random.randint(0, 9)
        r2 = random.randint(0, 9)
        r3 = random.randint(0, 9)
        number2 = str(r1) + str(r2) + str(r3)
        name = self.ent_nam.get()
        tag = number1 + self.typ + number2
        x = self.ent_x.get()
        y = self.ent_y.get()
        passenger = self.scale_pass.get()
        crew = self.scale_crew.get()
        self.callback_add(name, tag, crew, passenger, x, y)

    def result_om(self, even):
        res = self.option_var.get()
        if res == "Motorboat":
            self.passenger = 5
            self.crow = 2
            self.typ = "M"
        elif res == "PY-Yacht":
            self.passenger = 20
            self.crow = 5
            self.typ = "P"
        elif res == "AD-Destroyer-Tender":
            self.passenger = 100
            self.crow = 20
            self.typ = "A"
        elif res == "Landing-Craft":
            self.passenger = 150
            self.crow = 5
            self.typ = "L"
        elif res == "Submarine":
            self.passenger = 5
            self.crow = 15
            self.typ = "S"
        print(self.typ)
        self.frm_scale.grid(row=2, column=0)
        self.scale_crew.config(to=self.crow)
        self.scale_pass.config(to=self.passenger)
