             A job of Mantousis Evangelos

# 🎯 Real-time Face Recognition using OpenCV and Python

A simple and functional real-time face recognition system using Python and OpenCV.

---

## 🏃 Quick Start

1. **Download or clone the project**
2. **Open it with PyCharm**
3. **Make sure Python 3.10 is installed**
4. **Install required libraries** (see below)
5. **Place your known faces in the `images/` folder**
6. **Run `main.py`**

✅ That’s it! The webcam will start, and known faces will be recognized and logged.

---

## 📦 Required Libraries

Install the following packages (you can use the terminal in PyCharm):

```bash
pip install dlib==19.22.99
pip install face_recognition==1.2.3
pip install numpy==1.24.4
pip install opencv-python==4.11.0.86
pip install pillow==11.3.0
pip install cmake==4.0.3
pip install cvzone==1.6.1
pip install colorama==0.4.6
pip install click==8.2.1
⚠️ Do not use newer versions (especially of dlib, numpy, or face_recognition) unless you test compatibility.
also the install can be with intepreter button

🛠 Full Installation (Detailed)
1. Clone the Repository
bash
Αντιγραφή
Επεξεργασία
git clone https://github.com/your-username/Real-time-Face-Recognition-using-OpenCV-and-Python.git
cd Real-time-Face-Recognition-using-OpenCV-and-Python
2. Create a Virtual Environment
bash
Αντιγραφή
Επεξεργασία
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install All Requirements
bash
Αντιγραφή
Επεξεργασία
pip install -r requirements.txt
If requirements.txt is not included, use the manual installation above.

📂 Folder Structure
perl
Αντιγραφή
Επεξεργασία
Real-time-Face-Recognition-using-OpenCV-and-Python/
│
├── images/               # Folder with known face images
├── Attendance.csv        # Automatically generated attendance log
├── main.py               # Main script to run
├── requirements.txt
└── README.md
🚀 How It Works
Loads faces from images/

Starts webcam and performs live face detection

Recognizes known faces

Logs attendance in Attendance.csv (name + timestamp)

🧠 Credits
Created by checkmate93
A lightweight and educational implementation of real-time face recognition.

🙌 Credits
Developed by checkmate93
A simple, efficient real-time face recognition system powered by Python and OpenCV.
