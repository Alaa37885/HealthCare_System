import os
import django

# 👇 مهم جدًا
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from healthcare.models import Patient

from django.contrib.auth.models import User
from healthcare.models import Patient

patients = [
    ("Ahmed Ali", 25),
    ("Omar Hassan", 30),
    ("Khaled Mostafa", 40),
    ("Mohamed Adel", 22),
    ("Youssef Amin", 35),
    ("Hassan Tarek", 28),
    ("Sara Mohamed", 24),
    ("Mona Ahmed", 31),
    ("Laila Fathy", 27),
    ("Heba Adel", 29),
    ("Noor Samir", 20),
    ("Aya Yasser", 23),
    ("Reem Ashraf", 26),
    ("Menna Tarek", 22),
    ("Hana Ali", 25),
    ("Omar Ehab", 31),
    ("Yasmin Fawzy", 27),
    ("Karim Essam", 34),
    ("Farida Ahmed", 23),
    ("Doaa Saeed", 26),
]

for i, (name, age) in enumerate(patients):
    username = name.lower().replace(" ", "_")

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username,
            password="12345678",
            first_name=name.split()[0],
            last_name=name.split()[1] if len(name.split()) > 1 else ""
        )

        Patient.objects.create(
            user=user,
            age=age
        )

print("Patients created successfully!")