# YOU NEED TO UPDATE "initialBoundingBoxPositions" according to your video

import sys
from pathlib import Path
import torch
import cv2
import numpy as np

def loadModel():
    repo_path = Path('YOLO/yolov5')

    if repo_path not in sys.path:
        sys.path.append(str(repo_path))

    model = torch.hub.load(str(repo_path), 'custom', path=repo_path / 'yolov5s.pt', source='local')
    return model

# IOU
def computeIOU(box1, box2):
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


def processVideo(videoPath):
    # Load model
    model = loadModel()

    # Load video
    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f'FPS: {fps}, Width: {width}, Height: {height}')

    # Init BB Data
    initialBoundingBoxPositions = [
        (22, 154, 207, 270), (187, 158, 349, 268), (320, 170, 438, 299),
        (430, 180, 550, 310), (560, 175, 690, 300), (670, 180, 800, 310),
        (820, 180, 940, 325), (960, 175, 1100, 310), (1120, 210, 1300, 385)
    ]

    BB = {}
    for i, (x1, y1, x2, y2) in enumerate(initialBoundingBoxPositions):
        boxName = f'Box{i + 1}'
        BB[boxName] = {
            'flag': True, 
            'coordinates': (x1, y1, x2, y2)
        }

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)  
        boxes = results.xyxy[0].numpy()    
        labels = results.names   

        for key in BB.keys():
            BB[key]['flag'] = True  

        # Detect BB
        for box in boxes:
            xmin, ymin, xmax, ymax, confidence, classIDX = box
            label = labels[int(classIDX)]

            if label == 'car':
                current_box = (int(xmin), int(ymin), int(xmax), int(ymax))

                for boxName, boxInfo in BB.items():
                    initial_box = boxInfo['coordinates']
                    iou = computeIOU(initial_box, current_box)
                    if iou > 0.4:
                        BB[boxName]['flag'] = False  

        # Draw
        for boxName, boxInfo in BB.items():
            initial_box = boxInfo['coordinates']
            if boxInfo['flag']:
                color = (0, 255, 0)  
            else:
                color = (0, 0, 255) 

            cv2.rectangle(frame, (initial_box[0], initial_box[1]), (initial_box[2], initial_box[3]), color, 2)
            cv2.putText(frame, boxName, (initial_box[0], initial_box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    for boxName, boxInfo in BB.items():
        print(f"{boxName}: {boxInfo['flag']}")


# Process video from specified path or replace with camera feed for real-time processing
processVideo('Media/Dataset.mp4')