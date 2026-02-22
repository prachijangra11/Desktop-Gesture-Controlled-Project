from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gesture_engine import start_recognition
from trainer import add_gesture, train_model
import threading

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Gesture Control Backend Running"}

@app.post("/add-gesture/")
def create_gesture(name: str, action: str):
    add_gesture(name, action)
    return {"message": f"Gesture '{name}' recorded"}
    
@app.post("/train/")
def train():
    train_model()
    return {"message": "Model trained successfully"}

@app.post("/start/")
def start():
    thread = threading.Thread(target=start_recognition)
    thread.start()
    return {"message": "Recognition Started"}