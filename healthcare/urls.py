from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('book/', views.book_appointment, name='book'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('patients/', views.patient_list, name='patients'),
    path('appointments/', views.appointments, name='appointments'),
]