from django.urls import path
from . import views

urlpatterns = [
    path('', views.capture_attendance, name='capture-attendance'),
    path('register_attendance/', views.attendance, name='register-attendance'),
]