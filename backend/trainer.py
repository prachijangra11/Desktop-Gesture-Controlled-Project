import cv2
import mediapipe as mp
import numpy as np
import joblib
import json
from sklearn.neighbors import KNeighborsClassifier

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

data = []
labels = []

def add_gesture(name):
    cap = cv2.VideoCapture(0)
    print("Show gesture to camera...")

    count = 0
    while count < 50:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                landmarks = []
                for lm in handLms.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)

                data.append(landmarks)
                labels.append(name)
                count += 1

        cv2.imshow("Training Gesture", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

    with open("gestures.json", "r+") as f:
        gestures = json.load(f)
        gestures[name] = "scroll_up"  # default action
        f.seek(0)
        json.dump(gestures, f)

def train_model():
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(data, labels)
    joblib.dump(clf, "model.pkl")