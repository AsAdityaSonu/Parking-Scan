import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Automatic vision-based parking slot detection and occupancy classification")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")


def main():
    # Main win
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
