import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Process frame through YOLO
    # Draw bounding boxes
    # Encode to base64 for Frontend