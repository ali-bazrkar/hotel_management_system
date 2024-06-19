from tkinter import StringVar, Label, Entry, IntVar
from view.component.colors import *


class TextWithLabel:
    def __init__(self, master, text, x, y, theme_color="white", distance=60, disabled=False, width=20):
        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.distance = distance
        self.variable = StringVar(master)
        self.theme_color = theme_color

        if self.theme_color == "white":

            Label(master, text=text, background=theme).place(x=x, y=y)

            if disabled:
                self.text_box = Entry(master,
                                      textvariable=self.variable,
                                      width=width,
                                      bd=0,
                                      highlightthickness=2,
                                      highlightbackground=outline,
                                      readonlybackground =table,
                                      state="readonly",
                                      foreground=dark_table_header)
                self.text_box.place(x=x + distance, y=y)
            else:
                self.text_box = Entry(master,
                                      textvariable=self.variable,
                                      width=width,
                                      bd=0,
                                      highlightthickness=2,
                                      highlightbackground=outline,
                                      background=entry)
                self.text_box.place(x=x + distance, y=y)

        else:

            Label(master, text=text, foreground=entry, background=dark_theme).place(x=x, y=y)

            if disabled:
                self.text_box = Entry(master,
                                      textvariable=self.variable,
                                      width=width,
                                      bd=0,
                                      highlightthickness=2,
                                      highlightbackground=dark_outline,
                                      readonlybackground =dark_table_item,
                                      foreground=table_item,
                                      insertbackground=theme,
                                      state="readonly")
                self.text_box.place(x=x + distance, y=y)
            else:
                self.text_box = Entry(master,
                                      textvariable=self.variable,
                                      width=width,
                                      bd=0,
                                      highlightthickness=2,
                                      highlightbackground=dark_outline,
                                      background=dark_entry,
                                      insertbackground=theme,
                                      foreground=entry)
                self.text_box.place(x=x + distance, y=y)

