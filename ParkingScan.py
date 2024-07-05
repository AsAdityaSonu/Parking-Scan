import tkinter as tk
from tkinter import messagebox
from LoginPage import LoginPage
from MainPage import MainPage


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Automatic vision-based parking slot detection and occupancy classification")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        # Frame widget
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


def main():
    # Main win
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
