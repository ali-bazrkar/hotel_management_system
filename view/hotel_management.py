import tkinter.messagebox as msg
from tkinter import *
from controller import GeneralController, HotelController
from view import TextWithLabel, MyButton, Table
from view.component.colors import *


class HotelManagement:

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

    def save_click(self):
        status, message = HotelController.save(self.name.variable.get(),
                                               self.book_limit.variable.get(),
                                               self.address.variable.get())
        if status:
            msg.showinfo("Save", "Saved Successfully.")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = HotelController.edit(self.id.get(),
                                               self.name.variable.get(),
                                               self.book_limit.variable.get(),
                                               self.address.variable.get(),
                                               self.room_count.variable.get())
        if status:
            msg.showinfo("Edit", "Edited Successfully.")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = GeneralController.hotel_on_remove(self.id.get())
        if status:
            msg.showinfo("Remove", "Removed Successfully")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def book_window(self):
        from view import BookManagement
        status, message = HotelController.find_by_id(self.id.get())
        if status:
            self.win.destroy()
            book_management = BookManagement(message, self.user)
        else:
            msg.showwarning('Warning', "please select a hotel before you press 'Manage Book'.")

    def room_window(self):
        from view import RoomManagement
        status, message = HotelController.find_by_id(self.hotel.get())
        if status:
            self.win.destroy()
            room_management = RoomManagement(message, self.user)
        else:
            msg.showwarning('Warning', "please select a hotel before you press 'Manage Room'.")

    def hint_box(self):
        msg.showinfo('Hint',
                     'How many rooms can a user book in your hotel\n enter None: unlimited\nenter int (int > 0)')

    def close_win(self):
        from view import AdminPanel
        self.win.destroy()
        amin_panel = AdminPanel(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("Hotel Management")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=dark_theme)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 960) // 2
        y = (self.win.winfo_screenheight() - 305) // 2
        self.win.geometry(f"960x290+{x}+{y}")

        # CONNECT
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # WIDGETS
        self.hotel = StringVar()
        self.id = StringVar()
        self.name = TextWithLabel(self.win, "Hotel Name", 20, 20, "dark", 80)
        self.book_limit = TextWithLabel(self.win, "Book Limit", 20, 65, "dark", width=13, distance=80)
        self.room_count = TextWithLabel(self.win, "Room Count", 20, 110, "dark", 80, True)
        self.address = TextWithLabel(self.win, "Address", 240, 247, "dark", 60, width=40)

        # TABLE
        self.table = Table(self.win,
                           ["ID", 'NAME', 'BOOK LIMIT', 'ROOM COUNT', 'ADDRESS'],
                           [60, 120, 120, 120, 250],
                           260,
                           20,
                           self.select_row,
                           height=5,
                           theme_color="dark")

        # BUTTON
        self.manage_room = MyButton(self.win,
                                    text="Manage Rooms",
                                    x=790, y=245,
                                    command=self.room_window,
                                    theme_color="dark",
                                    style="flat",
                                    pack=False,
                                    height=4,
                                    width=18)

        self.manage_book = MyButton(self.win,
                                    text="Manage Book",
                                    x=635, y=245,
                                    command=self.book_window,
                                    theme_color="dark",
                                    style="flat",
                                    pack=False,
                                    height=4,
                                    width=18)
        y = 30
        self.save = MyButton(self.win,
                             text="Save",
                             x=20, y=230 - y,
                             command=self.save_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.reset = MyButton(self.win,
                              text="Reset",
                              x=20, y=275 - y,
                              command=self.reset_form,
                              theme_color="dark",
                              style="flat",
                              pack=False,
                              height=4,
                              width=11)

        self.remove = MyButton(self.win,
                               text="Remove",
                               x=125, y=275 - y,
                               command=self.remove_click,
                               theme_color="dark",
                               style="flat",
                               pack=False,
                               height=4,
                               width=11)

        self.edit = MyButton(self.win,
                             text="Edit",
                             x=125, y=230 - y,
                             command=self.edit_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.hint = MyButton(self.win,
                             text="?",
                             x=197, y=65,
                             command=self.hint_box,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=1,
                             width=3)

        self.reset_form()
        self.win.mainloop()
