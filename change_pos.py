from configure import Button, Label, Frame, Scale, Entry
from tkinter import messagebox


class ChangePos(Frame):
    def __init__(self, callback_change_pos, close, show_boat, master=None):
        super(ChangePos, self).__init__(master)
        self.close = close
        self.callback_change_pos = callback_change_pos
        self.show_boat = show_boat

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text="Boat Tag:").grid(row=0, column=0)
        self.ent_tag = Entry(frm1)
        self.ent_tag.grid(row=0, column=1)

        frm2 = Frame(self)
        frm2.grid(row=1, column=0)
        Label(frm2, text="X:").grid(row=0, column=0, sticky="E")
        self.ent_x = Scale(frm2, width=18, length=122, from_=1, to=500, orient="horizontal")
        self.ent_x.grid(row=0, column=1)
        Label(frm1, text="Y:").grid(row=0, column=2)
        self.ent_y = Scale(frm2, width=18, length=122, from_=1, to=200, orient="horizontal")
        self.ent_y.grid(row=0, column=3)

        Button(self, text="Change", command=self.change_pos).grid(row=2, column=0)

    def change_pos(self):
        tag = self.ent_tag.get()
        x = self.ent_x.get()
        y = self.ent_y.get()
        self.ent_tag.delete(0, "end")
        self.ent_y.set(1)
        self.ent_x.set(1)
        res = self.callback_change_pos(tag, x, y)
        if res is False:
            messagebox.showerror("TAG", "Not Found Tag")
            return
        self.show_boat()
        self.close()

