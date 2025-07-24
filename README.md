# ✋💡 Hand Gesture-Based Screen Brightness Controller

A real-time Python application that adjusts your screen brightness using hand gestures via webcam. Uses **OpenCV** for video capture and **MediaPipe** for hand tracking.

---

## 🔧 Tech Stack
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- screen-brightness-control

---

## 🚀 How It Works
1. Tracks your hand via webcam.
2. Measures distance between **thumb tip** and **index finger tip**.
3. Maps this distance to a **brightness range (10%–100%)**.
4. Applies brightness using `screen-brightness-control`.

---

## 📁 Files
- `main.py`: Runs the application
- `hand_tracker.py`: Handles hand detection logic
- `requirements.txt`: All dependencies

---

## 📦 Setup Instructions
```bash
pip install -r requirements.txt
python main.py

Use your thumb + index finger gesture to control brightness.
Press Q to exit.

Example Use Case
Touchless brightness control for accessibility, presentations, or hygiene-sensitive environments.

Notes
Requires webcam and admin rights for brightness control.
Works best on Windows/macOS with physical display controls.
