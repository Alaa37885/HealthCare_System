import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from healthcare.models import Patient, Doctor
import random

# =========================
# 🧑‍🤝‍🧑 Patients (names from your list)
# =========================

patients = [
    "Adam Khaled", "Lina Ahmed", "Omar Samir", "Mariam Hossam",
    "Youssef Ali", "Sara Tamer", "Hana Mostafa", "Ziad Nabil",
    "Layla Amr", "Karim Hassan",

    "Ali Mahmoud", "Sara Ahmed", "Omar Tarek", "Mona Salah",
    "Youssef Hany", "Heba Adel", "Mostafa Ali", "Nour Hassan",
    "Kareem Saad", "Laila Fathy",

    "Mohamed Nabil", "Dina Samir", "Ahmed Emad", "Reem Ashraf",
    "Hossam Tamer", "Salma Gamal", "Tamer Mostafa", "Noha Adel",
    "Sherif Hossam", "Aya Yasser",

    "Yasmin Fawzy", "Karim Essam", "Menna Tarek", "Mahmoud Reda",
    "Rana Adel", "Ahmed Samy", "Hana Ali", "Omar Ehab",
    "Mariam Mostafa", "Tarek Hany",
]

for i, name in enumerate(patients):
    username = f"patient_{i+1}"

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username,
            password="12345678"
        )

        Patient.objects.create(
            user=user,
            age=random.randint(4, 70)
        )

# =========================
# 👨‍⚕️ Doctors (real names, no doctor1)
# =========================

doctors = [
    ("Ahmed El-Sayed", "Cardiology"),
    ("Omar Hassan", "Cardiology"),
    ("Khaled Mostafa", "Cardiology"),

    ("Mohamed Adel", "Neurology"),
    ("Youssef Amin", "Neurology"),
    ("Tamer Fathy", "Neurology"),

    ("Hany Samir", "Dermatology"),
    ("Sherif Nabil", "Dermatology"),
    ("Amr Zaki", "Dermatology"),

    ("Mostafa Kamal", "Orthopedics"),
    ("Eslam Saeed", "Orthopedics"),
    ("Mahmoud Gamal", "Orthopedics"),

    ("Ali Fawzy", "Pediatrics"),
    ("Hossam Abdelrahman", "Pediatrics"),
    ("Ramy Ashraf", "Pediatrics"),

    ("Karim Adel", "ENT"),
    ("Nader Lotfy", "ENT"),
    ("Mohamed Reda", "ENT"),

    ("Sherif Adel", "Ophthalmology"),
    ("Ahmed Nagi", "Ophthalmology"),
    ("Yasser Fouad", "Ophthalmology"),
]

for name, specialty in doctors:
    username = name.lower().replace(" ", "_")

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username,
            password="12345678"
        )

        Doctor.objects.create(
            user=user,
            specialty=specialty
        )

print("✅ Real names data created successfully!")