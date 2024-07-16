import cv2
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime
import os

from Models.YOLOv5.mainFile import processVideo

bgColor = "#0e1017"
paused = False


# -------------------------------- Frame Update --------------------------------
def updateFrame(labelCamera, camera):
    ret, img = camera.read()
    if ret:
        if not paused:
            img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)

            labelCamera.imgtk = img
            labelCamera.configure(image=img)
    labelCamera.after(1, updateFrame, labelCamera, camera)


def takeSnapshot(camera):
    if camera is not None:
        ret, img = camera.read()
        if ret:
            output_folder = 'screenshotImages'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            timestamp = datetime.now().strftime("%d-%m-%y_%H:%M:%S")
            filename = os.path.join(output_folder, f"{timestamp}.png")

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img)

            img_pil.save(filename)
            print(f"Snapshot saved as {filename}")


def togglePause(pause_button):
    global paused
    paused = not paused
    pause_button.configure(text="Play" if paused else "Pause")


def exitCommand(app, camera):
    from MainPage import Dashboard
    Dashboard(app),
    camera.release()


def Camera(app, cameraNo):
    for widget in app.winfo_children():
        widget.destroy()

    app.title(f"Camera No {cameraNo}")
    app.configure(bg=bgColor)

    camera = cv2.VideoCapture(cameraNo)
    if not camera.isOpened():
        print(f"Error: Cannot open camera {cameraNo}")
        return

    # Frame
    frame = ctk.CTkFrame(
        master=app,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight(),
        bg_color=bgColor,
        fg_color=bgColor
    )
    frame.pack(expand=True, fill='both')

    # -------------------------------- Frame Top --------------------------------
    frameTop = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight() * 0.1,
        bg_color=bgColor,
        fg_color=bgColor
    )
    frameTop.pack(fill='x')

    date_label = ctk.CTkLabel(
        master=frameTop,
        text="",
        font=("Arial", 26),
        fg_color=bgColor,
        bg_color=bgColor
    )
    date_label.pack(side="left", padx=77, pady=5)

    project_name_label = ctk.CTkLabel(
        master=frameTop,
        text="Parking Scan",
        font=("Arial", 26, "bold"),
        fg_color=bgColor,
        bg_color=bgColor
    )
    project_name_label.pack(side="left", expand=True, pady=(10, 10))

    time_label = ctk.CTkLabel(
        master=frameTop,
        text="",
        font=("Arial", 26),
        fg_color=bgColor,
        bg_color=bgColor
    )
    time_label.pack(side="right", padx=77, pady=5)

    # -------------------------------- Frame Center --------------------------------
    frameCenter = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight() * 0.8,
        bg_color=bgColor,
        fg_color=bgColor,
    )
    frameCenter.pack(expand=True, fill='both')

    labelCamera = ctk.CTkLabel(
        master=frameCenter,
        text="",
    )
    labelCamera.pack(fill="both", expand=True)

    updateFrame(labelCamera, camera)

    # -------------------------------- Frame Bottom --------------------------------
    frameBottom = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight() * 0.1,
        bg_color=bgColor,
        fg_color=bgColor
    )
    frameBottom.pack(expand=True, fill='x')

    button_frame = ctk.CTkFrame(
        master=frameBottom,
        bg_color=bgColor,
        fg_color=bgColor
    )
    button_frame.pack(expand=True)

    snapshot_button = ctk.CTkButton(
        master=button_frame,
        text="Take Snapshot",
        command=takeSnapshot(camera),
        width=150,
        height=40,
        border_color="#81e6dd",
        fg_color=bgColor,
        bg_color=bgColor,
        border_width=2,
    )
    snapshot_button.pack(side="left", padx=10, pady=(10, 30))

    pause_button = ctk.CTkButton(
        master=button_frame,
        text="Pause",
        command=lambda: togglePause(pause_button),
        width=150,
        height=40,
        border_color="#81e6dd",
        fg_color=bgColor,
        bg_color=bgColor,
        border_width=2,
    )
    pause_button.pack(side="left", padx=10, pady=(10, 30))

    exit_button = ctk.CTkButton(
        master=button_frame,
        text="Back",
        command=lambda: exitCommand(app, camera),
        width=150,
        height=40,
        border_color="#81e6dd",
        fg_color=bgColor,
        bg_color=bgColor,
        border_width=2,
    )
    exit_button.pack(side="left", padx=10, pady=(10, 30))

    # -------------------------------- Date and Time --------------------------------
    def updateDateTime():
        current_date_time = datetime.now()
        current_date = current_date_time.strftime("%Y-%m-%d")
        current_time = current_date_time.strftime("%H:%M:%S")
        date_label.configure(text=current_date)
        time_label.configure(text=current_time)
        frameTop.after(1000, updateDateTime)

    updateDateTime()

    # -------------------------------- Destroy All --------------------------------
    def on_closing():
        camera.release()
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)
