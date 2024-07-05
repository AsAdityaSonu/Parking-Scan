import tkinter as tk
from tkinter import messagebox


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label_username = tk.Label(self, text="Username")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self, text="Password")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # validation
        if username == "admin" and password == "password":
            self.controller.show_frame("MainPage")
        else:
            messagebox.showerror("Login Info", "Invalid Username or Password")
