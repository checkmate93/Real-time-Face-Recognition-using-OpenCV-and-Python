             A job of Mantousis Evangelos
# 🎯 Real-time Face Recognition using OpenCV and Python

This project implements **real-time face recognition** using Python, OpenCV, and the `face_recognition` library. It is suitable for building attendance systems, access control mechanisms, or learning about computer vision and machine learning.

---

## 📦 Environment Specifications (Virtual Env)

To ensure compatibility, use the **exact versions** below:

| Package           | Version                         |
|------------------|----------------------------------|
| Python           | 3.10 (64-bit)                   |
| dlib             | 19.22.99 *(custom precompiled)* |
| face_recognition | 1.2.3 *(or 1.3.0 for better compatibility)* |
| numpy            | 1.24.4 *(do NOT use version 2.x!)*
| opencv-python    | 4.11.0.86                       |
| pillow           | 11.3.0                          |
| cmake            | 4.0.3                           |
| cvzone           | 1.6.1                           |
| colorama         | 0.4.6                           |
| click            | 8.2.1                           |

> ⚠️ **Important:** Using other version combinations may cause errors or unexpected behavior.

---

## 🛠 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/Real-time-Face-Recognition-using-OpenCV-and-Python.git
cd Real-time-Face-Recognition-using-OpenCV-and-Python
Create and activate a virtual environment:

bash
Αντιγραφή
Επεξεργασία
python -m venv venv
venv\Scripts\activate  # On Windows
Install required packages:

bash
Αντιγραφή
Επεξεργασία
pip install -r requirements.txt
🚀 Run the Application
To run the program:

Open main.py

Activate the virtual environment

Execute:

bash
Αντιγραφή
Επεξεργασία
python main.py
📂 Suggested Project Structure
perl
Αντιγραφή
Επεξεργασία
Real-time-Face-Recognition-using-OpenCV-and-Python/
│
├── images/               # Folder with known face images
├── Attendance.csv        # CSV log file for recognized faces
├── main.py               # Main script
├── requirements.txt
├── README.md
└── .gitignore
🧠 What main.py Does
Loads known face encodings from images/

Opens webcam feed

Detects and recognizes faces in real-time

Logs attendance (with name & timestamp) into Attendance.csv

⚙️ Requirements
Webcam access

Properly cropped face images in images/ directory

Matching versions of all dependencies

🙌 Credits
Developed by checkmate93
A simple, efficient real-time face recognition system powered by Python and OpenCV.
