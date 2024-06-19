from tkinter import ttk, END
from view.component.colors import *
from model.entity import User, Hotel, Room, Book
import tkinter as tk


class Table:
    def __init__(self, master, headers, widths, x, y, select_function, height=7, theme_color="white"):
        self.master = master
        self.x = x
        self.y = y
        self.headers = headers
        self.widths = widths
        self.select_function = select_function
        self.columns = list(range(len(headers)))
        self.height = height

        if theme_color == "white":
            self.style = ttk.Style()
            self.style.theme_use("default")
            self.style.configure("Treeview",
                                 background=table_item,
                                 foreground=dark_theme,
                                 rowheight=38,
                                 fieldbackground=table,
                                 bordercolor=table_item,
                                 borderwidth=0)
            self.style.map('Treeview',
                           background=[('selected', button)],
                           foreground=[('selected', theme)])

            self.style.configure("Treeview.Heading",
                                 background=table_header,
                                 foreground="#3e454a",
                                 relief="flat")
            self.style.map("Treeview.Heading", background=[('active', active_header)])

        if theme_color == "dark":
            self.style = ttk.Style()
            self.style.theme_use("default")
            self.style.configure("Treeview",
                                 background=dark_table_item,
                                 foreground=theme,
                                 rowheight=38,
                                 fieldbackground=dark_table,
                                 bordercolor=dark_table_item,
                                 borderwidth=0)
            self.style.map('Treeview', background=[('selected', dark_button)])

            self.style.configure("Treeview.Heading",
                                 background=dark_table_header,
                                 foreground=theme,
                                 relief="flat")
            self.style.map("Treeview.Heading", background=[('active', dark_active_header)])

        self.table = ttk.Treeview(self.master, columns=self.columns, show="headings", height=self.height)
        for col in self.columns:
            self.table.column(col, width=self.widths[col], stretch=tk.NO)
            self.table.heading(col, text=self.headers[col], anchor=tk.W)

        self.table.bind("<ButtonRelease>", self.select_table)
        self.table.bind("<KeyRelease>", self.select_table)
        self.table.place(x=x, y=y)

    def refresh_table(self, data_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=tuple(data.to_dict().values()))

    def select_table(self, event):
        data = self.table.item(self.table.focus())["values"]
        self.select_function(data)

