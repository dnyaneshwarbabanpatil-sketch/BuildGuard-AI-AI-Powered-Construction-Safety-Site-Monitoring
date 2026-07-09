from fastapi import FastAPI, WebSocket
import cv2
import asyncio
from ultralytics import YOLO
import google.generativeai as genai

app = FastAPI()
model = YOLO('yolov8n.pt') 

@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        results = model(frame)
        # Process detections...
        
        # Simulating detection flag
        incident_detected = False 
        
        _, buffer = cv2.imencode('.jpg', frame)
        await websocket.send_bytes(buffer.tobytes())
        await asyncio.sleep(0.03)