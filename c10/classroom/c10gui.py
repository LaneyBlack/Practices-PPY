# -*- coding: utf-8 -*-

from tkinter import BOTH, Tk, W, E, N, S, Canvas, NW, messagebox
from tkinter.ttk import Frame, Style, Label, Entry, Button, Combobox
from PIL import Image, ImageTk, ImageFilter

max_h = 500
max_w = 900


class Window(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initialise()

    def read_again(self):
        self.image = ImageTk.PhotoImage(self.im)
        self.base.create_image(0, 0, image=self.image, anchor=NW)

    def read_img(self):
        filepath = self.o.get()
        self.im = Image.open(filepath)
        self.f_btn.config(state="normal")
        self.save_btn.config(state="normal")
        self.can_btn.config(state="normal")
        self.scale_btn.config(state="normal")
        self.orig_img = self.im
        self.read_again()

    def save_img(self):
        filepath = self.z.get()
        if filepath=="":
            filepath = self.o.get()
        self.im.save(filepath)

    def scale(self):
        w,h = self.im.size
        multiplier = float(self.scbox.get())
        size = int(w*multiplier), int(h*multiplier)
        self.im = self.im.resize(size)
        self.read_again()

    def cancel(self):
        self.im = self.orig_img
        self.read_again()
    def initialise(self):
        self.parent.title("Lab10")
        self.style = Style()
        # Style Windows: "winnative"    MacOs:    Default: "default"
        self.style.theme_use("winnative")
        self.pack(fill=BOTH, expand=1)

        # Label config
        self.columnconfigure(1, weight=1)
        lbl = Label(self, text="File path:")
        lbl.grid(sticky=W, pady=4, padx=5)

        # Text fields
        self.o = Entry(self)
        self.o.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E + W + S + N)

        self.z = Entry(self)
        self.z.grid(row=2, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E + W + S + N)

        # Buttons
        op_btn = Button(self, text="Open", command=self.read_img)
        op_btn.grid(row=1, column=3)

        self.save_btn = Button(self, text="Save", command=self.save_img)
        self.save_btn.grid(row=2, column=3)
        self.save_btn.config(state="disabled")

        # ComboBoxes
        self.scbox = Combobox(self, values="0.1 0.2 0.3 0.4")
        self.scbox.grid(row=3, column=0, padx=5, pady=4, sticky=W + N)

        self.fcbox = Combobox(self, values="BLUR COTOUR EMBOSS")
        self.fcbox.grid(row=4, column=0, padx=5, pady=4, sticky=W + N)

        # Buttons near comboboxes
        self.scale_btn = Button(self, text="Scale", command=self.scale)
        self.scale_btn.grid(row=3, column=1, padx=5, pady=4, sticky=W + N)
        self.scale_btn.config(state="disabled")

        self.f_btn = Button(self, text="Filter")
        self.f_btn.grid(row=4, column=1, padx=5, pady=4, sticky=W + N)
        self.f_btn.config(state="disabled")

        self.base = Canvas(self, width=max_w, height=max_h)
        self.base.grid(row=5, column=0, padx=5, pady=4, sticky=E + W + S + N, columnspan=3)

        self.can_btn = Button(self, text="Cancel", command=self.cancel)
        self.can_btn.grid(row=5, column=3, padx=5, pady=4, sticky=W + N)
        self.can_btn.config(state="disabled")


def main():
    gui = Tk()
    gui.geometry("1000x700")
    app = Window(gui)
    gui.mainloop()


if __name__ == "__main__":
    main()
