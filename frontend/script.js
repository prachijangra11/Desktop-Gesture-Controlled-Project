const API = "http://127.0.0.1:8000";

async function addGesture() {
    const name = document.getElementById("gestureName").value;
    const action = document.getElementById("gestureAction").value;

    if (!name) {
        alert("Please enter gesture name");
        return;
    }

    await fetch(`${API}/add-gesture/?name=${name}&action=${action}`, { method: "POST" });

    alert("Gesture Recorded!");
}

async function trainModel() {
    await fetch(`${API}/train/`, { method: "POST" });
    alert("Model Trained!");
}

async function startRecognition() {
    await fetch(`${API}/start/`, { method: "POST" });
    alert("Recognition Started!");
}