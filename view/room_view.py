import tkinter.messagebox as msg
from datetime import datetime
from tkinter import *
from tkinter import ttk
from controller import RoomController, GeneralController
from view import TextWithLabel, MyButton, Table, PersianCalendar
from view.component.colors import *


class RoomView:

    def reset_form(self):
        self.id.set("")
        self.room_number.variable.set("")
        self.room_type.variable.set("")
        self.status.variable.set("")
        self.start_date.set_date((datetime.strptime("2021-03-21", "%Y-%m-%d")))
        self.end_date.set_date((datetime.strptime("2021-03-21", "%Y-%m-%d")))

        status, data_list = RoomController.find_empty_rooms_by_hotel(self.hotel.id)
        if status:
            self.table.refresh_table(data_list)
        else:
            self.table.refresh_table([])

    def select_row(self, item):
        if item and len(item) >= 4:
            self.id.set(item[0])
            self.room_number.variable.set("{:03}".format(item[1]))
            self.room_type.variable.set(item[2])
            self.status.variable.set(item[3])
        else:
            pass

    def save_click(self):
        status, message = GeneralController.book_on_save(self.start_date.gregorian_date,
                                                         self.end_date.gregorian_date,
                                                         self.user[0].id,
                                                         self.id.get())
        if status:
            msg.showinfo("Save", "Room booked successfully."
                                 "\n\n'Edit' or 'Cancel' your reservation from your panel.")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def close_win(self):
        from view import HotelView
        self.win.destroy()
        hotel_view = HotelView(self.user)

    def __init__(self, hotel, user):
        self.hotel = hotel
        self.win = Tk()
        self.win.title(f"Room Booking [Hotel ID : {self.hotel.id}]")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=theme)
        self.user = user

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 720) // 2
        y = (self.win.winfo_screenheight() - 300) // 2
        self.win.geometry(f"720x320+{x}+{y}")

        # CONNECT
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # VARIABLES
        self.id = StringVar()
        self.temp_holder = StringVar()

        # HOTEL INFO DICTIONARY
        self.hotel_info = TextWithLabel(self.win, "Hotel Info", 20, 20, disabled=True, theme_color='white', distance=90)
        self.hotel_info.variable.set(f"{self.hotel.id} - {self.hotel.hotel_name}")

        # WIDGETS & COMBOBOX
        self.room_number = TextWithLabel(self.win, "Room Number", 20, 60, "white", 90, True)
        self.room_type = TextWithLabel(self.win, "Room Type", 20, 100, "white", 90, True)
        self.status = TextWithLabel(self.win, "Status", 20, 140, "white", 90, True)
        Label(self.win, text="Start Date", background=theme, foreground=dark_theme).place(x=20, y=180)
        self.start_date = PersianCalendar(self.win, 110, 180, theme_color='white')
        Label(self.win, text="End Date", background=theme, foreground=dark_theme).place(x=20, y=220)
        self.end_date = PersianCalendar(self.win, 110, 220, theme_color='white')

        # TABLE
        self.table = Table(self.win,
                           ["ID", 'NUMBER', 'TYPE', 'STATUS'],
                           [60, 120, 120, 120],
                           270,
                           20,
                           self.select_row,
                           height=7,
                           theme_color="white")

        self.save = MyButton(self.win,
                             text="Reserve Room",
                             x=120, y=275,
                             command=self.save_click,
                             theme_color="white",
                             style="flat",
                             pack=False,
                             height=4,
                             width=15)

        self.reset = MyButton(self.win,
                              text="Reset",
                              x=20, y=275,
                              command=self.reset_form,
                              theme_color="white",
                              style="flat",
                              pack=False,
                              height=4,
                              width=11)
        self.reset_form()
        self.win.mainloop()
