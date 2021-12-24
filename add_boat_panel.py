from configure import Button, Label, LabelFrame, Entry, Frame, Scale
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
        self.scale = Scale()
        self.frm_scale.grid(row=1, column=0)

    def result_om(self, even):
        for child in self.frm_scale.winfo_children():
            child.destroy()
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





