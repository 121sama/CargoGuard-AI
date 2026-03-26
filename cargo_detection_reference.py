import cv2
import torch
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import io

# This is a reference implementation for a Cargo X-Ray Detection Backend
# using YOLOv8 and FastAPI.

class CargoDetector:
    def __init__(self, model_path='yolov8n.pt'):
        # In a real scenario, you would load a custom trained model for X-ray images
        # self.model = torch.hub.load('ultralytics/yolov8', 'custom', path=model_path)
        # For this example, we assume a model is loaded
        print(f"Loading model from {model_path}...")
        
    def preprocess(self, image):
        # Resize and normalize for the model
        image = cv2.resize(image, (640, 640))
        return image

    def detect(self, image):
        # Mock detection results
        # In reality: results = self.model(image)
        # return results.xyxy[0] # [x1, y1, x2, y2, conf, cls]
        return [
            {'bbox': [100, 150, 300, 400], 'label': 'electronics', 'conf': 0.92},
            {'bbox': [400, 50, 550, 200], 'label': 'spare_parts', 'conf': 0.85}
        ]

    def draw_boxes(self, image, detections):
        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            label = det['label']
            conf = det['conf']
            
            # Draw Green Bounding Box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw Label Background
            text = f"{label} {conf:.2f}"
            (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            cv2.rectangle(image, (x1, y1 - 20), (x1 + w, y1), (0, 255, 0), -1)
            
            # Draw Text
            cv2.putText(image, text, (x1, y1 - 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
        return image

app = FastAPI()
detector = CargoDetector()

@app.post("/detect")
async def detect_cargo(file: UploadFile = File(...)):
    # Read image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Process
    # processed_img = detector.preprocess(img)
    detections = detector.detect(img)
    annotated_img = detector.draw_boxes(img, detections)
    
    # Encode and return
    _, encoded_img = cv2.imencode('.jpg', annotated_img)
    return Response(content=encoded_img.tobytes(), media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
