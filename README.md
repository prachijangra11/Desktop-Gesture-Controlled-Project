**Gesture Controlled Desktop System**

A customizable, real-time hand gesture recognition system that allows users to train their own gestures and map them to desktop actions (scrolling, volume control, etc.) using computer vision and machine learning.

**Features**

Custom gesture recording using webcam

User-defined gesture → action mapping

Real-time gesture recognition

Desktop automation via PyAutoGUI

FastAPI backend + Web-based frontend

Machine learning using KNN classifier

MediaPipe hand landmark extraction

**System Architecture**
Browser (Frontend UI)
        ↓
FastAPI Backend
        ↓
MediaPipe (Hand Landmark Detection)
        ↓
KNN Model (Gesture Classification)
        ↓
PyAutoGUI (Desktop Automation)

**Installation Guide**
1️⃣ Clone Repository
git clone https://github.com/yourusername/Desktop-Gesture-Controlled-Project.git
cd Desktop-Gesture-Controlled-Project
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is missing:

pip install fastapi uvicorn opencv-python mediapipe scikit-learn joblib pyautogui numpy
▶️ Running The Project
Step 1 — Start Backend

Go into backend folder:

cd backend
uvicorn app:app --reload

Backend runs at:

http://127.0.0.1:8000

Keep this terminal open.

Step 2 — Open Frontend

Open:

frontend/index.html

in your browser
(or use VS Code Live Server)

**How To Use**
1️⃣ Add & Record Gesture

Enter gesture name

Select desired desktop action

Click Add & Record Gesture

Show your gesture to webcam (50 samples captured)

2️⃣ Train Model

Click Train Model

This creates:

model.pkl
3️⃣ Start Recognition

Click Start Recognition

Webcam opens

Perform trained gesture

Selected desktop action executes

🎮 Available Desktop Actions

Scroll Up

Scroll Down

Volume Up

Volume Down

(Extendable inside gesture_engine.py)

**Technologies Used**

Python

FastAPI

OpenCV

MediaPipe

Scikit-learn (KNN)

PyAutoGUI

HTML, CSS, JavaScript

**Resume Description**

Developed a real-time customizable hand gesture recognition system using MediaPipe and Scikit-learn integrated with FastAPI and a web interface to perform desktop automation tasks via PyAutoGUI.

**Future Improvements**

Deep learning-based gesture recognition (CNN)

Dataset persistence using CSV storage

Gesture deletion & management UI

Confidence threshold filtering

Adjustable action cooldown

Packaged desktop application

Multi-gesture recognition support

**Author**

Prachi Jangra
