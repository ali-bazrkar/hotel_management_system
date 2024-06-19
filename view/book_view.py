import tkinter.messagebox as msg
from tkinter import *
from datetime import datetime
from controller import GeneralController, BookController
from view import TextWithLabel, MyButton, Table, PersianCalendar
from view.component.colors import *


class BookView:

    def reset_form(self):
        self.id.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.room_number.variable.set("")
        self.room_type.variable.set("")
        self.hotel_name.variable.set("")
        self.start_date.set_date((datetime.strptime("2021-03-21", "%Y-%m-%d")))
        self.end_date.set_date((datetime.strptime("2021-03-21", "%Y-%m-%d")))

        status, data_list = GeneralController.find_books_by_user(self.user[0].id)

        if status:
            self.table.refresh_table(data_list)
        else:
            self.table.refresh_table([])

    def select_row(self, item):
        if item and len(item) >= 7:
            self.id.set(item[0])
            self.name.variable.set(item[3])
            self.family.variable.set(item[4])
            self.room_number.variable.set(item[5])
            self.room_type.variable.set(item[6])
            self.hotel_name.variable.set(item[7])
            self.start_date.set_date((datetime.strptime(item[1], "%Y-%m-%d")))
            self.end_date.set_date((datetime.strptime(item[2], "%Y-%m-%d")))
        else:
            pass

    def edit_click(self):
        check, config = BookController.find_by_id(self.id.get())
        config = GeneralController.ensure_list(config)
        if check:
            status, message = BookController.edit(self.id.get(),
                                                  self.start_date.gregorian_date,
                                                  self.end_date.gregorian_date,
                                                  config[0].user_id,
                                                  config[0].room_id)
            if status:
                msg.showinfo("Edit", "Edited Successfully.")
                self.reset_form()
            else:
                msg.showerror("Edit Error", message)
        else:
            msg.showerror("Edit Error", 'Please select an option first.')

    def remove_click(self):
        status, message = GeneralController.book_on_remove(self.id.get())
        if status:
            msg.showinfo("Remove", "Removed Successfully")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def close_win(self):
        from view import GuestPanel
        self.win.destroy()
        guest_panel = GuestPanel(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title(f"Book Management")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=dark_theme)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 980) // 2
        y = (self.win.winfo_screenheight() - 340) // 2
        self.win.geometry(f"980x340+{x}+{y}")

        # CONNECT
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # VARIABLES
        self.id = StringVar()
        self.temp_holder = StringVar()

        # WIDGETS
        self.name = TextWithLabel(self.win, "Name", 260, 250, "dark", 55, True)
        self.family = TextWithLabel(self.win, "Family", 260, 295, "dark", 55, True)
        self.room_number = TextWithLabel(self.win, "Room Number", 485, 250, "dark", 90, True)
        self.room_type = TextWithLabel(self.win, "Room Type", 485, 295, "dark", 90, True)
        self.hotel_name = TextWithLabel(self.win, "Hotel Name", 740, 250, "dark", 80, True)

        # Combobox Dates
        Label(self.win, text="Start Date", background=dark_theme, foreground=entry).place(x=20, y=250)
        self.start_date = PersianCalendar(self.win, 85, 250, theme_color='dark')
        Label(self.win, text="End Date", background=dark_theme, foreground=entry).place(x=20, y=295)
        self.end_date = PersianCalendar(self.win, 85, 295, theme_color='dark')

        self.start_date.set_date(datetime.strptime("2021-03-21", "%Y-%m-%d"))
        self.end_date.set_date(datetime.strptime("2021-03-21", "%Y-%m-%d"))

        # TABLE
        self.table = Table(self.win,
                           ["ID", 'START DATE',
                            'END DATE', 'GUEST NAME',
                            'GUEST FAMILY','ROOM NUMBER',
                            'ROOM TYPE', 'HOTEL NAME'],
                           [60, 130, 130, 130, 130, 100, 120, 140],
                           20,
                           20,
                           self.select_row,
                           height=5,
                           theme_color="dark")

        self.reset = MyButton(self.win,
                              text="Reset",
                              x=735, y=295,
                              command=self.reset_form,
                              theme_color="dark",
                              style="flat",
                              pack=False,
                              height=3,
                              width=8)

        self.edit = MyButton(self.win,
                             text="Edit",
                             x=815, y=295,
                             command=self.edit_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=3,
                             width=8)

        self.remove = MyButton(self.win,
                               text="Remove",
                               x=895, y=295,
                               command=self.remove_click,
                               theme_color="dark",
                               style="flat",
                               pack=False,
                               height=3,
                               width=8)

        self.reset_form()
        self.win.mainloop()
