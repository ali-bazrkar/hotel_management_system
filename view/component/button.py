from tkinter import Button
from view.component.colors import *


class MyButton:
    def __init__(self,
                 master,
                 text,
                 x, y,
                 command,
                 width=12,
                 theme_color="white",
                 pack=False,
                 style="flat",
                 height=3):

        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.command = command
        self.theme_color = theme_color
        self.style = style
        self.width = width
        self.pack = pack
        self.height = height


        if self.style == "flat":
            self.bd = 0
        if self.style == "raised":
            self.bd = 2
        if self.style == "groove":
            self.bd = 2

        if self.theme_color == "white":

            if pack == True:
                Button(self.master,
                       text=self.text,
                       width=self.width,
                       bg=button,
                       activebackground=button_effect,
                       fg='white',
                       activeforeground=table_item,
                       bd=self.bd,
                       relief=self.style,
                       highlightthickness=self.height,
                       command=self.command).pack(pady=(self.y, self.x))

            else:
                Button(self.master,
                       text=self.text,
                       width=self.width,
                       bg=button,
                       activebackground=button_effect,
                       fg='white',
                       activeforeground=table_item,
                       bd=self.bd,
                       relief=self.style,
                       highlightthickness=self.height,
                       command=self.command).place(x=self.x, y=self.y)

        else:

            if pack == True:

                Button(self.master,
                       text=self.text,
                       width=self.width,
                       bg=dark_button,
                       activebackground=dark_button_effect,
                       fg='white',
                       activeforeground=table_item,
                       bd=self.bd,
                       relief=self.style,
                       highlightthickness=self.height,
                       command=self.command).pack(pady=(self.y, self.x))
            else:

                Button(self.master,
                       text=self.text,
                       width=self.width,
                       bg=dark_button,
                       activebackground=dark_button_effect,
                       fg='white',
                       activeforeground=table_item,
                       bd=self.bd,
                       relief=self.style,
                       highlightthickness=self.height,
                       command=self.command).place(x=self.x, y=self.y)


