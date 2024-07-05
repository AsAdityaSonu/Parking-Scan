import tkinter.messagebox as tkmb
import customtkinter as ctk
from PIL import Image
from MainPage import Dashboard


def loginScreen(app, frame_width, frame_height, frame_x, frame_y):
    frame = ctk.CTkFrame(
        master=app,
        width=frame_width,
        height=frame_height,
        border_width=2,
        border_color="#404040"
    )
    frame.place(x=frame_x, y=frame_y, anchor='center')

    label = ctk.CTkLabel(app, text="Welcome to the Pehal Portal!", font=("Helvetica", 36, "bold"))
    label.pack(pady=60)

    image_path = "/Users/adityapandey/GUI/pythonProject/Tkinter/7.jpg"
    try:
        image = Image.open(image_path)
        ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(100, 100))

        header_label = ctk.CTkLabel(master=frame, image=ctk_image, text='')
        header_label.pack(pady=(50, 0))
    except FileNotFoundError:
        tkmb.showerror("Error", f"Image not found at {image_path}")

    container = ctk.CTkFrame(master=frame, fg_color="transparent")
    container.pack(expand=True, fill='both', padx=50, pady=(30, 50))

    user_entry = ctk.CTkEntry(
        master=container,
        placeholder_text="Username",
        font=("Helvetica", 16),
        width=300,
        height=40,
        corner_radius=10,
        border_width=2,
        border_color="gray",
        fg_color="white",
        # bg_color="lightblue",
        text_color="black",
        placeholder_text_color="gray"
    )
    user_entry.pack(pady=12)

    user_pass = ctk.CTkEntry(
        master=container,
        placeholder_text="Password",
        show="*",
        font=("Helvetica", 16),
        width=300,
        height=40,
        corner_radius=10,
        border_width=2,
        border_color="gray",
        fg_color="white",
        # bg_color="lightblue",
        text_color="black",
        placeholder_text_color="gray"
    )
    user_pass.pack(pady=12)

    login_button = ctk.CTkButton(
        master=container,
        text='Login',
        command=lambda: login(app, user_entry, user_pass),
        font=("Helvetica", 16, "bold"),
        width=300,
        height=40,
        corner_radius=10,
        border_width=2,
        border_color="gray",
        fg_color="lightblue",
        hover_color="lightblue",
        text_color="black"
    )
    login_button.pack(pady=12)


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
