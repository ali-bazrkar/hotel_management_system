import tkinter.messagebox as msg
from tkinter import *
from controller.user_controller import UserController
from view import TextWithLabel, MyButton, SignupView
from view.component.colors import *


class LoginView:
    def login_click(self):

        ret, user = UserController.find_by_username_and_password(self.username.variable.get(),
                                                                 self.password.variable.get())
        if ret:
            if user[0].role.lower() == "guest":
                from view import GuestPanel
                self.win.destroy()
                guest_panel = GuestPanel(user)
            elif user[0].role.lower() == "admin":
                from view import AdminPanel
                self.win.destroy()
                admin_panel = AdminPanel(user)
        else:
            msg.showerror("Login Error", "Access Denied !!!")

    def signup_click(self):
        self.win.destroy()
        signup_view = SignupView()

    def __init__(self):
        self.win = Tk()
        self.win.title("Login")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=dark_theme)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 250) // 2
        y = (self.win.winfo_screenheight() - 280) // 2
        self.win.geometry(f"250x280+{x}+{y}")

        # LABELS
        self.username = TextWithLabel(self.win, "Username", 20, 40, "dark", 70)
        self.password = TextWithLabel(self.win, "Password", 20, 90, "dark", 70)

        # BUTTONS
        self.login = MyButton(self.win,
                              text="Login",
                              x=5, y=180,
                              command=self.login_click,
                              theme_color="dark",
                              style="flat",
                              pack=True,
                              height=6)

        Button(self.win,
               text="New Account",
               width=12,
               bg=dark_theme,
               activebackground=dark_theme,
               fg=dark_button,
               relief="flat",
               bd=0,
               activeforeground=dark_button_effect,
               command=self.signup_click).pack(pady=(10, 10))

        self.win.mainloop()

