import tkinter.messagebox as msg
from tkinter import *
from tkinter import ttk

from controller import GeneralController, RoomController
from view import TextWithLabel, MyButton, Table
from view.component.colors import *


class RoomManagement:

    def reset_form(self):
        self.id.set("")
        self.room_number.variable.set("")
        self.room_type.set("")
        self.status.set("")
        self.temp_holder.set("")

        status, data_list = GeneralController.find_hotel_rooms(self.hotel.id)
        if status:
            self.table.refresh_table(data_list)
        else:
            self.table.refresh_table([])

    def select_row(self, item):
        if item and len(item) >= 4:
            self.id.set(item[0])
            self.room_number.variable.set("{:03}".format(item[1]))
            self.room_type.set(item[2])
            self.status.set(item[3])
            self.temp_holder.set(item[3])
        else:
            pass

    def save_click(self):
        if self.temp_holder.get() == 'reserved':
            msg.showerror("Error", 'You cannot add a reserved room on default!')
        else:
            status, message = GeneralController.room_on_save(self.room_number.variable.get(),
                                                             self.room_type.get(),
                                                             self.status.get(),
                                                             self.hotel.id)
            if status:
                msg.showinfo("Save", "Saved Successfully.")
                self.reset_form()
            else:
                msg.showerror("Save Error", message)

    def edit_click(self):
        check, config = RoomController.find_by_id(self.id.get())
        config = GeneralController.ensure_list(config)
        if check:
            if self.temp_holder.get() == 'reserved':
                status, message = RoomController.edit(self.id.get(),
                                                      self.room_number.variable.get(),
                                                      self.room_type.get(),
                                                      'reserved',
                                                      self.hotel.id,
                                                      config[0].user_id)
                if status:
                    msg.showwarning("Attention", "room 'status' will not be changes when 'reserved'.")
                    msg.showinfo("Edit", "Edited Successfully.")
                    self.reset_form()
                else:
                    msg.showerror("Edit Error", message)
            else:
                status, message = RoomController.edit(self.id.get(),
                                                      self.room_number.variable.get(),
                                                      self.room_type.get(),
                                                      self.status.get(),
                                                      self.hotel.id,
                                                      config[0].user_id)
                if status:
                    msg.showinfo("Edit", "Edited Successfully.")
                    self.reset_form()
                else:
                    msg.showerror("Edit Error", message)
        else:
            msg.showerror("Edit Error", 'Please select an option first.')

    def remove_click(self):
        status, message = GeneralController.room_on_remove(self.id.get())
        if status:
            msg.showinfo("Remove", "Removed Successfully")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def close_win(self):
        from view import HotelManagement
        self.win.destroy()
        hotel_management = HotelManagement(self.user)

    def __init__(self, hotel, user):
        self.hotel = hotel
        self.win = Tk()
        self.win.title(f"Room Management [Hotel ID : {self.hotel.id}]")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=dark_theme)
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
        self.hotel_info = TextWithLabel(self.win, "Hotel Info", 20, 20, disabled=True, theme_color='dark', distance=90)
        self.hotel_info.variable.set(f"{self.hotel.id} - {self.hotel.hotel_name}")

        # COMBOBOX STYLE
        self.combo_style = ttk.Style()
        self.combo_style.theme_use('default')
        self.combo_style.layout('TCombobox', [
            ('Combobox.padding', {
                'sticky': 'nswe',
                'children': [ #TODO : CHECK :)
                    ('Combobox.textarea', {'sticky': 'nswe'}),
                    ('Combobox.downarrow', {'side': 'right', 'sticky': 'ns'})]})])
        self.combo_style.configure('TCombobox',
                                   fieldbackground=dark_entry,
                                   background=dark_entry,
                                   foreground=entry,
                                   bordercolor=dark_outline,
                                   relief='flat',
                                   insertbackground=theme,
                                   padding=3)
        self.combo_style.map('TCombobox',
                             fieldbackground=[('readonly', dark_entry)],
                             foreground=[('readonly', theme)],
                             selectbackground=[('focus', dark_button)],
                             background=[('hover', dark_active_header)])
        self.win.option_add('*TCombobox*Listbox.background', dark_entry)
        self.win.option_add('*TCombobox*Listbox.selectBackground', dark_button)
        self.win.option_add('*TCombobox*Listbox.foreground', entry)

        # WIDGETS & COMBOBOX
        Label(self.win, text="Room Type", background=dark_theme, foreground=entry).place(x=20, y=110)
        self.room_number = TextWithLabel(self.win, "Room Number", 20, 65, "dark", 90)
        self.room_type = ttk.Combobox(self.win,
                                      values=['single room', 'double room', 'twin room', 'suite', 'deluxe room'],
                                      width=20, state='readonly')
        self.room_type.place(x=110, y=110)
        Label(self.win, text="Status", background=dark_theme, foreground=entry).place(x=20, y=155)
        self.status = ttk.Combobox(self.win, values=['empty', 'fixing'], width=20, style='TCombobox', state='readonly')
        self.status.place(x=110, y=155)

        # TABLE
        self.table = Table(self.win,
                           ["ID", 'NUMBER', 'TYPE', 'STATUS'],
                           [60, 120, 120, 120],
                           270,
                           20,
                           self.select_row,
                           height=7,
                           theme_color="dark")

        self.save = MyButton(self.win,
                             text="Save",
                             x=40, y=230,
                             command=self.save_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.reset = MyButton(self.win,
                              text="Reset",
                              x=40, y=275,
                              command=self.reset_form,
                              theme_color="dark",
                              style="flat",
                              pack=False,
                              height=4,
                              width=11)

        self.remove = MyButton(self.win,
                               text="Remove",
                               x=145, y=275,
                               command=self.remove_click,
                               theme_color="dark",
                               style="flat",
                               pack=False,
                               height=4,
                               width=11)

        self.edit = MyButton(self.win,
                             text="Edit",
                             x=145, y=230,
                             command=self.edit_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.reset_form()
        self.win.mainloop()
