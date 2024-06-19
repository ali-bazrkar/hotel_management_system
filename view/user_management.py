import tkinter.messagebox as msg
from tkinter import *

from controller import GeneralController, UserController

from view import TextWithLabel, MyButton, Table
from view.component.colors import *


class UserManagement:

    def reset_form(self):
        self.id.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.username.variable.set("")
        self.password.variable.set("")
        self.role.variable.set("guest")

        status1, user_list = UserController.find_by_guest()
        status2, admin = UserController.find_by_id(self.user[0].id)
        entity_list = [admin] + user_list

        if status2 or status1:
            self.table.refresh_table(entity_list)
        else:
            self.table.refresh_table([])

    def select_row(self, item):
        if item and len(item) >= 6:
            self.id.set(item[0])
            self.name.variable.set(item[1])
            self.family.variable.set(item[2])
            self.username.variable.set(item[3])
            self.password.variable.set(item[4])
            self.role.variable.set(item[5])
            self.username_holder.set(item[3])
        else:
            pass

    def save_click(self):
        check, current = UserController.find_by_username(self.username.variable.get())
        if check:
            msg.showerror("Save Error", 'this username is already taken.')
        else:
            if self.role.variable.get() == 'admin':
                msg.showwarning("Warning", 'You dont have permission to add an admin user')
            else:
                status, message = UserController.save(self.name.variable.get(),
                                                      self.family.variable.get(),
                                                      self.username.variable.get(),
                                                      self.password.variable.get(),
                                                      self.role.variable.get().lower())
                if status:
                    msg.showinfo("Save", "Saved Successfully.")
                    self.reset_form()
                else:
                    msg.showerror("Save Error", message)

    def edit_click(self):
        if self.username_holder.get() != self.username.variable.get():
            check, item = UserController.find_by_username(self.username.variable.get())
            if check:
                msg.showerror('Error', 'This username is taken.')
            else:
                status, message = UserController.edit(self.id.get(),
                                                      self.name.variable.get(),
                                                      self.family.variable.get(),
                                                      self.username.variable.get(),
                                                      self.password.variable.get(),
                                                      self.role.variable.get())
                if status:
                    msg.showinfo("Edit", "Edited Successfully.")
                    self.reset_form()
                else:
                    msg.showerror("Edit Error", message)
        else:
            status, message = UserController.edit(self.id.get(),
                                                  self.name.variable.get(),
                                                  self.family.variable.get(),
                                                  self.username.variable.get(),
                                                  self.password.variable.get(),
                                                  'guest')

    def remove_click(self):
        if self.role.variable.get() != 'admin':
            status, message = GeneralController.user_on_remove(self.id.get())
            if status:
                msg.showinfo("Remove", "Removed Successfully")
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)
        else:
            msg.showwarning("Warning", 'you can not delete yourself')

    def close_win(self):
        from view import AdminPanel
        self.win.destroy()
        admin_panel = AdminPanel(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("User Management")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=dark_theme)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 880) // 2
        y = (self.win.winfo_screenheight() - 325) // 2
        self.win.geometry(f"880x325+{x}+{y}")

        # CONNECT
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # WIDGETS
        self.id = StringVar()
        self.username_holder = StringVar()
        self.name = TextWithLabel(self.win, "Name", 20, 20, "dark", 70)
        self.family = TextWithLabel(self.win, "Family", 20, 60, "dark", 70)
        self.username = TextWithLabel(self.win, "Username", 20, 100, "dark", 70)
        self.password = TextWithLabel(self.win, "Password", 20, 140, "dark", 70)
        self.role = TextWithLabel(self.win, "Role", 20, 180, "dark", 70, True)

        # TABLE
        self.table = Table(self.win,
                           ["ID", 'NAME', 'FAMILY', 'USERNAME', 'PASSWORD', 'ROLE'],
                           [60, 120, 120, 120, 120, 60],
                           250,
                           20,
                           self.select_row,
                           height=7,
                           theme_color="dark")

        # BUTTON
        self.save = MyButton(self.win,
                             text="Save",
                             x=20, y=230,
                             command=self.save_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.reset = MyButton(self.win,
                              text="Reset",
                              x=20, y=275,
                              command=self.reset_form,
                              theme_color="dark",
                              style="flat",
                              pack=False,
                              height=4,
                              width=11)

        self.remove = MyButton(self.win,
                               text="Remove",
                               x=125, y=275,
                               command=self.remove_click,
                               theme_color="dark",
                               style="flat",
                               pack=False,
                               height=4,
                               width=11)

        self.edit = MyButton(self.win,
                             text="Edit",
                             x=125, y=230,
                             command=self.edit_click,
                             theme_color="dark",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.reset_form()
        self.win.mainloop()
