import customtkinter as ctk
import tkinter.messagebox as tkmb


def Dashboard(app):
    label = ctk.CTkLabel(app, text="Welcome to the New Page", font=("Helvetica", 24, "bold"))
    label.pack(pady=50)

    message_label = ctk.CTkLabel(app, text="You have successfully logged in.", font=("Helvetica", 16))
    message_label.pack(pady=20)

    back_button = ctk.CTkButton(app, text="Back to Login", command=main_window, font=("Helvetica", 16, "bold"))
    back_button.pack(pady=20)
