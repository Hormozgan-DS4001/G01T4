from configure import Frame, Button, Scale, Label


class ChangePassCrew(Frame):
    def __init__(self, callback_boat, close, show_boat, master=None):
        super(ChangePassCrew, self).__init__(master)
        self.callback_boat = callback_boat
        self.show_boat = show_boat
        self.close = close
        res = self.callback_boat.tag[2]

        self.passenger = 0
        self.crew = 0
        self.frm_scale = Frame(self)
        self.frm_scale.grid(row=0, column=0)
        if res == "M":
            self.passenger = 5
            self.crew = 2
        elif res == "P":
            self.passenger = 20
            self.crew = 5
        elif res == "A":
            self.passenger = 100
            self.crew = 20
        elif res == "L":
            self.passenger = 150
            self.crew = 5
        elif res == "S":
            self.passenger = 5
            self.crew = 15
        Label(self.frm_scale, text="Passenger: ").grid(row=0, column=0)
        self.scale_pass = Scale(self.frm_scale, width=18, length=122, from_=1, to=self.passenger
                                , orient="horizontal")
        self.scale_pass.grid(row=0, column=1)
        Label(self.frm_scale, text="Crew: ").grid(row=1, column=0)
        self.scale_crew = Scale(self.frm_scale, width=18, length=122, from_=1, to=self.crew
                                , orient="horizontal")
        self.scale_crew.grid(row=1, column=1)

        Button(self, text="Change", command=self.change).grid(row=1, column=0)

    def change(self):
        pas = self.scale_pass.get()
        crew = self.scale_crew.get()
        self.callback_boat.change_cr_pass(pas, crew)
        self.show_boat()
        self.close()




