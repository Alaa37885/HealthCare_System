# 🏥 HealthCare System

A simple Hospital Management System built with Django that allows managing doctors, patients, and appointments in an easy and organized way.

---

## 🚀 Features

- 👨‍⚕️ View list of doctors  
- 🧑 View list of patients  
- 📅 Book appointments between doctors and patients  
- 📋 View all booked appointments  
- 🔍 Search doctors by specialty  
- 🔐 User registration with automatic patient creation  

---

## 🛠️ Tech Stack

- Python 3  
- Django Framework  
- HTML / CSS  
- SQLite Database  

---

## 📂 Project Structure

HealthCare_System/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/
│   └── images/
│       ├── doctors.png
│       ├── book.png
│       └── appointments.png
│
├── db.sqlite3
├── manage.py

---

## ⚙️ Installation & Setup

1. Clone the repository  
git clone https://github.com/Alaa37885/HealthCare_System.git  
cd HealthCare_System  

2. Create virtual environment  
python -m venv venv  
venv\\Scripts\\activate   # Windows  

3. Install dependencies  
pip install django  

4. Run migrations  
python manage.py makemigrations  
python manage.py migrate  

5. Create superuser  
python manage.py createsuperuser  

6. Run server  
python manage.py runserver  

---

## 🌐 Pages

- /doctors/ → Doctors List  
- /book/ → Book Appointment  
- /appointments/ → View Appointments  
- /patients/ → Patients List  
- /admin/ → Django Admin Panel  

---

## 📸 UI Preview

- ![Interface](Result_img.png)


---

## 💡 Future Improvements

- Dashboard analytics  
- Doctor availability system  
- Appointment status system  
- Django REST API integration  
- Modern UI (Bootstrap / React)  

---

## 👩‍💻 Author

Alaa Omar Hamed  

---

⭐ If you like this project, please star it!
"""
