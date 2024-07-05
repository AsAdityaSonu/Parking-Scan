'''
    This file is the entry point for the Parking Scan application.
'''

import customtkinter as ctk
from LoginPage import loginScreen


def set_theme():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


def main_window(app):
    for widget in app.winfo_children():
        widget.destroy()

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}")
    app.title("Login")

    frame_width = 500
    frame_height = 600
    frame_x = screen_width // 2
    frame_y = (screen_height - 100) // 2

    loginScreen(app, frame_width, frame_height, frame_x, frame_y)


def main():
    app = ctk.CTk()
    set_theme()
    main_window(app)
    app.mainloop()


if __name__ == "__main__":
    main()
