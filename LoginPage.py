import tkinter.messagebox as tkmb
from MainPage import Dashboard


def login(app, user_entry, user_pass):
    username = "aadi"
    password = "12345"
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
        redirectTo(app)
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong Password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong Username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")


def redirectTo(app):
    for widget in app.winfo_children():
        widget.destroy()
    Dashboard(app)
