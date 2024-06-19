import tkinter.messagebox as msg
from tkinter import *
from controller.user_controller import UserController
from view.component.colors import *
from view import TextWithLabel, MyButton


class SignupView:

    def create_account(self):
        check, current = UserController.find_by_username(self.username.variable.get())
        if check:
            msg.showerror("Save Error", 'this username is already taken.')
        else:
            status, message = UserController.save(self.name.variable.get(),
                                                  self.family.variable.get(),
                                                  self.username.variable.get(),
                                                  self.password.variable.get(),
                                                  'guest')
            if status:
                from view import LoginView
                msg.showinfo("Save", "Account created successfully.")
                self.win.destroy()
                login_view = LoginView()
            else:
                msg.showerror("Error", message)

    def close_win(self):
        from view import LoginView
        self.win.destroy()
        login_view = LoginView()

    def __init__(self):
        self.win = Tk()
        self.win.title("New Account")
        self.win.resizable(width=False, height=False)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        self.win.configure(bg=dark_theme)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 250) // 2
        y = (self.win.winfo_screenheight() - 300) // 2
        self.win.geometry(f"250x300+{x}+{y}")

        # LABELS
        self.name = TextWithLabel(self.win, "Name", 20, 40, "dark", 70)
        self.family = TextWithLabel(self.win, "Family", 20, 80, "dark", 70)
        self.username = TextWithLabel(self.win, "Username", 20, 120, "dark", 70)
        self.password = TextWithLabel(self.win, "Password", 20, 160, "dark", 70)

        self.sign_up = MyButton(self.win,
                                text="Sign up",
                                x=5, y=230,
                                command=self.
                                create_account,
                                theme_color="dark",
                                style="flat",
                                pack=True,
                                height=6)

        self.win.mainloop()
