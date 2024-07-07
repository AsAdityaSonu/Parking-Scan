import customtkinter as ctk
from PIL import Image, ImageTk


def changePage(content, app):
    for widget in frameRight.winfo_children():
        widget.destroy()

    if content == "Home":
        frameRightTop = ctk.CTkFrame(
            master=frameRight,
            width=app.winfo_screenwidth() * 0.75,
            height=100,
            # fg_color="#a2acf2",
            fg_color="#0e1017",
            corner_radius=0
        )
        frameRightTop.pack(fill='x')

        text_label = ctk.CTkLabel(
            master=frameRightTop,
            text="Dashboard",
            font=("Helvetica", 36, "bold")
        )
        text_label.pack(side='left', padx=35, pady=25)

        image = Image.open("Tkinter/Images/logo.png")
        image = image.resize((40, 40))
        photo = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(master=frameRightTop, image=photo, text="")
        image_label.pack(side='right', padx=30, pady=20)
    elif content == "Features":
        features_label = ctk.CTkLabel(
            master=frameRight,
            text="Features of the Application",
            font=("Helvetica", 24, "bold"),
            text_color="#FFFFFF"
        )
        features_label.pack(pady=50)
    elif content == "About":
        about_label = ctk.CTkLabel(
            master=frameRight,
            text="About the Application",
            font=("Helvetica", 24, "bold"),
            text_color="#FFFFFF"
        )
        about_label.pack(pady=50)
    else:
        from LoginPage import loginScreen
        for widget in app.winfo_children():
            widget.destroy()

        loginScreen(app, 500, 600, app.winfo_screenwidth() // 2, (app.winfo_screenheight() - 50) // 2)


def Dashboard(app):
    app.title("Dashboard")

    frame = ctk.CTkFrame(
        master=app,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight(),
        # fg_color="#1c1c1c"
    )
    frame.pack(expand=True, fill='both')

    # -------------------------------- Left Frame --------------------------------
    frameLeft = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth() * 0.25,
        height=app.winfo_screenheight(),
        fg_color="#252525",
        bg_color="#252525"
    )
    frameLeft.pack(side='left', fill='y')

    frameLeftTop = ctk.CTkFrame(
        master=frameLeft,
        width=app.winfo_screenwidth() * 0.25,
        height=app.winfo_screenheight() * 0.15,
        fg_color="#252525",
        bg_color="#252525"
    )
    frameLeftTop.grid(row=0, column=0, sticky='ew')

    # NameBgFrame = ctk.CTkFrame(
    #     master=frameLeftTop,
    #     fg_color="#E63981",
    #     corner_radius=45
    # )
    # NameBgFrame.place(x=25, y=25)

    Name = ctk.CTkLabel(
        master=frameLeftTop,
        text="APSDC",
        font=("Helvetica", 36, "bold"),
        text_color="#fff",
        # fg_color="#ffffff"
    )
    Name.place(x=25, y=25)

    frameLeftCenter = ctk.CTkFrame(
        master=frameLeft,
        width=app.winfo_screenwidth() * 0.25,
        height=app.winfo_screenheight() * 0.62,
        fg_color="#252525",
        bg_color="#252525"
    )
    frameLeftCenter.grid(row=1, column=0, sticky='ew')

    frameLeftCenterButtons = ctk.CTkFrame(
        master=frameLeftCenter,
        fg_color="#252525",
        bg_color="#252525"
    )

    frameLeftCenterButtons.place(relx=0.5, rely=0, anchor='n', relwidth=1, x=0)

    # Define button colors
    button_color = "#E63981"
    button_hover_color = "#FF5C93"

    button1 = ctk.CTkButton(
        master=frameLeftCenterButtons,
        text="Home",
        fg_color=button_color,
        hover_color=button_hover_color,
        text_color="#FFFFFF",
        font=("Helvetica", 18),
        height=40,
        corner_radius=30,
        command=lambda: changePage("Home", app)
    )
    button1.pack(pady=10, padx=20, fill='x')

    button2 = ctk.CTkButton(
        master=frameLeftCenterButtons,
        text="Features",
        fg_color=button_color,
        hover_color=button_hover_color,
        text_color="#FFFFFF",
        font=("Helvetica", 18),
        height=40,
        corner_radius=30,
        command=lambda: changePage("Features", app)
    )
    button2.pack(pady=10, padx=20, fill='x')

    button3 = ctk.CTkButton(
        master=frameLeftCenterButtons,
        text="About Us",
        fg_color=button_color,
        hover_color=button_hover_color,
        text_color="#FFFFFF",
        font=("Helvetica", 18),
        height=40,
        corner_radius=30,
        command=lambda: changePage("About", app)
    )
    button3.pack(pady=10, padx=20, fill='x')

    frameLeftBottom = ctk.CTkFrame(
        master=frameLeft,
        width=app.winfo_screenwidth() * 0.23,
        height=app.winfo_screenheight() * 0.25,
        fg_color="#252525",
        bg_color="#252525"
    )
    frameLeftBottom.grid(row=2, column=0, sticky='ew')

    frameLeftBottomButton = ctk.CTkFrame(
        master=frameLeftBottom,
        fg_color="#252525",
        bg_color="#252525"
    )
    frameLeftBottomButton.pack(side='bottom', fill='x', padx=10, pady=10)

    button4 = ctk.CTkButton(
        master=frameLeftBottomButton,
        text="logout",
        fg_color="#ffffff",
        hover_color="#eeeeee",
        text_color="#E63981",
        font=("Helvetica", 18),
        height=40,
        corner_radius=30,
        command=lambda: changePage("logout", app)
    )
    button4.pack(pady=10, padx=20, fill='x', side='bottom')

    # -------------------------------- Right Frame --------------------------------
    global frameRight
    frameRight = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth() * 0.75,
        height=app.winfo_screenheight(),
        fg_color="#0e1017"
    )
    frameRight.pack(side='right', fill='both', expand=True)

    changePage("Home", app)
