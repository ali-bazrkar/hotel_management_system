from tkinter import *
from view.component.colors import *
from view import MyButton
import tkinter.messagebox as msg


class GuestPanel:
    def profile_view(self):
        from view import ProfileView
        self.win.destroy()
        profile_view = ProfileView(self.user)

    def hotel_view(self):
        from view import HotelView
        self.win.destroy()
        hotel_view = HotelView(self.user)

    def book_view(self):
        from view import BookView
        self.win.destroy()
        book_view = BookView(self.user)

    def need_help(self):
        msg.showinfo('Help Desk', "'View Profile' : access your account info"
                                  "\n\n'View Rooms' : select hotel and book "
                                  "\n\n'View Reservation' : view your booked rooms here")

    def logout(self):
        from view import LoginView
        self.win.destroy()
        login_view = LoginView()

    def __init__(self, user):
        self.user = user
        self.win = Tk()

        self.win.title("Guest Panel")
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=theme)

        x = (self.win.winfo_screenwidth() - 250) // 2
        y = (self.win.winfo_screenheight() - 430) // 2
        self.win.geometry(f"260x430+{x}+{y}")

        Label(text='Welcome to panel', font=("arial", 15), bg=theme, fg=button).pack(pady=(30, 0))
        Label(text=user[0].name.title() + " " + user[0].family.title(), font=("arial", 12), bg=theme, fg=dark_theme).pack(pady=(5, 0))

        self.profile_view = MyButton(self.win,
                                     text="View Profile",
                                     x=0, y=70,
                                     command=self.profile_view,
                                     width=18,
                                     theme_color="white",
                                     pack=True,
                                     style="flat",
                                     height=8)

        self.hotel_view = MyButton(self.win,
                                   text="View Rooms",
                                   x=0, y=30,
                                   command=self.hotel_view,
                                   width=18,
                                   theme_color="white",
                                   pack=True,
                                   style="flat",
                                   height=8)

        self.book_view = MyButton(self.win,
                                  text="View Reservations",
                                  x=0, y=30,
                                  command=self.book_view,
                                  width=18,
                                  theme_color="white",
                                  pack=True,
                                  style="flat",
                                  height=8)

        Button(self.win,
               text="Need help?",
               width=12,
               bg=theme,
               activebackground=theme,
               fg=button,
               relief="flat",
               font=('arial', 11),
               bd=0,
               activeforeground=button_effect,
               command=self.need_help).pack(pady=(30, 4))

        Button(self.win,
               text="Log Out",
               width=12,
               bg=theme,
               activebackground=theme,
               fg=button,
               relief="flat",
               font=('arial', 10),
               bd=0,
               activeforeground=button_effect,
               command=self.logout).pack(pady=(0, 0))

        self.win.mainloop()
