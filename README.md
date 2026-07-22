# 🚗 Automatic Number Plate Detection and Vehicle Information System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">

<img src="https://img.shields.io/badge/EasyOCR-OCR-red?style=for-the-badge">

<img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">

<img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-yellow?style=for-the-badge">

</p>

---

# 📖 Project Overview

Automatic Number Plate Detection and Vehicle Information System is a real-time vehicle identification project developed using **Python, OpenCV, EasyOCR, YOLOv8 and MySQL Database**.

The system automatically detects vehicle number plates from a live camera or video, extracts the plate number using OCR technology and retrieves the corresponding vehicle owner's information from the database.

This project can be used in:

- 🚗 Smart Parking System
- 🚓 Traffic Monitoring
- 🛡 Security Checkpoints
- 🛣 Toll Collection
- 🏢 University Gate Security
- 🏭 Industrial Vehicle Management

---

# 🎯 Project Objectives

The main objectives of this project are:

- Detect vehicle number plates automatically.
- Read plate numbers using EasyOCR.
- Search vehicle information from MySQL Database.
- Display owner details instantly.
- Save detected plate images.
- Reduce manual work and improve accuracy.

---

# 🖥 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| OpenCV | Image Processing |
| EasyOCR | Number Plate Recognition |
| YOLOv8 | Object Detection |
| Haar Cascade | Number Plate Detection |
| MySQL | Vehicle Database |
| SQLite | Local Testing Database |
| VS Code | Development Environment |

---

# ⚙️ System Workflow

```
Camera / Video

↓

Vehicle Detection (YOLOv8)

↓

Number Plate Detection

↓

Image Preprocessing

↓

EasyOCR

↓

Extract Plate Number

↓

Search Database

↓

Display Vehicle Information

↓

Save Plate Image
```

---

# ✨ Features

✅ Real-Time Number Plate Detection

✅ Vehicle Detection using YOLOv8

✅ OCR using EasyOCR

✅ Fast Image Processing

✅ Automatic Database Search

✅ Vehicle Information Display

✅ Save Plate Images

✅ User Friendly Interface

✅ High Detection Accuracy

---

# 🗄 Database Structure

```sql
CREATE TABLE vehicles (

id INT AUTO_INCREMENT PRIMARY KEY,

plate_number VARCHAR(20),

owner_name VARCHAR(100),

location VARCHAR(100),

country VARCHAR(100)

);
```

### Sample Database

| Plate Number | Owner | Location | Country |
|--------------|---------|----------|----------|
|0007|Rahim Ahmed|Dhaka|Bangladesh|
|C06S0B38|Ivan Petrov|Moscow|Russia|
|DHAKA1234|Sakib Hasan|Tangail|Bangladesh|

---

# 📸 Project Output

## Number Plate Detection

![Detection](Result%20final1.png)

---

## OCR Recognition

![OCR](Result%20final2.png)

---

## Vehicle Information

![Vehicle](Result%20Info.png)

---

## Vehicle Not Found

![Not Found](Result%20not.png)

---

# 🎥 Project Demo Video

▶️ Watch on YouTube

https://youtu.be/PASTE_YOUR_VIDEO_LINK_HERE

---

# 📂 Project Structure

```
Car-Number-Plates/

│

├── model/

│ └── haarcascade_russian_plate_number.xml

│

├── plates/

│

├── number_plate.py

├── vehicles.db

├── requirements.txt

├── README.md

├── .gitignore

│

├── Result final1.png

├── Result final2.png

├── Result final3.png

├── Result Info.png

└── Result not.png
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/apurbaroyy/Car-Number-Plates.git
```

Go to project folder

```bash
cd Car-Number-Plates
```

Install required packages

```bash
pip install -r requirements.txt
```

Run the project

```bash
python number_plate.py
```

---

# 📌 Future Improvements

- Web Dashboard
- Mobile Application
- Cloud Database
- Face Recognition
- Multiple Camera Support
- Vehicle Tracking
- Fine Management System
- AI Based Vehicle Analytics

---

# 👨‍💻 Developer

## Apurba Chandra Roy

Department of Information and Communication Technology (ICT)

Mawlana Bhashani Science and Technology University

Tangail-1902, Bangladesh

---

# 🎓 Supervisor

**Dr. Ziaur Rahaman**

Professor

Department of Information and Communication Technology (ICT)

Mawlana Bhashani Science and Technology University

---

# 📜 License

This project is developed for academic and educational purposes.

© 2026 Apurba Chandra Roy. All Rights Reserved.

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

Thank you for visiting this repository.
