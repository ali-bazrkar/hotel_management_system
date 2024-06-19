from tkinter import *
import tkinter.messagebox as msg
from controller import UserController
from view import MyButton, TextWithLabel


class ProfileView:
    def reset_form(self):
        self.id.set(self.user[0].id)
        self.name.variable.set(self.user[0].name)
        self.family.variable.set(self.user[0].family)
        self.username.variable.set(self.user[0].username)
        self.password.variable.set(self.user[0].password)

    def edit_click(self):
        status, message = UserController.edit(self.id.get(),
                                              self.name.variable.get(),
                                              self.family.variable.get(),
                                              self.username.variable.get(),
                                              self.password.variable.get(),
                                              'guest')
        if status:
            msg.showinfo("Edit", "Edited Successfully.")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def close_win(self):
        from view import GuestPanel
        self.win.destroy()
        guest_panel = GuestPanel(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("Guest Profile")
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 250) // 2
        y = (self.win.winfo_screenheight() - 260) // 2
        self.win.geometry(f"250x260+{x}+{y}")

        # WIDGETS
        self.id = StringVar()
        self.name = TextWithLabel(self.win, "Name", 20, 20, "white", 70)
        self.family = TextWithLabel(self.win, "Family", 20, 60, "white", 70)
        self.username = TextWithLabel(self.win, "Username", 20, 100, "white", 70)
        self.password = TextWithLabel(self.win, "Password", 20, 140, "white", 70)

        # BUTTON
        self.edit = MyButton(self.win,
                             text="Edit",
                             x=80, y=200,
                             command=self.edit_click,
                             theme_color="white",
                             style="flat",
                             pack=False,
                             height=4,
                             width=11)

        self.reset_form()
        self.win.mainloop()
