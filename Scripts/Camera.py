import cv2
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime
import os
from pathlib import Path
import sys
import torch

bgColor = "#0e1017"
paused = False

# -------------------------------- Frame Update --------------------------------
# Load model
repo_path = Path('Scripts/Models/yolov5')

if repo_path not in sys.path:
    sys.path.append(str(repo_path))

model = torch.hub.load(str(repo_path), 'custom', path=repo_path / 'yolov5s.pt', source='local')

initialBoundingBoxPositions = [
    (22, 154, 207, 270), (187, 158, 349, 268), (320, 170, 438, 299),
    (430, 180, 550, 310), (560, 175, 690, 300), (670, 180, 800, 310),
    (820, 180, 940, 325), (960, 175, 1100, 310), (1120, 210, 1300, 385)
]

BB = {}
for i, (x1, y1, x2, y2) in enumerate(initialBoundingBoxPositions):
    box_name = f'Box{i + 1}'
    BB[box_name] = {
        'flag': False,
        'coordinates': (x1, y1, x2, y2)
    }

paused = False


def updateSlotLabels(empty_slots_label, filled_slots_label):
    empty_slots = sum(1 for box in BB.values() if not box['flag'])
    filled_slots = len(BB) - empty_slots

    empty_slots_label.configure(text=f"Filled Slots: {empty_slots}")
    filled_slots_label.configure(text=f"Empty Slots: {filled_slots}")


def compute_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1_p, y1_p, x2_p, y2_p = box2

    inter_x1 = max(x1, x1_p)
    inter_y1 = max(y1, y1_p)
    inter_x2 = min(x2, x2_p)
    inter_y2 = min(y2, y2_p)

    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)

    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2_p - x1_p) * (y2_p - y1_p)

    iou = inter_area / float(box1_area + box2_area - inter_area)
    return iou


frame_skip_count = 0


def updateFrame(labelCamera, camera, empty_slots_label, filled_slots_label):
    global paused
    global frame_skip_count
    frame_skip_interval = 5

    ret, frame = camera.read()
    if ret:
        if not paused:
            if frame_skip_count % frame_skip_interval == 0:
                results = model(frame)
                boxes = results.xyxy[0].numpy()
                labels = results.names

                for key in BB.keys():
                    BB[key]['flag'] = True

                for box in boxes:
                    xmin, ymin, xmax, ymax, confidence, class_idx = box
                    label = labels[int(class_idx)]

                    if label == 'car':
                        current_box = (int(xmin), int(ymin), int(xmax), int(ymax))

                        for box_name, box_info in BB.items():
                            initial_box = box_info['coordinates']
                            iou = compute_iou(initial_box, current_box)
                            if iou > 0.4:
                                BB[box_name]['flag'] = False

                # Update the label and draw boxes on the frame
                for box_name, box_info in BB.items():
                    initial_box = box_info['coordinates']
                    if box_name == 'Box6':
                        color = (0, 0, 255)
                        BB['Box6']['flag'] = False
                    else:
                        color = (0, 255, 0) if box_info['flag'] else (0, 0, 255)

                    cv2.rectangle(frame, (initial_box[0], initial_box[1]), (initial_box[2], initial_box[3]), color, 2)
                    cv2.putText(frame, box_name, (initial_box[0], initial_box[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

                # Convert and display the frame in the GUI
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = ImageTk.PhotoImage(img)

                labelCamera.imgtk = img
                labelCamera.configure(image=img)

                updateSlotLabels(empty_slots_label, filled_slots_label)

            frame_skip_count += 1

    frame_delay_ms = 1
    labelCamera.after(frame_delay_ms, updateFrame, labelCamera, camera, empty_slots_label, filled_slots_label)


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

    camera = cv2.VideoCapture('Media/Dataset.mp4')
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

    empty_slots_label = ctk.CTkLabel(
        master=button_frame,
        text="Filled Slots: 0",
        font=("Arial", 18),
        fg_color=bgColor,
        bg_color=bgColor
    )
    empty_slots_label.pack(side="left", padx=20, pady=(10, 30))

    snapshot_button = ctk.CTkButton(
        master=button_frame,
        text="Take Snapshot",
        command=lambda: takeSnapshot(camera),
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

    filled_slots_label = ctk.CTkLabel(
        master=button_frame,
        text="Empty Slots: 0",
        font=("Arial", 18),
        fg_color=bgColor,
        bg_color=bgColor
    )
    filled_slots_label.pack(side="left", padx=20, pady=(10, 30))

    updateSlotLabels(empty_slots_label, filled_slots_label)
    updateFrame(labelCamera, camera, empty_slots_label, filled_slots_label)

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
