from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def clean(self):
        # منع تكرار نفس الدكتور في نفس الوقت
        if Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date
        ).exclude(id=self.id).exists():
            raise ValidationError("This time is already booked!")

    def __str__(self):
        return f"{self.patient} with {self.doctor} at {self.date}"