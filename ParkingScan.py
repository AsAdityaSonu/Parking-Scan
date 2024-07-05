import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
from LoginPage import login


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
    frame_y = (screen_height-100) // 2

    frame = ctk.CTkFrame(master=app, width=frame_width, height=frame_height)
    frame.place(x=frame_x, y=frame_y, anchor='center')

    label = ctk.CTkLabel(app, text="Welcome to Pehal", font=("Helvetica", 24, "bold"))
    label.pack(pady=50)

    image_path = "/Users/adityapandey/GUI/pythonProject/Tkinter/7.jpg"
    try:
        image = Image.open(image_path)
        image = image.resize((100, 100))
        img = ImageTk.PhotoImage(image)

        # Image label
        header_label = ctk.CTkLabel(master=frame, image=img, text='')
        header_label.image = img
        header_label.pack(pady=(50, 0))
    except FileNotFoundError:
        tkmb.showerror("Error", f"Image not found at {image_path}")

    container = ctk.CTkFrame(master=frame, fg_color="transparent")
    container.pack(expand=True, fill='both', padx=50, pady=50)

    user_entry = ctk.CTkEntry(master=container, placeholder_text="Username", font=("Helvetica", 16), width=300)
    user_entry.pack(pady=12)

    user_pass = ctk.CTkEntry(master=container, placeholder_text="Password", show="*", font=("Helvetica", 16), width=300)
    user_pass.pack(pady=12)

    login_button = ctk.CTkButton(master=container, text='Login', command=lambda: login(app, user_entry, user_pass),
                                 font=("Helvetica", 16, "bold"))
    login_button.pack(pady=12)


def main():
    app = ctk.CTk()
    set_theme()
    main_window(app)
    app.mainloop()


if __name__ == "__main__":
    main()
