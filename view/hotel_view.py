import tkinter.messagebox as msg
from tkinter import *
from controller import HotelController
from view import TextWithLabel, MyButton, Table
from view.component.colors import *


class HotelView:

    def reset_form(self):
        self.id.set("")
        self.name.variable.set("")
        self.book_limit.variable.set("")
        self.room_count.variable.set("")
        self.address.variable.set("")
        self.hotel.set("")

        status, data_list = HotelController.find_all()

        if status:
            self.table.refresh_table(data_list)
        else:
            self.table.refresh_table([])

    def select_row(self, item):
        if item and len(item) >= 5:
            self.id.set(item[0])
            self.name.variable.set(item[1])
            self.book_limit.variable.set(item[2])
            self.room_count.variable.set(item[3])
            self.address.variable.set(item[4])
            self.hotel.set(item[0])
        else:
            pass

    def room_window(self):
        from view import RoomView
        status, message = HotelController.find_by_id(self.hotel.get())
        if status:
            self.win.destroy()
            room_management = RoomView(message, self.user)
        else:
            msg.showwarning('Warning', "please select a hotel before you press 'View Rooms'.")

    def close_win(self):
        from view import GuestPanel
        self.win.destroy()
        guest_panel = GuestPanel(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("Hotel View")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=theme)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 710) // 2
        y = (self.win.winfo_screenheight() - 335) // 2
        self.win.geometry(f"710x335+{x}+{y}")

        # CONNECT
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # WIDGETS
        self.hotel = StringVar()
        self.id = StringVar()
        self.name = TextWithLabel(self.win, "Hotel Name", 20, 250, "white", 85, disabled=True)
        self.book_limit = TextWithLabel(self.win, "Book Limit", 20, 295, "white", distance=85, disabled=True)
        self.room_count = TextWithLabel(self.win, "Room Count", 260, 295, "white", 85, True)
        self.address = TextWithLabel(self.win, "Hotel Address", 260, 250, "white", 85, width=55, disabled=True)

        # TABLE
        self.table = Table(self.win,
                           ["ID", 'NAME', 'BOOK LIMIT', 'ROOM COUNT', 'ADDRESS'],
                           [60, 120, 120, 120, 250],
                           20,
                           20,
                           self.select_row,
                           height=5,
                           theme_color="white")

        # BUTTON
        self.select_room = MyButton(self.win,
                                    text="View Rooms",
                                    x=580, y=290,
                                    command=self.room_window,
                                    theme_color="white",
                                    style="flat",
                                    pack=False,
                                    height=4,
                                    width=12)

        self.reset = MyButton(self.win,
                              text="Reset",
                              x=500, y=290,
                              command=self.reset_form,
                              theme_color="white",
                              style="flat",
                              pack=False,
                              height=4,
                              width=8)

        self.reset_form()
        self.win.mainloop()
