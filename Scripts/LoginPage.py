import tkinter as tk
import tkinter.messagebox as tkmb
import customtkinter as ctk
from MainPage import Dashboard
from PIL import Image, ImageTk


def loginScreen(app, frame_width, frame_height, frame_x, frame_y):
    # -------------------------------- Bg Img --------------------------------
    image = Image.open("Images/bg.png")
    image = image.resize((app.winfo_screenwidth(), app.winfo_screenheight()))
    photo = ImageTk.PhotoImage(image)

    screen_width = app.winfo_screenwidth()
    canvas = tk.Canvas(app, width=screen_width, height=app.winfo_screenheight(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=photo)

    # Store a reference to the image to prevent garbage collection
    app.image_reference = photo
    # -------------------------------- TOP INTRO --------------------------------
    # label = ctk.CTkLabel(
    #     master=canvas,
    #     text="Welcome to the Pehal Portal!",
    #     font=("Helvetica", 36, "bold"),
    #     text_color="white",
    #     fg_color="red",
    # )
    # canvas.create_window(screen_width // 2, 40, window=label)

    canvas.create_text(
        screen_width // 2, 80,
        text="Welcome to the Parking Portal!",
        fill="#E63981",
        font=("Helvetica", 40, "bold"),
        anchor="n",
    )

    # -------------------------------- Login Box --------------------------------
    frame = ctk.CTkFrame(
        master=app,
        width=frame_width,
        height=frame_height,
        border_width=2,
        fg_color="#071B4B",
        border_color="#173885"
        # border_color="#E63981"
    )
    frame.place(x=frame_x, y=frame_y, anchor='center')

    image_path = "Images/logo.png"
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
        border_color="#637db8",
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
        border_color="#637db8",
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
        border_color="#637db8",
        fg_color="#3f6ccc",
        hover_color="#4f7de0",
        text_color="white"
    )
    login_button.pack(pady=12)

    def on_key_press(event):
        login_button.invoke()

    app.bind('<Return>', on_key_press)


def login(app, user_entry, user_pass):
    username = "aadi"
    password = "tiet"
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
