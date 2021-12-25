from configure import Button, Label, LabelFrame, Entry, Frame, Scale, Tk
import tkinter


class AddBoat(Frame):
    def __init__(self, callback_add_boat):
        super(AddBoat, self).__init__()
        self.callback_add = callback_add_boat
        self.passenger = 0
        self.crow = 0
        self.typ = ""

        self.tag = ""

        Label(self, text="Type: ").grid(row=0, column=0)
        self.option_var = tkinter.StringVar()
        self.option_var.set("------")
        value = ["Motorboat", "PY-Yacht", "AD-Destroyer-Tender", "Landing-Craft", "Submarine"]
        tkinter.OptionMenu(self, self.option_var, *value,
                           command=self.result_om).grid(row=0, column=1, sticky="w")
        self.frm_scale = Frame(self)
        Label(self.frm_scale, text="Passenger: ").grid(row=0, column=0)
        self.scale_pass = Scale(self.frm_scale, width=18, length=122, from_=1, to=self.passenger, orient="horizontal")
        self.scale_pass.grid(row=0, column=1)
        Label(self.frm_scale, text="Crow: ").grid(row=1, column=0)
        self.scale_crow = Scale(self.frm_scale, width=18, length=122, from_=1, to=self.crow, orient="horizontal")
        self.scale_crow.grid(row=1, column=1)

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

        self.frm_scale.grid(row=1, column=0)
        self.scale_crow.config(to=self.crow)
        self.scale_pass.config(to=self.passenger)


m = AddBoat("sdfsdf")
m.mainloop()