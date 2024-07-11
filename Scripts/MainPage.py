import customtkinter as ctk
from Camera import Camera
from PIL import Image, ImageTk

bgColor = "#0e1017"


def changePage(content, app):
    for widget in frameRight.winfo_children():
        widget.destroy()

    # -------------------------------- Home --------------------------------
    if content == "Home":
        # -------------------------------- Right Top --------------------------------
        frameRightTop = ctk.CTkFrame(
            master=frameRight,
            height=100,
            fg_color=bgColor,
            corner_radius=0
        )
        frameRightTop.pack(fill='x')

        text_label = ctk.CTkLabel(
            master=frameRightTop,
            text="Dashboard",
            font=("Helvetica", 36, "bold")
        )
        text_label.pack(side='left', padx=35, pady=25)

        frameRightTopRight = ctk.CTkFrame(
            master=frameRightTop,
            fg_color=bgColor,
        )
        frameRightTopRight.pack(side='right', padx=30, pady=20)

        # Load and resize the image
        image = Image.open("Images/Transparent.png")
        image = image.resize((40, 40))
        photo = ImageTk.PhotoImage(image)

        # Configure grid layout
        frameRightTopRight.grid_columnconfigure(0, weight=0)
        frameRightTopRight.grid_columnconfigure(1, weight=0)

        # Image label
        image_label = ctk.CTkLabel(master=frameRightTopRight, image=photo, text="")
        image_label.grid(row=0, column=0, sticky='nsew', padx=(0, 15))

        # Sign out button
        button4 = ctk.CTkButton(
            master=frameRightTopRight,
            text="Sign out",
            fg_color="#ffffff",
            hover_color="#eeeeee",
            text_color="#53b5ac",
            font=("Helvetica", 18),
            command=lambda: changePage("logout", app)
        )
        button4.grid(row=0, column=1, sticky='nsew')

        # -------------------------------- Right Bottom --------------------------------
        frameRightBottom = ctk.CTkFrame(
            master=frameRight,
            fg_color=bgColor,
            height=app.winfo_screenheight() - 90,
            corner_radius=0,
        )
        frameRightBottom.pack(fill='x')

        # Camera Image
        imagePathCamera = "Images/Camera1.png"
        imageCamera = ctk.CTkImage(light_image=Image.open(imagePathCamera), size=(150, 150))

        def on_button_click():
            Camera(app, 0)

        image_button = ctk.CTkButton(
            master=frameRightBottom,
            image=imageCamera,
            text="Camera 1",
            font=("Helvetica", 18, "bold"),
            text_color="#FFFFFF",
            command=on_button_click,
            fg_color="#1E1E2E",
            hover_color="#28283b",
            border_color="#53565c",
            border_width=2,
            corner_radius=8,
            anchor='center',
            compound="top",
            width=180,
            height=200
        )
        image_button.place(relx=0.5, rely=0.5, anchor="c")

    # -------------------------------- Features --------------------------------
    elif content == "Features":
        frameRightTopFeatures = ctk.CTkFrame(
            master=frameRight,
            height=100,
            fg_color=bgColor,
            corner_radius=0
        )
        frameRightTopFeatures.pack(fill='x')

        text_label = ctk.CTkLabel(
            master=frameRightTopFeatures,
            text="Features",
            font=("Helvetica", 36, "bold")
        )
        text_label.pack(side='left', padx=35, pady=25)

        frameRightBottomFeatures = ctk.CTkFrame(
            master=frameRight,
            fg_color=bgColor,
            height=app.winfo_screenheight() - 90,
            corner_radius=0,
        )
        frameRightBottomFeatures.pack(fill='both', expand=True)

        # project description
        description_text = (
            "Parking Scan is a Python application using Tkinter, featuring a login screen and multiple pages "
            "for managing and visualizing data from a parking lot detection system.\n\n"
            "It is an interface for a project that is Parking guidance information (PGI) systems, which are used to "
            "provide"
            "information to drivers about the nearest parking lots and the number of vacant parking slots. Recently, "
            "vision-based"
            "solutions started to appear as a cost-effective alternative to standard PGI systems based on hardware "
            "sensors mounted on each parking slot.\n\n"
            "Vision-based systems provide information about parking occupancy based on images taken by a camera that "
            "is recording a parking lot. However, such systems are challenging to develop due to various possible "
            "viewpoints, weather conditions, and object occlusions. Most notably, they require manual labeling of "
            "parking slot locations in the input image which is sensitive to camera angle change, replacement, "
            "or maintenance.\n\n"
            "In this project, the algorithm that performs Automatic Parking Slot Detection and Occupancy "
            "Classification (APSD-OC) solely on input images is proposed. Automatic parking slot detection is based "
            "on vehicle detections in a series of parking lot images upon which clustering is applied in bird's eye "
            "view to detect parking slots. Once the parking slots positions are determined in the input image, "
            "each detected parking slot is classified as occupied or vacant using a specifically trained ResNet34 "
            "deep classifier.\n\n"
            "The proposed 2-step approach is extensively evaluated on well-known publicly available datasets (PKLot "
            "and CNRPark+EXT), showing high efficiency in parking slot detection and a certain degree of robustness "
            "to the presence of illegal parking or passing vehicles. The trained classifier achieves high accuracy in "
            "parking slot occupancy classification."
        )

        description_label = ctk.CTkLabel(
            master=frameRightBottomFeatures,
            text=description_text,
            font=("Helvetica", 16),
            wraplength=app.winfo_screenwidth() * 0.70,
            justify="left"
        )
        description_label.pack(pady=20)

        # bullet-point features
        features = [
            "Easy login.",
            "Real-time parking lot status visualization.",
            "User-friendly interface.",
            # "Detailed reports and analytics.",
            "Vision-based parking slot detection and classification.",
            "High efficiency in parking slot detection.",
            # "Robustness to illegal parking or passing vehicles.",
            "High accuracy in parking slot occupancy classification."
        ]

        for feature in features:
            feature_label = ctk.CTkLabel(
                master=frameRightBottomFeatures,
                text=f"• {feature}",
                font=("Helvetica", 16)
            )
            feature_label.pack(padx=30, pady=5, anchor='w')

    # -------------------------------- About Us --------------------------------
    elif content == "About":
        frameRightTopAbout = ctk.CTkFrame(
            master=frameRight,
            width=app.winfo_screenwidth() * 0.75,
            height=100,
            fg_color=bgColor,
            corner_radius=0
        )
        frameRightTopAbout.pack(fill='x')

        text_label = ctk.CTkLabel(
            master=frameRightTopAbout,
            text="About Us",
            font=("Helvetica", 36, "bold")
        )
        text_label.pack(side='left', padx=35, pady=25)

        frameRightBottomAbout = ctk.CTkFrame(
            master=frameRight,
            fg_color=bgColor,
            height=app.winfo_screenheight() - 90,
            corner_radius=0,
        )
        frameRightBottomAbout.pack(fill='both', expand=True)

        # Project description
        about_text = (
            "Our project is developed by a dedicated team of students under the guidance of experienced mentors. "
            "We aim to create innovative solutions for parking lot management using vision-based technologies."
        )

        about_label = ctk.CTkLabel(
            master=frameRightBottomAbout,
            text=about_text,
            font=("Helvetica", 16),
            wraplength=app.winfo_screenwidth() * 0.70,
            justify="left"
        )
        about_label.pack(pady=20)

        side_by_side_frame = ctk.CTkFrame(
            master=frameRightBottomAbout,
            fg_color=bgColor
        )
        side_by_side_frame.pack(fill='both', expand=True, padx=20, pady=20)

        mentors_frame = ctk.CTkFrame(
            master=side_by_side_frame,
            fg_color=bgColor
        )
        mentors_frame.pack(side='left', fill='both', expand=True, padx=20)

        mentors_label = ctk.CTkLabel(
            master=mentors_frame,
            text="Mentors",
            font=("Helvetica", 20, "bold"),
            justify="left"
        )
        mentors_label.pack(padx=30, pady=10, anchor='w')

        mentors = [
            "Prof. Kulbir Singh",
            "Dr. Neeru Jindal",
            "Dr. Sandeep Mandia",
            "Dr. Shishir Maheshwari"
        ]

        for mentor in mentors:
            mentor_label = ctk.CTkLabel(
                master=mentors_frame,
                text=f"• {mentor}",
                font=("Helvetica", 16)
            )
            mentor_label.pack(padx=30, pady=5, anchor='w')

        # Students section
        students_frame = ctk.CTkFrame(
            master=side_by_side_frame,
            fg_color=bgColor
        )
        students_frame.pack(side='left', fill='both', expand=True, padx=20)

        students_label = ctk.CTkLabel(
            master=students_frame,
            text="Students",
            font=("Helvetica", 20, "bold"),
            justify="left"
        )
        students_label.pack(padx=30, pady=10, anchor='w')

        students = [
            "Aditya Pandey",
            "Vaibhav Baldeva",
            "Mridula Pal",
            "Nitika Joshi",
            "Dhwani",
        ]

        for student in students:
            student_label = ctk.CTkLabel(
                master=students_frame,
                text=f"• {student}",
                font=("Helvetica", 16)
            )
            student_label.pack(padx=30, pady=5, anchor='w')
    else:
        from LoginPage import loginScreen
        for widget in app.winfo_children():
            widget.destroy()

        loginScreen(app, 500, 600, app.winfo_screenwidth() // 2, (app.winfo_screenheight() - 50) // 2)


def Dashboard(app):
    for widget in app.winfo_children():
        widget.destroy()

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
        fg_color=bgColor
    )
    frameLeft.pack(side='left', fill='y')

    frameLeftTop = ctk.CTkFrame(
        master=frameLeft,
        width=app.winfo_screenwidth() * 0.25,
        height=app.winfo_screenheight() * 0.15,
        fg_color=bgColor
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
        text="Parking Scan",
        font=("Helvetica", 36, "bold"),
        text_color="#fff",
        # fg_color="#ffffff"
    )
    Name.place(x=25, y=25)

    frameLeftCenter = ctk.CTkFrame(
        master=frameLeft,
        width=app.winfo_screenwidth() * 0.25,
        height=app.winfo_screenheight() * 0.85,
        fg_color=bgColor
    )
    frameLeftCenter.grid(row=1, column=0, sticky='ew')

    frameLeftCenterButtons = ctk.CTkFrame(
        master=frameLeftCenter,
        fg_color=bgColor
    )

    frameLeftCenterButtons.place(relx=0.5, rely=0, anchor='n', relwidth=1, x=0)

    # Define button colors
    button_color = bgColor
    button_hover_color = "#1f222b"
    button_border_color = "#81e6dd"

    button1 = ctk.CTkButton(
        master=frameLeftCenterButtons,
        text="Home",
        fg_color=button_color,
        hover_color=button_hover_color,
        text_color="#FFFFFF",
        font=("Helvetica", 18, "bold"),
        height=50,
        corner_radius=10,
        border_width=2,
        border_color=button_border_color,
        command=lambda: changePage("Home", app)
    )
    button1.pack(pady=10, padx=20, fill='x')

    button2 = ctk.CTkButton(
        master=frameLeftCenterButtons,
        text="Features",
        fg_color=button_color,
        hover_color=button_hover_color,
        text_color="#FFFFFF",
        font=("Helvetica", 18, "bold"),
        height=50,
        corner_radius=10,
        border_width=2,
        border_color=button_border_color,
        command=lambda: changePage("Features", app)
    )
    button2.pack(pady=10, padx=20, fill='x')

    button3 = ctk.CTkButton(
        master=frameLeftCenterButtons,
        text="About Us",
        fg_color=button_color,
        hover_color=button_hover_color,
        text_color="#FFFFFF",
        font=("Helvetica", 18, "bold"),
        height=50,
        corner_radius=10,
        border_width=2,
        border_color=button_border_color,
        command=lambda: changePage("About", app)
    )
    button3.pack(pady=10, padx=20, fill='x')

    # -------------------------------- Central Vertical line --------------------------------
    canvas = ctk.CTkCanvas(
        master=frame,
        width=2,
        height=app.winfo_screenheight(),
        bg="#252525",
        highlightthickness=0
    )
    canvas.pack(side='left', fill='y')
    canvas.create_line(1, 0, 1, app.winfo_screenheight(), fill="#252525")

    # -------------------------------- Right Frame --------------------------------
    global frameRight
    frameRight = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth() * 0.75,
        height=app.winfo_screenheight(),
        fg_color="#252525",
        bg_color="#252525"
    )
    frameRight.pack(side='right', fill='both', expand=True)

    changePage("Home", app)
