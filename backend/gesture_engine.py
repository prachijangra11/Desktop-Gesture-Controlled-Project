import cv2
import mediapipe as mp
import numpy as np
import joblib
import pyautogui
import json

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

model = None
try:
    model = joblib.load("model.pkl")
except:
    pass

def execute_action(label):
    with open("gestures.json", "r") as f:
        actions = json.load(f)

    action = actions.get(label)

    if action == "volume_up":
        pyautogui.press("volumeup")
    elif action == "volume_down":
        pyautogui.press("volumedown")
    elif action == "scroll_up":
        pyautogui.scroll(200)
    elif action == "scroll_down":
        pyautogui.scroll(-200)

def start_recognition():
    global model
    if model is None:
        model = joblib.load("model.pkl")

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                landmarks = []
                for lm in handLms.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)

                prediction = model.predict([landmarks])
                execute_action(prediction[0])

        cv2.imshow("Gesture Control", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()