from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime

from .models import Patient, Doctor, Appointment


# =========================
# REGISTER
# =========================
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # إنشاء Patient تلقائي
            Patient.objects.create(
                user=user,
                age=20
            )

            login(request, user)
            return redirect('doctor_list')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# =========================
# DOCTORS LIST
# =========================
def doctor_list(request):
    doctors = Doctor.objects.all()

    specialty = request.GET.get('specialty')
    if specialty:
        doctors = doctors.filter(specialty__icontains=specialty)

    return render(request, 'doctor_list.html', {
        'doctors': doctors
    })


# =========================
# PATIENTS LIST
# =========================
def patient_list(request):
    patients = Patient.objects.all()

    return render(request, 'patient_list.html', {
        'patients': patients
    })


# =========================
# BOOK APPOINTMENT
# =========================
def book_appointment(request):
    success = None
    error = None

    if request.method == "POST":
        try:
            doctor = Doctor.objects.get(id=request.POST.get("doctor"))
            patient = Patient.objects.get(id=request.POST.get("patient"))
            date = parse_datetime(request.POST.get("date"))

            appointment = Appointment(
                doctor=doctor,
                patient=patient,
                date=date
            )

            appointment.clean()
            appointment.save()

            success = "Appointment booked successfully!"

        except Exception:
            error = "This time is already booked or invalid data!"

    return render(request, 'book.html', {
        'doctors': Doctor.objects.all(),
        'patients': Patient.objects.all(),
        'success': success,
        'error': error
    })


# =========================
# APPOINTMENTS LIST 
# =========================
def appointments(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').order_by('-date')

    return render(request, 'appointments.html', {
        'appointments': appointments
    })

