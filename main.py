import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk

# === Φόρτωση Εικόνων ===
path = 'C:/Users/vagge/PycharmProjects/PythonProject/images'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    img = cv2.imread(os.path.join(path, cl))
    if img is not None:
        images.append(img)
        classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encs = face_recognition.face_encodings(img)
        if encs:
            encodeList.append(encs[0])
    return encodeList

encodeListKnown = findEncodings(images)

attendance_file = 'Attendance.csv'

def load_attendance_names():
    try:
        with open(attendance_file, 'r') as f:
            lines = f.readlines()
            names = set()
            for line in lines:
                if line.strip():
                    names.add(line.split(',')[0])
            return names
    except FileNotFoundError:
        return set()

attendance_names = load_attendance_names()

max_entries = 40
remaining = max_entries - len(attendance_names)

def markAttendance(name):
    global remaining
    if name not in attendance_names and remaining > 0:
        now = datetime.now()
        with open(attendance_file, 'a') as f:
            f.write(f'{name},{now.strftime("%Y-%m-%d %H:%M:%S")}\n')
        attendance_names.add(name)
        remaining -= 1
        update_remaining_label()

# === GUI ===
window = tk.Tk()
window.title("Αναγνώριση Προσώπου")
window.geometry("850x550")
window.configure(bg="lightsteelblue")

professor_label = tk.Label(
    window,
    text="ΔΙΔΑΣΚΩΝ ΚΑΘΗΓΗΤΗΣ Γ. ΜΕΛΕΤΙΟΥ",
    font=("Arial", 14, "bold"),
    bg="lightsteelblue",
    fg="red"
)
professor_label.place(x=490, y=10)

lesson_label = tk.Label(
    window,
    text="Μάθημα: Αρχές Λειτουργικών Συστημάτων",
    font=("Arial", 12),
    bg="lightsteelblue",
    fg="black"
)
lesson_label.place(x=490, y=45)

remaining_label = tk.Label(
    window,
    text=f"Εναπομείνασες Κενές Θέσεις: {remaining}",
    font=("Arial", 16, "bold"),
    bg="lightsteelblue",
    fg="darkred"
)
remaining_label.place(x=490, y=80)

datetime_label = tk.Label(window, font=("Arial", 12), bg="lightsteelblue", fg="black")
datetime_label.place(x=610, y=120)

def update_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datetime_label.config(text=now)
    window.after(1000, update_time)

def update_remaining_label():
    remaining_label.config(text=f"Εναπομείνασες Κενές Θέσεις: {remaining}")

video_label = tk.Label(window, bg="lightsteelblue")
video_label.pack(side="left", padx=20, pady=20)

status_btn = tk.Button(window, text="Περιμένει...", font=("Arial", 14), bg="gray", fg="white", width=25, height=2)
status_btn.pack(side="right", padx=30)

cap = cv2.VideoCapture(0)
last_recognized = None

def reset_button():
    status_btn.config(text="Περιμένει...", bg="gray", fg="white")
    global last_recognized
    last_recognized = None

def show_frame():
    global remaining, last_recognized
    ret, frame = cap.read()
    if not ret:
        return

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(encodeListKnown, face_encoding)
        face_distances = face_recognition.face_distance(encodeListKnown, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = classNames[best_match_index].upper()

            if name != last_recognized:
                if remaining > 0:
                    markAttendance(name)
                    status_btn.config(text=f"✅ Επιτυχία: {name}", bg="green", fg="white")
                    last_recognized = name
                    window.after(3000, reset_button)  # Αλλαγή εδώ στα 3 δευτερόλεπτα
                else:
                    status_btn.config(text="❌ Δεν υπάρχουν θέσεις", bg="red", fg="white")
                    window.after(3000, reset_button)

            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (70, 120, 240), 2)
            cv2.putText(frame, name, (left + 6, bottom + 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (70, 120, 240), 2)

            break

    face_display = cv2.resize(frame, (400, 400))
    face_display = cv2.cvtColor(face_display, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(face_display)
    imgtk = ImageTk.PhotoImage(image=img_pil)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    window.after(10, show_frame)

update_time()
update_remaining_label()
show_frame()
window.mainloop()

cap.release()
cv2.destroyAllWindows()
