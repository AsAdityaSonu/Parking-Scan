import cv2
import customtkinter as ctk
from PIL import Image, ImageTk

bgColor = "#0e1017"


# -------------------------------- Frame Update --------------------------------
def updateFrame(frame, camera):
    ret, img = camera.read()
    if ret:
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        frame.imgtk = img
        frame.configure(image=img)
    frame.after(10, updateFrame, frame, camera)


def Camera(app, cameraNo):
    for widget in app.winfo_children():
        widget.destroy()

    app.title(f"Camera No {cameraNo}")
    app.configure(bg=bgColor)

    camera = cv2.VideoCapture(cameraNo)
    if not camera.isOpened():
        print(f"Error: Cannot open camera {cameraNo}")
        return

    frame = ctk.CTkLabel(
        master=app,
        text=""
    )
    frame.pack(fill="both", expand=True)

    updateFrame(frame, camera)

    # Release camera when the window is closed
    def on_closing():
        camera.release()
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)