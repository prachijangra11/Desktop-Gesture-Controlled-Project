**Gesture Controlled Desktop System**

A customizable, real-time hand gesture recognition system that allows users to train their own gestures and map them to desktop actions (scrolling, volume control, etc.) using computer vision and machine learning.

**Features**

* Custom gesture recording using webcam

* User-defined gesture → action mapping

* Real-time gesture recognition

* Desktop automation via PyAutoGUI

* FastAPI backend + Web-based frontend

* Machine learning using KNN classifier

* MediaPipe hand landmark extraction

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
* 1️⃣ Clone Repository
* 2️⃣ Create Virtual Environment
* 3️⃣ Install Dependencies
  ▶️ Running The Project

Step 1 — Start Backend
Backend runs at:
http://127.0.0.1:8000
Keep this terminal open.

Step 2 — Open Frontend
in your browser

**How To Use**
* 1️⃣ Add & Record Gesture

Enter gesture name

Select desired desktop action

Click Add & Record Gesture

Show your gesture to webcam (50 samples captured)

* 2️⃣ Train Model

Click Train Model

This creates:

model.pkl
* 3️⃣ Start Recognition

Click Start Recognition

Webcam opens

Perform trained gesture

Selected desktop action executes

🎮 Available Desktop Actions

1. Scroll Up

2. Scroll Down

3. Volume Up

4. Volume Down

   (Extendable inside gesture_engine.py)

**Technologies Used**

1. Python

2. FastAPI

3. OpenCV

4. MediaPipe

5. Scikit-learn (KNN)

6. PyAutoGUI

7. HTML, CSS, JavaScript

**Resume Description**

Developed a real-time customizable hand gesture recognition system using MediaPipe and Scikit-learn integrated with FastAPI and a web interface to perform desktop automation tasks via PyAutoGUI.

**Future Improvements**

1. Deep learning-based gesture recognition (CNN)

2. Dataset persistence using CSV storage

3. Gesture deletion & management UI

4. Confidence threshold filtering

5. Adjustable action cooldown

6. Packaged desktop application

7. Multi-gesture recognition support

**Author**

Prachi Jangra
