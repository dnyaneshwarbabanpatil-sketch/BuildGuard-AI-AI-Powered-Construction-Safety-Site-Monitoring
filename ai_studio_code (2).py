from ultralytics import YOLO

model = YOLO('yolov8n.pt') # Custom trained on PPE dataset

def detect_ppe(frame):
    results = model(frame)
    # Logic to filter classes: 0: Person, 1: Helmet, 2: Vest
    return results