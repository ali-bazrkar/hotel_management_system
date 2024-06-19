from tkinter import *
from view.component.colors import *
from view import MyButton


class AdminPanel:
    def user_management(self):
        from view import UserManagement
        self.win.destroy()
        user_management = UserManagement(self.user)

    def hotel_management(self):
        from view import HotelManagement
        self.win.destroy()
        hotel_management = HotelManagement(self.user)

    def logout(self):
        from view import LoginView
        self.win.destroy()
        login_view = LoginView()

    def __init__(self, user):
        self.user = user
        self.win = Tk()

        self.win.title("Admin Panel")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=dark_theme)

        x = (self.win.winfo_screenwidth() - 250) // 2
        y = (self.win.winfo_screenheight() - 350) // 2
        self.win.geometry(f"250x350+{x}+{y}")

        Label(text='Welcome to panel', font=("arial", 15), bg=dark_theme, fg=dark_button).pack(pady=(30, 0))
        Label(text=user[0].name.title() + " " + user[0].family.title(), font=("arial", 12), bg=dark_theme, fg=theme).pack(pady=(5, 0))

        self.user_management = MyButton(self.win,
                                        text="User Management",
                                        x=0, y=70,
                                        command=self.user_management,
                                        width=18,
                                        theme_color="dark",
                                        pack=True,
                                        style="flat",
                                        height=8)
        self.hotel_management = MyButton(self.win,
                                         text="Hotel Management",
                                         x=0, y=30,
                                         command=self.hotel_management,
                                         width=18,
                                         theme_color="dark",
                                         pack=True,
                                         style="flat",
                                         height=8)

        Button(self.win,
               text="Log Out",
               width=12,
               bg=dark_theme,
               activebackground=dark_theme,
               fg=dark_button,
               relief="flat",
               font=('arial', 10),
               bd=0,
               activeforeground=dark_button_effect,
               command=self.logout).pack(pady=(40, 10))

        self.win.mainloop()

